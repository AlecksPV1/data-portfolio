import React from 'react';
import { motion } from 'framer-motion';
import { TypeAnimation } from 'react-type-animation';
import { ArrowRight } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';

const Hero = () => {
  const { content, lang } = useLanguage();
  
  // Force remount of TypeAnimation when language changes to restart sequence
  const typewriterKey = `typewriter-${lang}`;

  return (
    <section id="hero" className="min-h-screen flex items-center justify-center relative pt-20" style={{ display: 'flex', alignItems: 'center', minHeight: '100vh', justifyContent: 'center' }}>
      <div style={{ textAlign: 'center', zIndex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '2rem' }}>
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h2 style={{ fontSize: '1.5rem', color: 'var(--text-secondary)', marginBottom: '1rem' }}>
            {content.hero.greeting}
          </h2>
          <h1 style={{ fontSize: '4rem', lineHeight: 1.1, marginBottom: '1.5rem' }}>
            {content.hero.name} <br />
            <span className="heading-gradient">{content.hero.title}</span>
          </h1>
          
          <div style={{ fontSize: '2rem', height: '60px', fontWeight: 600 }}>
            <TypeAnimation
              key={typewriterKey}
              sequence={[
                content.hero.typewriter[0], 2000,
                content.hero.typewriter[1], 2000,
                content.hero.typewriter[2], 2000,
                content.hero.typewriter[3], 2000
              ]}
              wrapper="span"
              speed={50}
              repeat={Infinity}
              style={{ color: 'var(--accent-neon)' }}
            />
          </div>
          
          <p style={{ maxWidth: '600px', margin: '0 auto 2rem', color: 'var(--text-secondary)', fontSize: '1.1rem', lineHeight: 1.6 }}>
            {content.hero.desc}
          </p>

          <a href="#projects" style={{ textDecoration: 'none' }}>
            <button className="btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '10px', margin: '0 auto' }}>
              {content.hero.button} <ArrowRight size={20} />
            </button>
          </a>
        </motion.div>
      </div>
    </section>
  );
};

export default Hero;
