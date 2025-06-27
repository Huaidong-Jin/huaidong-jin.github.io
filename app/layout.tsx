import './globals.css';
import { Inter } from 'next/font/google';
import { Metadata } from 'next';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  metadataBase: new URL('https://huaidong-jin.github.io'),
  title: {
    default: 'Huaidong Jin Blog',
    template: '%s | Huaidong Jin Blog',
  },
  description: 'Lifelong Generative AI & Robotics Pitfall Explorer',
  keywords: ['blog', 'AI', 'robotics', 'technology', 'Huaidong Jin'],
  authors: [{ name: 'Huaidong Jin' }],
  creator: 'Huaidong Jin',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://huaidong-jin.github.io/',
    title: 'Huaidong Jin Blog',
    description: 'Lifelong Generative AI & Robotics Pitfall Explorer',
    siteName: 'Huaidong Jin Blog',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Huaidong Jin Blog',
    description: 'Lifelong Generative AI & Robotics Pitfall Explorer',
    creator: '@HuaidongJin',
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