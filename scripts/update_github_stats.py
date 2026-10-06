#!/usr/bin/env python3
"""Regenerate data/github-stats.json from the GitHub API.

Requires the GitHub CLI (`gh`) logged in as the profile owner, so that
contribution counts include private work (shown only as aggregate numbers).

    python3 scripts/update_github_stats.py
"""
import collections
import datetime as dt
import json
import pathlib
import subprocess

USER = "duvu"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "github-stats.json"


def gh(*args):
    return json.loads(subprocess.check_output(["gh", "api", *args]))


def graphql(query):
    return gh("graphql", "-f", f"query={query}")["data"]["user"]


def main():
    today = dt.date.today()
    profile = gh(f"users/{USER}")
    repos = gh("--paginate", "--slurp", f"users/{USER}/repos?per_page=100&type=owner")
    repos = [r for page in repos for r in page]
    sources = [r for r in repos if not r["fork"]]

    years = graphql(f'{{ user(login:"{USER}") {{ contributionsCollection {{ contributionYears }} }} }}')
    years = sorted(years["contributionsCollection"]["contributionYears"])

    fields = "contributionCalendar { totalContributions } totalCommitContributions totalPullRequestContributions"
    parts = [
        f'y{y}: contributionsCollection(from:"{y}-01-01T00:00:00Z", to:"{y}-12-31T23:59:59Z") {{ {fields} }}'
        for y in years
    ]
    last_year = (today - dt.timedelta(days=365)).isoformat()
    parts.append(
        f'last: contributionsCollection(from:"{last_year}T00:00:00Z", to:"{today.isoformat()}T23:59:59Z") '
        f"{{ {fields} totalIssueContributions totalRepositoriesWithContributedCommits }}"
    )
    parts.append("organizations(first:100) { totalCount }")
    data = graphql(f'{{ user(login:"{USER}") {{ {" ".join(parts)} }} }}')

    by_year = [
        {"year": y, "contributions": data[f"y{y}"]["contributionCalendar"]["totalContributions"]}
        for y in years
    ]
    last = data["last"]
    languages = collections.Counter(r["language"] for r in sources if r["language"])

    stats = {
        "generated_at": today.isoformat(),
        "member_since": profile["created_at"][:10],
        "public_repos": profile["public_repos"],
        "original_repos": len(sources),
        "followers": profile["followers"],
        "organizations": data["organizations"]["totalCount"],
        "total_contributions": sum(y["contributions"] for y in by_year),
        "last_12_months": {
            "contributions": last["contributionCalendar"]["totalContributions"],
            "commits": last["totalCommitContributions"],
            "pull_requests": last["totalPullRequestContributions"],
            "issues": last["totalIssueContributions"],
            "repositories": last["totalRepositoriesWithContributedCommits"],
        },
        "contributions_by_year": by_year,
        "languages_by_repo": [{"name": k, "repos": v} for k, v in languages.most_common(8)],
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
