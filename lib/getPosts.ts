import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { format } from 'date-fns';

export interface Post {
  slug: string;
  title: string;
  date: string;
  formattedDate: string;
  summary: string;
  readingTime: string;
  tags?: string[];
  content: string;
}

const postsDirectory = path.join(process.cwd(), 'content/posts');

export async function getPosts(): Promise<Post[]> {
  // Check if directory exists, create if not
  if (!fs.existsSync(postsDirectory)) {
    fs.mkdirSync(postsDirectory, { recursive: true });
    return [];
  }

  const fileNames = fs.readdirSync(postsDirectory);
  const allPostsData = fileNames
    .filter((name) => name.endsWith('.mdx'))
    .map((fileName) => {
      const slug = fileName.replace(/\.mdx$/, '');
      const fullPath = path.join(postsDirectory, fileName);
      const fileContents = fs.readFileSync(fullPath, 'utf8');

      const { data, content } = matter(fileContents);

      return {
        slug,
        title: data.title || 'Untitled',
        date: data.date || new Date().toISOString(),
        formattedDate: format(new Date(data.date || new Date()), 'MMMM dd, yyyy'),
        summary: data.summary || data.description || extractSummary(content),
        readingTime: calculateReadingTime(content),
        tags: data.tags || [],
        content,
      } as Post;
    });

  return allPostsData.sort((a, b) => (a.date < b.date ? 1 : -1));
}

export async function getPostBySlug(slug: string): Promise<Post | null> {
  try {
    const fullPath = path.join(postsDirectory, `${slug}.mdx`);
    const fileContents = fs.readFileSync(fullPath, 'utf8');
    const { data, content } = matter(fileContents);

    return {
      slug,
      title: data.title || 'Untitled',
      date: data.date || new Date().toISOString(),
      formattedDate: format(new Date(data.date || new Date()), 'MMMM dd, yyyy'),
      summary: data.summary || data.description || extractSummary(content),
      readingTime: calculateReadingTime(content),
      tags: data.tags || [],
      content,
    } as Post;
  } catch (error) {
    return null;
  }
}

function extractSummary(content: string, maxLength = 160): string {
  // Remove markdown formatting and get plain text
  const plainText = content
    .replace(/#{1,6}\s+/g, '') // Remove headers
    .replace(/\*\*(.*?)\*\*/g, '$1') // Remove bold
    .replace(/\*(.*?)\*/g, '$1') // Remove italic
    .replace(/`(.*?)`/g, '$1') // Remove inline code
    .replace(/\[(.*?)\]\(.*?\)/g, '$1') // Remove links
    .replace(/\n+/g, ' ') // Replace newlines with spaces
    .trim();

  if (plainText.length <= maxLength) {
    return plainText;
  }

  return plainText.substring(0, maxLength).trim() + '...';
}

function calculateReadingTime(content: string): string {
  const wordsPerMinute = 200;
  const words = content.split(/\s+/).length;
  const readingTimeMinutes = Math.ceil(words / wordsPerMinute);
  return `${readingTimeMinutes} min read`;
} 