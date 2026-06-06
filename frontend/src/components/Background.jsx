import React from 'react';
import { motion } from 'framer-motion';

const Background = () => {
  return (
    <div className="fixed inset-0 z-[-1] overflow-hidden bg-grid">
      {/* Animated Gradient Orbs */}
      <motion.div 
        className="absolute w-[500px] h-[500px] rounded-full blur-[100px] opacity-20"
        style={{ background: 'var(--accent-cyan)', top: '-10%', left: '-10%' }}
        animate={{
          x: [0, 50, 0],
          y: [0, 30, 0],
        }}
        transition={{ duration: 10, repeat: Infinity, ease: "easeInOut" }}
      />
      <motion.div 
        className="absolute w-[400px] h-[400px] rounded-full blur-[100px] opacity-20"
        style={{ background: 'var(--accent-neon)', bottom: '-10%', right: '-10%' }}
        animate={{
          x: [0, -40, 0],
          y: [0, -50, 0],
        }}
        transition={{ duration: 12, repeat: Infinity, ease: "easeInOut" }}
      />
    </div>
  );
};

export default Background;
