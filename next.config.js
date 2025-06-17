const withMDX = require('@next/mdx')({
  extension: /\.mdx?$/,
  options: {
    remarkPlugins: [require('remark-gfm')],
    rehypePlugins: [
      require('rehype-slug'),
      require('rehype-autolink-headings'),
      require('rehype-highlight')
    ],
  },
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['ts', 'tsx', 'js', 'jsx', 'md', 'mdx'],
  images: {
    unoptimized: true,
  },
  trailingSlash: true,
  output: 'export',
  basePath: process.env.NODE_ENV === 'production' ? '/huaidong-blog' : '',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/huaidong-blog' : '',
};

module.exports = withMDX(nextConfig); 