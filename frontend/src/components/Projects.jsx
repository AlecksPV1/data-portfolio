import React from 'react';
import { motion } from 'framer-motion';
import { useLanguage } from '../context/LanguageContext';

const Projects = () => {
  const { content } = useLanguage();

  return (
    <section id="projects">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6 }}
        style={{ textAlign: 'center', marginBottom: '3rem' }}
      >
        <h2 className="section-title">
          {content.projects.title} <span className="heading-gradient">{content.projects.highlight}</span>
        </h2>
      </motion.div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>
        {content.projects.items.map((project, index) => (
          <motion.div 
            key={index}
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-50px" }}
            transition={{ duration: 0.5, delay: index * 0.2 }}
            className="glass glass-hover"
            style={{ overflow: 'hidden', display: 'flex', flexDirection: 'column' }}
          >
            {/* Card without image */}
            <div style={{ padding: '24px', flexGrow: 1, display: 'flex', flexDirection: 'column' }}>
              <h3 style={{ fontSize: '1.4rem', marginBottom: '1rem', color: 'var(--text-primary)' }}>{project.title}</h3>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '1rem' }}>
                {project.tags.map((tag, i) => (
                  <span key={i} style={{ 
                    fontSize: '0.8rem', 
                    padding: '4px 10px', 
                    background: 'rgba(6, 182, 212, 0.1)', 
                    color: 'var(--accent-cyan)', 
                    borderRadius: '20px',
                    border: '1px solid rgba(6, 182, 212, 0.2)'
                  }}>
                    {tag}
                  </span>
                ))}
              </div>
              <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, flexGrow: 1, marginBottom: '1.5rem' }}>{project.desc}</p>
              
              {project.link !== "#" && (
                <a href={project.link} target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', marginTop: 'auto' }}>
                  <span style={{ color: 'var(--accent-neon)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '5px' }}>
                    {content.projects.viewProject}
                  </span>
                </a>
              )}
            </div>
          </motion.div>
        ))}
      </div>
    </section>
  );
};

export default Projects;
