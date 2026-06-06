import React, { createContext, useState, useContext } from 'react';
import { CONTENT } from '../data/content';

const LanguageContext = createContext();

export const LanguageProvider = ({ children }) => {
  const [lang, setLang] = useState('ES');
  
  const toggleLanguage = () => {
    setLang(prevLang => prevLang === 'ES' ? 'EN' : 'ES');
  };

  const content = CONTENT[lang];

  return (
    <LanguageContext.Provider value={{ lang, toggleLanguage, content }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => useContext(LanguageContext);
