import Link from 'next/link';
import { Metadata } from 'next';
import { getPosts } from '@/lib/getPosts';

export const metadata: Metadata = {
  title: 'Posts',
  description: 'All blog posts by Huaidong Jin',
};

export default async function PostsPage() {
  const posts = await getPosts();

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <h1 className="text-4xl font-bold mb-12 text-foreground">All Posts</h1>
      
      {posts.length === 0 ? (
        <div className="text-center py-20">
          <p className="text-foreground/70 mb-4">No posts found.</p>
          <p className="text-foreground/60">Check back later for new content!</p>
        </div>
      ) : (
        <div className="space-y-8">
          {posts.map((post) => (
            <article
              key={post.slug}
              className="border-b border-foreground/20 pb-8 last:border-b-0"
            >
              <h2 className="text-2xl font-semibold mb-3 text-foreground">
                <Link
                  href={`/posts/${post.slug}`}
                  className="hover:opacity-80 transition-opacity"
                >
                  {post.title}
                </Link>
              </h2>
              
              <div className="flex items-center gap-4 text-sm text-foreground/60 mb-4">
                <time dateTime={post.date}>{post.formattedDate}</time>
                <span>•</span>
                <span>{post.readingTime}</span>
                {post.tags && post.tags.length > 0 && (
                  <>
                    <span>•</span>
                    <div className="flex gap-2">
                      {post.tags.map((tag) => (
                        <span
                          key={tag}
                          className="px-2 py-1 bg-foreground/10 rounded-md text-xs"
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                  </>
                )}
              </div>
              
              <p className="text-foreground/80 leading-relaxed">
                {post.summary}
              </p>
            </article>
          ))}
        </div>
      )}
    </div>
  );
} 