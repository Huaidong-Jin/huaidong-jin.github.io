'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Header() {
  const pathname = usePathname();

  return (
    <header className="border-b border-foreground/20 bg-background">
      <div className="max-w-4xl mx-auto px-6 py-4">
        <nav className="flex justify-between items-center">
          <div className="logo">
            <Link
              href="/"
              className="text-2xl font-bold text-foreground hover:opacity-80"
            >
              Jimmy Kin
            </Link>
          </div>
          <div className="nav-links flex gap-8">
            <Link
              href="/"
              className={`text-foreground hover:opacity-80 transition-opacity ${
                pathname === '/' ? 'font-medium' : ''
              }`}
            >
              Home
            </Link>
            <Link
              href="/posts"
              className={`text-foreground hover:opacity-80 transition-opacity ${
                pathname.startsWith('/posts') ? 'font-medium' : ''
              }`}
            >
              Posts
            </Link>
            <Link
              href="/about"
              className={`text-foreground hover:opacity-80 transition-opacity ${
                pathname === '/about' ? 'font-medium' : ''
              }`}
            >
              About
            </Link>
            <a
              href="https://github.com/JimmyKin"
              target="_blank"
              rel="noopener noreferrer"
              className="text-foreground hover:opacity-80 transition-opacity"
            >
              Projects
            </a>
          </div>
        </nav>
      </div>
    </header>
  );
} 