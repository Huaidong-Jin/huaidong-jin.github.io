import './globals.css';
import { Inter } from 'next/font/google';
import { Metadata } from 'next';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  metadataBase: new URL('https://jimmykin.github.io'),
  title: {
    default: 'Jimmy Kin Blog',
    template: '%s | Jimmy Kin Blog',
  },
  description: 'Lifelong Generative AI & Robotics Pitfall Explorer',
  keywords: ['blog', 'AI', 'robotics', 'technology', 'Jimmy Kin'],
  authors: [{ name: 'Jimmy Kin' }],
  creator: 'Jimmy Kin',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://jimmykin.github.io/',
    title: 'Jimmy Kin Blog',
    description: 'Lifelong Generative AI & Robotics Pitfall Explorer',
    siteName: 'Jimmy Kin Blog',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Jimmy Kin Blog',
    description: 'Lifelong Generative AI & Robotics Pitfall Explorer',
    creator: '@JimmyKin',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" data-theme="light">
      <body className={inter.className}>
        <div className="min-h-screen flex flex-col">
          <Header />
          <main className="flex-1">{children}</main>
          <Footer />
        </div>
      </body>
    </html>
  );
} 