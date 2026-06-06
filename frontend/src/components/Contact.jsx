import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Mail, CheckCircle } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';

const GithubIcon = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
    <path d="M9 18c-4.51 2-5-2-7-2"/>
  </svg>
);

const LinkedinIcon = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
    <rect width="4" height="12" x="2" y="9"/>
    <circle cx="4" cy="4" r="2"/>
  </svg>
);

const Contact = () => {
  const [submitted, setSubmitted] = useState(false);
  const { content } = useLanguage();

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => setSubmitted(false), 3000);
  };

  return (
    <section id="contact" style={{ paddingBottom: '100px' }}>
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6 }}
        style={{ textAlign: 'center', marginBottom: '3rem' }}
      >
        <h2 className="section-title">
          {content.contact.title} <span className="heading-gradient">{content.contact.highlight}</span>
        </h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem' }}>{content.contact.subtitle}</p>
      </motion.div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '3rem', alignItems: 'center' }}>
        
        {/* Contact Info & Socials */}
        <motion.div
          initial={{ opacity: 0, x: -50 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}
        >
          <div className="glass" style={{ padding: '2rem' }}>
            <h3 style={{ fontSize: '1.5rem', marginBottom: '1rem', color: 'var(--accent-cyan)' }}>{content.contact.infoTitle}</h3>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <Mail size={18} /> alejandropav27@gmail.com
            </p>
            <p style={{ color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '10px' }}>
              📍 {content.contact.location}
            </p>
          </div>

          <div style={{ display: 'flex', gap: '1rem' }}>
            <motion.a whileHover={{ y: -5, scale: 1.1 }} href="#" className="glass" style={{ padding: '15px', color: 'var(--text-primary)', display: 'inline-block' }}>
              <GithubIcon size={24} />
            </motion.a>
            <motion.a whileHover={{ y: -5, scale: 1.1 }} href="#" className="glass" style={{ padding: '15px', color: '#0077b5', display: 'inline-block' }}>
              <LinkedinIcon size={24} />
            </motion.a>
          </div>
        </motion.div>

        {/* Contact Form */}
        <motion.div
          initial={{ opacity: 0, x: 50 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <form onSubmit={handleSubmit} className="glass" style={{ padding: '2.5rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>{content.contact.form.name}</label>
              <input type="text" required style={{ width: '100%', padding: '12px', borderRadius: '8px', border: '1px solid var(--glass-border)', background: 'rgba(15, 23, 42, 0.5)', color: 'white', outline: 'none' }} />
            </div>
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>{content.contact.form.email}</label>
              <input type="email" required style={{ width: '100%', padding: '12px', borderRadius: '8px', border: '1px solid var(--glass-border)', background: 'rgba(15, 23, 42, 0.5)', color: 'white', outline: 'none' }} />
            </div>
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>{content.contact.form.message}</label>
              <textarea rows="4" required style={{ width: '100%', padding: '12px', borderRadius: '8px', border: '1px solid var(--glass-border)', background: 'rgba(15, 23, 42, 0.5)', color: 'white', outline: 'none', resize: 'vertical' }}></textarea>
            </div>
            
            <button type="submit" className="btn-primary" style={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '10px' }}>
              {submitted ? <><CheckCircle size={20}/> {content.contact.form.sent}</> : content.contact.form.button}
            </button>
          </form>
        </motion.div>

      </div>
    </section>
  );
};

export default Contact;
