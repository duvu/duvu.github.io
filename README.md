# Personal Portfolio Website

A modern, responsive personal portfolio website built with HTML, Tailwind CSS, and JavaScript. The site showcases personal information, skills, GitHub statistics, projects, and includes a contact form.

## Features

- **Modern Design**: Clean and professional layout with Tailwind CSS
- **Responsive**: Fully responsive design that works on all devices
- **Dark Mode**: Toggle between light and dark themes with persistent preferences
- **GitHub Integration**: Dynamic GitHub stats with caching for performance
- **Performance Optimized**: Lazy loading, resource hints, and image optimization
- **Accessibility**: ARIA attributes, keyboard navigation, and screen reader support
- **SEO Friendly**: Meta tags, Open Graph, and Twitter card support
- **Security**: Form validation, honeypot fields, and sanitization

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/duvu/duvu.github.io.git
   cd duvu.github.io
   ```

2. **Local Development**
   - Open the `index.html` file in your browser to view the site locally
   - For a development server with live reloading, you can use:
     ```bash
     npx serve
     ```
     or
     ```bash
     npx http-server
     ```

3. **Deploy to GitHub Pages**
   - Push changes to your `main` branch
   - GitHub Pages will automatically build and deploy your site
   - Your site will be available at `https://<username>.github.io`

## Customization

### Personal Information
Edit these sections in the `index.html` file:
- Header section: Update name, title, and social media links
- About section: Change the personal description
- Skills section: Update the skills and proficiency levels
- Contact section: Update contact details

### GitHub Integration
The website automatically fetches GitHub statistics using the GitHub API. Customize the GitHub integration by:
1. Changing the GitHub username in the `fetchGitHubData()` function
2. Modifying the display of repositories in the `displayRepositories()` function
3. Adjusting caching settings in the codebase

### Dark Mode
The website includes a dark mode toggle that:
1. Remembers user preferences using localStorage
2. Respects system preferences by default
3. Provides a smooth transition between themes

## JavaScript Functions

The website includes the following core functionality:

- `setupDarkMode()`: Handles theme switching and preference storage
- `setupAccessibility()`: Adds accessibility features like skip links
- `setupContactForm()`: Manages form validation and submission
- `fetchGitHubData()`: Retrieves GitHub statistics with caching
- `displayRepositories()`: Renders repository information
- `showNotification()`: Displays user notifications

## Browser Compatibility

The website is compatible with:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Android Chrome)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Tailwind CSS](https://tailwindcss.com/) for styling
- [Font Awesome](https://fontawesome.com/) for icons
- [GitHub API](https://docs.github.com/en/rest) for GitHub statistics 