# Huaidong Jin Blooog

A modern, minimalist blog built with Next.js 13, featuring a clean black and white design inspired by Overreacted.io.

## 🚀 Features

- **Next.js 13** with App Router
- **MDX** support for rich content
- **Tailwind CSS** for styling
- **TypeScript** for type safety
- **Static Generation** for optimal performance
- **RSS Feed** generation
- **SEO Optimized** with proper meta tags
- **Responsive Design** for all devices
- **GitHub Actions** for CI/CD
- **GitHub Pages** deployment

## 📁 Project Structure

```
├── app/                    # Next.js app directory
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Home page
│   ├── about/page.tsx     # About page
│   └── posts/
│       ├── page.tsx       # Posts list
│       └── [slug]/page.tsx # Individual post
├── components/            # React components
│   ├── Header.tsx
│   ├── Footer.tsx
│   └── ...
├── content/
│   └── posts/            # MDX blog posts
├── lib/                  # Utility functions
│   ├── getPosts.ts       # Post fetching logic
│   └── mdx-components.tsx # MDX components
├── public/               # Static assets
└── scripts/
    └── generate-rss.js   # RSS generation
```

## 🛠️ Tech Stack

- **Framework**: Next.js 13
- **Styling**: Tailwind CSS
- **Content**: MDX
- **Language**: TypeScript
- **Testing**: Jest + React Testing Library
- **E2E Testing**: Cypress
- **Deployment**: GitHub Pages
- **CI/CD**: GitHub Actions

## 🚀 Getting Started

### Prerequisites

- Node.js 16+ 
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Huaidong-Jin/huaidong-jin.github.io.git
cd huaidong-jin.github.io
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 📝 Writing Posts

Create new MDX files in the `content/posts/` directory with the following frontmatter:

```mdx
---
title: "Your Post Title"
date: "2024-01-01"
summary: "A brief description of your post"
tags: ["tag1", "tag2"]
---

Your post content here...
```

## 🎨 Customization

### Theme Colors

The blog uses CSS variables for theming. Edit `app/globals.css`:

```css
:root {
  --bg: #fff;
  --fg: #000;
}

[data-theme="dark"] {
  --bg: #000;
  --fg: #fff;
}
```

### Site Configuration

Update site metadata in `app/layout.tsx` and `scripts/generate-rss.js`.

## 📦 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier
- `npm run test` - Run tests
- `npm run generate-rss` - Generate RSS feed

## 🚀 Deployment

The blog is automatically deployed to GitHub Pages using GitHub Actions. On every push to the main branch:

1. Dependencies are installed
2. Code is linted and tested
3. Site is built and exported
4. RSS feed is generated
5. Site is deployed to GitHub Pages

## 🧪 Testing

Run tests with:

```bash
npm run test
```

For end-to-end testing:

```bash
npm run cypress:open
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Huaidong Jin**
- GitHub: [@Huaidong-Jin](https://github.com/Huaidong-Jin)
- Website: [huaidong-jin.github.io](https://huaidong-jin.github.io)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Huaidong-Jin/huaidong-jin.github.io/issues).

---

Built with ❤️ by Huaidong Jin