export const CONTENT = {
  ES: {
    nav: {
      home: "Inicio",
      skills: "Habilidades",
      experience: "Experiencia",
      projects: "Proyectos",
      contact: "Contacto",
      toggle: "🇺🇸 English"
    },
    hero: {
      greeting: "Hola, soy",
      name: "Alejandro Peña",
      title: "Ingeniero Mecatrónico",
      typewriter: [
        'Especialista en Automatización',
        'Machine Learning Engineer',
        'Integración de Hardware',
        'Data Scientist'
      ],
      desc: "Transformando datos complejos en decisiones claras y automatizando procesos mediante inteligencia artificial y control avanzado.",
      button: "Ver mis proyectos"
    },
    skills: {
      title: "Habilidades",
      highlight: "Técnicas",
      items: [
        "Machine Learning", "Data Science", "Redes Neuronales Convolucionales (CNN)", 
        "Integración de Hardware", "Raspberry Pi", "Linux", "Python", "Desarrollo de Sistemas",
        "Deep Learning", "TensorFlow", "Visión por Computadora", "Automatización"
      ]
    },
    experience: {
      title: "Trayectoria",
      highlight: "Profesional",
      items: [
        {
          company: "Unilever",
          role: "Ingeniero Mecatrónico / Especialista en Automatización",
          period: "2021 - Presente",
          desc: "Optimización y automatización de líneas de producción. Implementación de sistemas de control e IoT para monitoreo en tiempo real, mejorando la eficiencia operativa."
        },
        {
          company: "Proinsem",
          role: "Ingeniero de Proyectos",
          desc: "Diseño y despliegue de soluciones de integración de hardware. Desarrollo de algoritmos de control industrial y mantenimiento de sistemas electromecánicos.",
          link: "https://www.proinsem.com"
        },
        {
          company: "Estudios de Posgrado",
          role: "Maestría en Control Automático",
          desc: "Especialización enfocada en teoría de control avanzado, sistemas dinámicos y aplicación de algoritmos de inteligencia artificial como redes neuronales."
        }
      ]
    },
    projects: {
      title: "Proyectos",
      highlight: "Destacados",
      viewProject: "Ver Proyecto →",
      items: [
        {
          title: "Sistema de Predicción de Ventas Retail",
          tags: ["Streamlit", "Pandas", "Scikit-Learn"],
          desc: "Dashboard interactivo para optimizar stock prediciendo demanda futura con Random Forest.",
          link: "https://pandaspractica-ale.streamlit.app/"
        },
        {
          title: "Sistema de Fidelidad / Customer Loyalty System",
          tags: ["Django", "Python", "QR Codes"],
          desc: "Aplicación web completa con generación de QR, registro de visitas y dashboard administrativo. Diseño premium y adaptable para negocios.",
          link: "https://registro-fidelidad-x6u5.vercel.app/"
        },
        {
          title: "Solar Energy Prediction vs. Uncertainty",
          tags: ["Deep Learning", "Time Series", "Python"],
          desc: "Modelo predictivo de irradiación solar utilizando redes neuronales profundas para optimizar la reserva de potencia en redes eléctricas. El desafío principal fue la limpieza de series temporales meteorológicas ruidosas.",
          link: "#"
        },
        {
          title: "Cloudiness Recognition (Deep CNN)",
          tags: ["Computer Vision", "TensorFlow", "CNN"],
          desc: "Clasificador automático de nubosidad basado en imágenes satelitales. Implementé una arquitectura CNN personalizada que superó a los métodos tradicionales de umbralización en diversas condiciones de iluminación.",
          link: "https://jcyta.cenidet.tecnm.mx/revistas/jcyta/10-Vol_6_Num_1_Enero-Junio_2023.pdf"
        },
        {
          title: "Scalable Telemetry Pipeline",
          tags: ["IoT Data", "SQL", "Cloud"],
          desc: "Sistema ETL para datos de sensores remotos. Diseñé el esquema de base de datos SQL y las rutinas de carga en la nube, permitiendo monitorización en tiempo real y análisis histórico sin latencia.",
          link: "#"
        }
      ]
    },
    contact: {
      title: "Hablemos de",
      highlight: "Proyectos",
      subtitle: "¿Listo para potenciar tus datos? ¡Conectemos!",
      infoTitle: "Información de Contacto",
      location: "Cuernavaca, México",
      form: {
        name: "Nombre",
        email: "Correo Electrónico",
        message: "Mensaje",
        button: "Enviar Mensaje",
        sent: "Enviado"
      },
      footer: "© 2026 Alejandro Peña. Todos los derechos reservados."
    }
  },
  EN: {
    nav: {
      home: "Home",
      skills: "Skills",
      experience: "Experience",
      projects: "Projects",
      contact: "Contact",
      toggle: "🇪🇸 Español"
    },
    hero: {
      greeting: "Hi, I am",
      name: "Alejandro Peña",
      title: "Mechatronics Engineer",
      typewriter: [
        'Automation Specialist',
        'Machine Learning Engineer',
        'Hardware Integration',
        'Data Scientist'
      ],
      desc: "Transforming complex data into clear decisions and automating processes through artificial intelligence and advanced control.",
      button: "View my projects"
    },
    skills: {
      title: "Technical",
      highlight: "Skills",
      items: [
        "Machine Learning", "Data Science", "Convolutional Neural Networks (CNN)", 
        "Hardware Integration", "Raspberry Pi", "Linux", "Python", "Systems Development",
        "Deep Learning", "TensorFlow", "Computer Vision", "Automation"
      ]
    },
    experience: {
      title: "Professional",
      highlight: "Experience",
      items: [
        {
          company: "Unilever",
          role: "Mechatronics Engineer / Automation Specialist",
          period: "2021 - Present",
          desc: "Optimization and automation of production lines. Implementation of control systems and IoT for real-time monitoring, improving operational efficiency."
        },
        {
          company: "Proinsem",
          role: "Project Engineer",
          desc: "Design and deployment of hardware integration solutions. Development of industrial control algorithms and maintenance of electromechanical systems.",
          link: "https://www.proinsem.com"
        },
        {
          company: "Graduate Studies",
          role: "Master's Degree in Automatic Control",
          desc: "Specialization focused on advanced control theory, dynamical systems, and the application of artificial intelligence algorithms such as neural networks."
        }
      ]
    },
    projects: {
      title: "Featured",
      highlight: "Projects",
      viewProject: "View Project →",
      items: [
        {
          title: "Retail Sales Prediction System",
          tags: ["Streamlit", "Pandas", "Scikit-Learn"],
          desc: "Interactive dashboard for stock optimization, predicting future demand using Random Forest.",
          link: "https://pandaspractica-ale.streamlit.app/"
        },
        {
          title: "Loyalty System / Sistema de Fidelidad",
          tags: ["Django", "Python", "QR Codes"],
          desc: "Full-stack loyalty web app with QR generation, visit tracking, and admin dashboard. Premium design and business-ready.",
          link: "https://registro-fidelidad-x6u5.vercel.app/"
        },
        {
          title: "Solar Energy Prediction vs. Uncertainty",
          tags: ["Deep Learning", "Time Series", "Python"],
          desc: "Predictive model for solar irradiation using deep neural networks to optimize power reserve in electrical grids. Addressed the challenge of noisy meteorological time series data.",
          link: "#"
        },
        {
          title: "Cloudiness Recognition (Deep CNN)",
          tags: ["Computer Vision", "TensorFlow", "CNN"],
          desc: "Automated cloudiness classifier based on satellite images. Implemented a custom CNN architecture that outperformed traditional thresholding methods under various lighting conditions.",
          link: "https://jcyta.cenidet.tecnm.mx/revistas/jcyta/10-Vol_6_Num_1_Enero-Junio_2023.pdf"
        },
        {
          title: "Scalable Telemetry Pipeline",
          tags: ["IoT Data", "SQL", "Cloud"],
          desc: "ETL system for remote sensor data. Designed the SQL database schema and cloud loading routines, enabling real-time monitoring and historical analysis with zero latency.",
          link: "#"
        }
      ]
    },
    contact: {
      title: "Let's talk about",
      highlight: "Projects",
      subtitle: "Ready to leverage your data? Let's connect!",
      infoTitle: "Contact Information",
      location: "Cuernavaca, Mexico",
      form: {
        name: "Name",
        email: "Email Address",
        message: "Message",
        button: "Send Message",
        sent: "Sent"
      },
      footer: "© 2026 Alejandro Peña. All rights reserved."
    }
  }
};
