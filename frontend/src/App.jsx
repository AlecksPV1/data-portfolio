import React from 'react';
import Background from './components/Background';
import Hero from './components/Hero';
import Skills from './components/Skills';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Contact from './components/Contact';
import { useLanguage } from './context/LanguageContext';
import { Globe } from 'lucide-react';

function App() {
  const { content, toggleLanguage } = useLanguage();

  return (
    <>
      <Background />
      
      <nav style={{ position: 'fixed', top: 0, width: '100%', padding: '15px 40px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', zIndex: 100, backdropFilter: 'blur(10px)', background: 'rgba(15, 23, 42, 0.8)', borderBottom: '1px solid rgba(148, 163, 184, 0.1)' }}>
        <div style={{ fontWeight: 700, fontSize: '1.2rem', color: 'var(--accent-cyan)' }}>Alejandro.dev</div>
        
        <div style={{ display: 'flex', gap: '20px', alignItems: 'center' }}>
          <div style={{ display: 'flex', gap: '20px', display: 'none', '@media (minWidth: 768px)': { display: 'flex' } }} className="nav-links">
            <a href="#hero" style={{ color: 'var(--text-primary)', textDecoration: 'none', fontWeight: 500 }}>{content.nav.home}</a>
            <a href="#skills" style={{ color: 'var(--text-primary)', textDecoration: 'none', fontWeight: 500 }}>{content.nav.skills}</a>
            <a href="#experience" style={{ color: 'var(--text-primary)', textDecoration: 'none', fontWeight: 500 }}>{content.nav.experience}</a>
            <a href="#projects" style={{ color: 'var(--text-primary)', textDecoration: 'none', fontWeight: 500 }}>{content.nav.projects}</a>
            <a href="#contact" style={{ color: 'var(--text-primary)', textDecoration: 'none', fontWeight: 500 }}>{content.nav.contact}</a>
          </div>
          
          <button onClick={toggleLanguage} style={{
            background: 'rgba(255,255,255,0.1)', border: '1px solid var(--glass-border)', borderRadius: '20px',
            padding: '6px 14px', color: 'white', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px',
            transition: 'all 0.3s ease'
          }} className="lang-btn">
            <Globe size={16} />
            {content.nav.toggle}
          </button>
        </div>
      </nav>

      <main style={{ paddingTop: '60px' }}>
        <Hero />
        <Skills />
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <Experience />
        </div>
        <Projects />
        <Contact />
      </main>
      
      <footer style={{ textAlign: 'center', padding: '20px', color: 'var(--text-secondary)', borderTop: '1px solid var(--glass-border)' }}>
        <p>{content.contact.footer}</p>
      </footer>
    </>
  );
}

export default App;
