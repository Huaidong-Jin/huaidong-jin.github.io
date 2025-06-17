const withMDX = require('@next/mdx')({
  extension: /\.mdx?$/,
  options: {
    // Simplified configuration without ES module plugins for now
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
};

module.exports = withMDX(nextConfig); 