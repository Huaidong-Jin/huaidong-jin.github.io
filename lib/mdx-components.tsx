import Link from 'next/link';
import { MDXComponents } from 'mdx/types';

export const mdxComponents: MDXComponents = {
  h1: ({ children }) => (
    <h1 className="text-4xl font-bold mb-6 text-foreground">{children}</h1>
  ),
  h2: ({ children }) => (
    <h2 className="text-3xl font-semibold mb-5 mt-8 text-foreground">{children}</h2>
  ),
  h3: ({ children }) => (
    <h3 className="text-2xl font-medium mb-4 mt-6 text-foreground">{children}</h3>
  ),
  h4: ({ children }) => (
    <h4 className="text-xl font-medium mb-3 mt-5 text-foreground">{children}</h4>
  ),
  p: ({ children }) => (
    <p className="mb-4 leading-relaxed text-foreground">{children}</p>
  ),
  a: ({ href, children }) => {
    if (href?.startsWith('http')) {
      return (
        <a
          href={href}
          target="_blank"
          rel="noopener noreferrer"
          className="text-foreground underline hover:opacity-80"
        >
          {children}
        </a>
      );
    }
    return (
      <Link href={href || '#'} className="text-foreground underline hover:opacity-80">
        {children}
      </Link>
    );
  },
  ul: ({ children }) => (
    <ul className="mb-4 ml-6 list-disc text-foreground">{children}</ul>
  ),
  ol: ({ children }) => (
    <ol className="mb-4 ml-6 list-decimal text-foreground">{children}</ol>
  ),
  li: ({ children }) => (
    <li className="mb-1 text-foreground">{children}</li>
  ),
  blockquote: ({ children }) => (
    <blockquote className="border-l-4 border-foreground/30 pl-4 my-6 italic text-foreground/80">
      {children}
    </blockquote>
  ),
  code: ({ children }) => (
    <code className="bg-foreground/10 px-2 py-1 rounded text-sm font-mono text-foreground">
      {children}
    </code>
  ),
  pre: ({ children }) => (
    <pre className="bg-foreground/5 border border-foreground/20 rounded-lg p-4 my-6 overflow-x-auto">
      {children}
    </pre>
  ),
  table: ({ children }) => (
    <div className="overflow-x-auto my-6">
      <table className="min-w-full border border-foreground/20 text-foreground">
        {children}
      </table>
    </div>
  ),
  th: ({ children }) => (
    <th className="border border-foreground/20 px-4 py-2 bg-foreground/5 font-semibold text-left">
      {children}
    </th>
  ),
  td: ({ children }) => (
    <td className="border border-foreground/20 px-4 py-2">{children}</td>
  ),
  hr: () => (
    <hr className="my-8 border-t border-foreground/20" />
  ),
  div: ({ children, ...props }) => (
    <div {...props}>{children}</div>
  ),
}; 