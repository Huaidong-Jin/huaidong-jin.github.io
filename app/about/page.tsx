import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'About',
  description: 'Learn more about Huaidong Jin',
};

export default function AboutPage() {
  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <article className="prose prose-lg max-w-none">
        <h1>About Me</h1>
        <div className="content">
          <p>
            Hello! I am Huaidong Jin, a passionate advocate of technology and innovation.
            As a lifelong explorer of Generative AI & Robotics, I&apos;m constantly diving into
            the fascinating world of artificial intelligence and its applications.
          </p>
          
          <h2>What I Do</h2>
          <p>
            I specialize in exploring the cutting edge of generative AI and robotics,
            sharing insights, challenges, and discoveries along the way. My work involves:
          </p>
          
          <ul>
            <li>Researching and experimenting with AI technologies</li>
            <li>Building and testing robotic systems</li>
            <li>Writing about the latest developments in the field</li>
            <li>Sharing knowledge through technical articles and tutorials</li>
          </ul>
          
          <h2>Connect With Me</h2>
          <p>Feel free to connect with me on:</p>
          <ul>
            <li>
              GitHub: <a href="https://github.com/JimmyKin" target="_blank" rel="noopener noreferrer">@JimmyKin</a>
            </li>
          </ul>
          
          <p>
            I believe in the power of sharing knowledge and learning from the community.
            Whether you&apos;re a fellow developer, researcher, or someone curious about AI and robotics,
            I hope you&apos;ll find value in the content I share here.
          </p>
        </div>
      </article>
    </div>
  );
} 