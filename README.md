# duvu.github.io

Personal profile page of Du Quang Vu — Senior Backend Software Engineer. Published at <https://duvu.github.io>.

A single static page (`index.html`, plain HTML/CSS/JS, no build step) with light/dark themes, responsive layout and print styles.

## Structure

```
index.html                      # the page
data/github-stats.json          # GitHub statistics rendered in the "GitHub activity" section
scripts/update_github_stats.py  # regenerates data/github-stats.json
imgs/                           # profile photo and project screenshots
```

## Preview locally

The page loads `data/github-stats.json` with `fetch`, so serve it over HTTP instead of opening the file directly:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Refresh GitHub statistics

The stats are a snapshot so the page never hits GitHub API rate limits. To refresh them:

```bash
gh auth login        # once, as the profile owner
python3 scripts/update_github_stats.py
git add data/github-stats.json && git commit -m "Update GitHub stats" && git push
```

Contribution counts include private contributions (as aggregate numbers only) because the script runs with your own token.

## Deploy

Push to `main`; GitHub Pages serves the repository root.
