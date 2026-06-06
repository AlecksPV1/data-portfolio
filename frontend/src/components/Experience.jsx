import React from 'react';
import { motion } from 'framer-motion';
import { useLanguage } from '../context/LanguageContext';

const Experience = () => {
  const { content } = useLanguage();

  return (
    <section id="experience" style={{ maxWidth: '800px' }}>
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6 }}
      >
        <h2 className="section-title">
          {content.experience.title} <span className="heading-gradient">{content.experience.highlight}</span>
        </h2>
      </motion.div>

      <div style={{ position: 'relative', borderLeft: '2px solid var(--accent-cyan)', paddingLeft: '30px', marginLeft: '20px' }}>
        {content.experience.items.map((item, index) => (
          <motion.div 
            key={index}
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.5, delay: index * 0.2 }}
            className="glass glass-hover"
            style={{ marginBottom: '2rem', padding: '24px', position: 'relative' }}
          >
            <div style={{
              position: 'absolute',
              left: '-42px',
              top: '24px',
              width: '20px',
              height: '20px',
              borderRadius: '50%',
              background: 'var(--accent-cyan)',
              border: '4px solid var(--bg-color)',
              boxShadow: '0 0 10px var(--accent-cyan)'
            }}></div>
            
            <h3 style={{ fontSize: '1.5rem', marginBottom: '0.5rem', color: 'var(--text-primary)' }}>{item.role}</h3>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap' }}>
              {item.link ? (
                <a href={item.link} target="_blank" rel="noopener noreferrer" style={{ color: 'var(--accent-neon)', fontWeight: 'bold', fontSize: '1.1rem', textDecoration: 'none' }}>
                  {item.company} 🔗
                </a>
              ) : (
                <span style={{ color: 'var(--accent-neon)', fontWeight: 'bold', fontSize: '1.1rem' }}>{item.company}</span>
              )}
            </div>
            <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6 }}>{item.desc}</p>
          </motion.div>
        ))}
      </div>
    </section>
  );
};

export default Experience;
