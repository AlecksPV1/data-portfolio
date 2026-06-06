import React from 'react';
import { motion } from 'framer-motion';
import { useLanguage } from '../context/LanguageContext';

const Skills = () => {
  const { content } = useLanguage();
  
  return (
    <section id="skills" style={{ overflow: 'hidden', padding: '100px 0' }}>
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6 }}
        style={{ textAlign: 'center', marginBottom: '3rem' }}
      >
        <h2 className="section-title">
          {content.skills.title} <span className="heading-gradient">{content.skills.highlight}</span>
        </h2>
      </motion.div>

      <div className="marquee-container" style={{ padding: '20px 0', background: 'rgba(30, 41, 59, 0.3)', borderTop: '1px solid rgba(148,163,184,0.1)', borderBottom: '1px solid rgba(148,163,184,0.1)' }}>
        <div className="marquee-content">
          {[...content.skills.items, ...content.skills.items, ...content.skills.items].map((skill, index) => (
            <div 
              key={index}
              style={{
                margin: '0 20px',
                padding: '12px 24px',
                background: 'linear-gradient(90deg, #1e293b, #334155)',
                borderRadius: '30px',
                border: '1px solid #475569',
                color: 'var(--accent-cyan)',
                fontSize: '1.1rem',
                fontWeight: '500',
                display: 'inline-flex',
                alignItems: 'center',
                boxShadow: '0 4px 6px rgba(0,0,0,0.2)'
              }}
            >
              {skill}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skills;
