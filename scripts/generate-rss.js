const fs = require('fs');
const path = require('path');
const { getPosts } = require('../lib/getPosts');

async function generateRSS() {
  try {
    const posts = await getPosts();
    const siteUrl = 'https://jimmy.github.io';
    
    const rssItems = posts
      .slice(0, 10) // Only latest 10 posts
      .map(post => `
    <item>
      <title><![CDATA[${post.title}]]></title>
      <description><![CDATA[${post.summary}]]></description>
      <link>${siteUrl}/posts/${post.slug}/</link>
      <guid>${siteUrl}/posts/${post.slug}/</guid>
      <pubDate>${new Date(post.date).toUTCString()}</pubDate>
    </item>`)
      .join('');

    const rssXml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Huaidong Jin Blog</title>
    <description>Lifelong Generative AI & Robotics Pitfall Explorer</description>
    <link>${siteUrl}</link>
    <language>en</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <managingEditor>jimmy@example.com (Huaidong Jin)</managingEditor>
    <webMaster>jimmy@example.com (Huaidong Jin)</webMaster>
    ${rssItems}
  </channel>
</rss>`;

    // Ensure public directory exists
    const publicDir = path.join(process.cwd(), 'public');
    if (!fs.existsSync(publicDir)) {
      fs.mkdirSync(publicDir, { recursive: true });
    }

    // Write RSS file
    fs.writeFileSync(path.join(publicDir, 'rss.xml'), rssXml);
    
    console.log('RSS feed generated successfully!');
  } catch (error) {
    console.error('Error generating RSS feed:', error);
    process.exit(1);
  }
}

generateRSS(); 