import Link from 'next/link';
import { getPosts } from '@/lib/getPosts';

export default async function HomePage() {
  const posts = await getPosts();
  const featuredPosts = posts.slice(0, 3);

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      {/* Hero Section */}
      <section className="text-center py-20">
        <h1 className="text-5xl font-bold mb-4 text-foreground">
          Hi, I am Huaidong Jin
        </h1>
        <h2 className="text-2xl text-foreground/80 mb-8">
          Lifelong Generative AI & Robotics Pitfall Explorer
        </h2>
        <div className="flex justify-center gap-4">
          <Link
            href="/about"
            className="px-6 py-3 bg-foreground text-background rounded-lg hover:opacity-80 transition-opacity"
          >
            About Me
          </Link>
          <Link
            href="/posts"
            className="px-6 py-3 border border-foreground text-foreground rounded-lg hover:bg-foreground hover:text-background transition-colors"
          >
            Read Blog
          </Link>
        </div>
      </section>

      {/* Featured Posts */}
      {featuredPosts.length > 0 && (
        <section className="py-16">
          <h2 className="text-3xl font-bold text-center mb-12 text-foreground">
            Latest Posts
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredPosts.map((post) => (
              <article
                key={post.slug}
                className="border border-foreground/20 rounded-lg p-6 hover:shadow-lg transition-shadow"
              >
                <h3 className="text-xl font-semibold mb-3 text-foreground">
                  <Link
                    href={`/posts/${post.slug}`}
                    className="hover:opacity-80"
                  >
                    {post.title}
                  </Link>
                </h3>
                <p className="text-foreground/70 mb-4 line-clamp-3">
                  {post.summary}
                </p>
                <div className="flex justify-between items-center text-sm text-foreground/60">
                  <time dateTime={post.date}>{post.formattedDate}</time>
                  <span>{post.readingTime}</span>
                </div>
              </article>
            ))}
          </div>
          <div className="text-center mt-12">
            <Link
              href="/posts"
              className="inline-block px-6 py-3 border border-foreground text-foreground rounded-lg hover:bg-foreground hover:text-background transition-colors"
            >
              View All Posts
            </Link>
          </div>
        </section>
      )}
    </div>
  );
} 