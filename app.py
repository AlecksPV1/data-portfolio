<<<<<<< HEAD
import streamlit as st
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alejandro Peña | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ASSETS & ANIMATIONS ---
# --- ASSETS ---
# No external assets needed, using CSS animations

# --- BILINGUAL CONTENT DICTIONARY ---
CONTENT = {
    "ES": {
        "role": "Data Analyst / Machine Learning Engineer",
        "bio_title": "Sobre Mí",
        "bio": """
        **Ingeniero Mecatrónico** transformado en **Data Scientist**.
        
        Mi pasión reside en encontrar la señal en medio del ruido. Con una Maestría en Control y especialización en Redes Neuronales, combino la rigurosidad matemática con herramientas modernas de Data Science para resolver problemas reales.
        
        <br>
        
        🔹 **Enfoque:** Modelos Predictivos, Deep Learning & Automatización.
        🔹 **Misión:** Transformar datos complejos en decisiones de negocio claras.
        """,
        "skills_title": "Habilidades Técnicas",
        "projects_title": "Portafolio de Proyectos",
        "contact_title": "Contacto",
        "download_cv": "Descargar CV",
        "nav": {
            "about": "Perfil",
            "skills": "Habilidades",
            "projects": "Proyectos",
            "contact": "Contacto"
        },
        "skills_cats": {
            "lang": "Lenguajes & Core",
            "ds": "Data Science & ML",
            "tools": "Herramientas & Cloud"
        },
        "projects": [
            {
                "title": "Sistema de Predicción de Ventas Retail",
                "tags": ["Streamlit", "Pandas", "Scikit-Learn"],
                "desc": "Dashboard interactivo para optimizar stock prediciendo demanda futura con Random Forest.",
                "link": "https://pandaspractica-ale.streamlit.app/"
            },
            {
                "title": "Sistema de Fidelidad / Customer Loyalty System",
                "tags": ["Django", "Python", "QR Codes"],
                "desc": "Aplicación web completa con generación de QR, registro de visitas y dashboard administrativo. Diseño premium y adaptable para negocios.",
                "link": "https://registro-fidelidad-x6u5.vercel.app/"
            },
            {
                "title": "Solar Energy Prediction vs. Uncertainty",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Modelo predictivo de irradiación solar utilizando redes neuronales profundas para optimizar la reserva de potencia en redes eléctricas. El desafío principal fue la limpieza de series temporales meteorológicas ruidosas.",
                "link": None
            },
            {
                "title": "Cloudiness Recognition (Deep CNN)",
                "tags": ["Computer Vision", "TensorFlow", "CNN"],
                "desc": "Clasificador automático de nubosidad basado en imágenes satelitales. Implementé una arquitectura CNN personalizada que superó a los métodos tradicionales de umbralización en diversas condiciones de iluminación.",
                "link": "https://jcyta.cenidet.tecnm.mx/revistas/jcyta/10-Vol_6_Num_1_Enero-Junio_2023.pdf"
            },
            {
                "title": "Scalable Telemetry Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud"],
                "desc": "Sistema ETL para datos de sensores remotos. Diseñé el esquema de base de datos SQL y las rutinas de carga en la nube, permitiendo monitorización en tiempo real y análisis histórico sin latencia.",
                "link": None
            }
        ],
        "contact_info": {
            "location": "Cuernavaca, México",
            "email": "alejandropav27@gmail.com",
            "cta": "¿Listo para potenciar tus datos? ¡Conectemos!"
        }
    },
    "EN": {
        "role": "Data Analyst / Machine Learning Engineer",
        "bio_title": "About Me",
        "bio": """
        **Mechatronics Engineer** turned **Data Scientist**.
        
        My passion lies in finding the signal amidst the noise. With an MSc in Control and specialization in Neural Networks, I combine mathematical rigor with modern Data Science tools to solve real-world problems.
        
        <br>
        
        🔹 **Focus:** Predictive Modeling, Deep Learning & Automation.
        🔹 **Mission:** Transform complex data into clear business decisions.
        """,
        "skills_title": "Technical Skills",
        "projects_title": "Project Portfolio",
        "contact_title": "Contact",
        "download_cv": "Download CV",
        "nav": {
            "about": "Profile",
            "skills": "Skills",
            "projects": "Projects",
            "contact": "Contact"
        },
        "skills_cats": {
            "lang": "Languages & Core",
            "ds": "Data Science & ML",
            "tools": "Tools & Cloud"
        },
        "projects": [
            {
                "title": "Retail Sales Prediction System",
                "tags": ["Streamlit", "Pandas", "Scikit-Learn"],
                "desc": "Interactive dashboard for stock optimization, predicting future demand using Random Forest.",
                "link": "https://pandaspractica-ale.streamlit.app/"
            },
            {
                "title": "Loyalty System / Sistema de Fidelidad",
                "tags": ["Django", "Python", "QR Codes"],
                "desc": "Full-stack loyalty web app with QR generation, visit tracking, and admin dashboard. Premium design and business-ready.",
                "link": "https://registro-fidelidad-x6u5.vercel.app/"
            },
            {
                "title": "Solar Energy Prediction vs. Uncertainty",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Predictive model for solar irradiation using deep neural networks to optimize power reserve in electrical grids. Addressed the challenge of noisy meteorological time series data.",
                "link": None
            },
            {
                "title": "Cloudiness Recognition (Deep CNN)",
                "tags": ["Computer Vision", "TensorFlow", "CNN"],
                "desc": "Automated cloudiness classifier based on satellite images. Implemented a custom CNN architecture that outperformed traditional thresholding methods under various lighting conditions.",
                "link": "https://jcyta.cenidet.tecnm.mx/revistas/jcyta/10-Vol_6_Num_1_Enero-Junio_2023.pdf"
            },
            {
                "title": "Scalable Telemetry Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud"],
                "desc": "ETL system for remote sensor data. Designed the SQL database schema and cloud loading routines, enabling real-time monitoring and historical analysis with zero latency.",
                "link": None
            }
        ],
        "contact_info": {
            "location": "Cuernavaca, Mexico",
            "email": "alejandropav27@gmail.com",
            "cta": "Ready to leverage your data? Let's connect!"
        }
    }
}

# --- CUSTOM CSS ---
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        /* Modern Dark & Gradient Theme */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #FAFAFA;
        }
        
        /* Typography */
        h1, h2, h3 {
            font-weight: 700;
        }
        h1 {
            background: -webkit-linear-gradient(45deg, #3b82f6, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Cards */
        .project-card {
            background-color: rgba(30, 41, 59, 0.7);
            padding: 25px;
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.1);
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .project-card:hover {
            transform: translateY(-5px);
            border-color: #3b82f6;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.2);
        }
        
        /* Skills Badges */
        .skill-badge {
            display: inline-block;
            padding: 6px 12px;
            margin: 4px;
            background: linear-gradient(90deg, #1e293b, #334155);
            border-radius: 20px;
            font-size: 0.85em;
            color: #60a5fa;
            border: 1px solid #475569;
            transition: 0.2s;
        }
        /* Animated Gradient Orb */
        @keyframes float {
            0% { transform: translate(0px, 0px) scale(1); }
            33% { transform: translate(30px, -50px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
            100% { transform: translate(0px, 0px) scale(1); }
        }

        .hero-animation {
            width: 300px;
            height: 300px;
            background: linear-gradient(45deg, #3b82f6, #06b6d4, #8b5cf6);
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.6;
            animation: float 10s ease-in-out infinite;
            margin: auto;
        }

        .skill-badge:hover {
            background: #3b82f6;
            color: white;
            border-color: #3b82f6;
        }

        a.project-link {
            text-decoration: none;
            color: #FAFAFA;
        }
        a.project-link:hover h3 {
             color: #3b82f6;
             transition: color 0.3s ease;
        }
        </style>
    """, unsafe_allow_html=True)

# --- MAIN APP ---
def main():
    local_css()

    # Sidebar
    with st.sidebar:
        st.header("Alejandro Peña")
        # Language Switcher
        st.divider()
        lang_choice = st.radio("Language / Idioma", options=["Español", "English"], horizontal=True)
        lang = "ES" if lang_choice == "Español" else "EN"
        data = CONTENT[lang]
        
        st.divider()
        st.write(f"📍 {data['contact_info']['location']}")
        st.write(f"📧 {data['contact_info']['email']}")
    
    # Hero Section
    col_hero_text, col_hero_img = st.columns([1.5, 1])
    with col_hero_text:
        st.title("Alejandro Peña Vargas")
        st.subheader(data['role'])
        st.markdown("---")
        st.markdown(data['bio'], unsafe_allow_html=True)
        
    with col_hero_img:
        # CSS Animation
        st.markdown('<div class="hero-animation"></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Skills Section
    st.header(data['skills_title'])
    
    sk_c1, sk_c2, sk_c3 = st.columns(3)
    with sk_c1:
        st.markdown(f"**{data['skills_cats']['lang']}**")
        st.markdown("""
        <div style="margin-top:10px;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">SQL</span>
            <span class="skill-badge">MATLAB</span>
        </div>
        """, unsafe_allow_html=True)

    with sk_c2:
        st.markdown(f"**{data['skills_cats']['ds']}**")
        st.markdown("""
        <div style="margin-top:10px;">
            <span class="skill-badge">Machine Learning</span>
            <span class="skill-badge">Deep Learning</span>
            <span class="skill-badge">Computer Vision</span>
            <span class="skill-badge">NLP</span>
        </div>
        """, unsafe_allow_html=True)

    with sk_c3:
        st.markdown(f"**{data['skills_cats']['tools']}**")
        st.markdown("""
        <div style="margin-top:10px;">
            <span class="skill-badge">Git</span>
            <span class="skill-badge">AWS/GCP</span>
            <span class="skill-badge">Docker</span>
            <span class="skill-badge">Streamlit</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Projects Section
    st.header(data['projects_title'])
    
    # Using columns for grid layout
    for i, project in enumerate(data['projects']):
        title_html = f"<h3>{project['title']}</h3>"
        if project['link']:
            title_html = f"<a href='{project['link']}' target='_blank' class='project-link'><h3>{project['title']} 🔗</h3></a>"
        
        st.markdown(f"""
        <div class="project-card">
            {title_html}
            <p style="color:#94a3b8; font-size:0.9em;">{' • '.join(project['tags'])}</p>
            <p>{project['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Contact Section
    st.header(data['contact_title'])
    
    c_col1, c_col2 = st.columns([1, 1])
    with c_col1:
        st.markdown(f"### {data['contact_info']['cta']}")
        st.markdown(f"""
        <div style="background:#1e293b; padding:20px; border-radius:10px; border:1px solid #334155;">
            <p style="font-size:1.2em;">📧 <b>{data['contact_info']['email']}</b></p>
            <p>📍 {data['contact_info']['location']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c_col2:

        # Simple CSS geometric shape for contact
        st.markdown("""
        <div style="
            width: 150px; 
            height: 150px; 
            margin: auto; 
            border: 2px solid #3b82f6; 
            border-radius: 50%; 
            display: flex; 
            align-items: center; 
            justify_content: center;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
        ">
            <span style="font-size: 3em;">✉️</span>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
=======
import streamlit as st
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alejandro Peña | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ASSETS & ANIMATIONS ---
# --- ASSETS ---
# No external assets needed, using CSS animations

# --- BILINGUAL CONTENT DICTIONARY ---
CONTENT = {
    "ES": {
        "role": "Data Analyst / Machine Learning Engineer",
        "bio_title": "Sobre Mí",
        "bio": """
        **Ingeniero Mecatrónico** transformado en **Data Scientist**.
        
        Mi pasión reside en encontrar la señal en medio del ruido. Con una Maestría en Control y especialización en Redes Neuronales, combino la rigurosidad matemática con herramientas modernas de Data Science para resolver problemas reales.
        
        <br>
        
        🔹 **Enfoque:** Modelos Predictivos, Deep Learning & Automatización.
        🔹 **Misión:** Transformar datos complejos en decisiones de negocio claras.
        """,
        "skills_title": "Habilidades Técnicas",
        "projects_title": "Portafolio de Proyectos",
        "contact_title": "Contacto",
        "download_cv": "Descargar CV",
        "nav": {
            "about": "Perfil",
            "skills": "Habilidades",
            "projects": "Proyectos",
            "contact": "Contacto"
        },
        "skills_cats": {
            "lang": "Lenguajes & Core",
            "ds": "Data Science & ML",
            "tools": "Herramientas & Cloud"
        },
        "projects": [
            {
                "title": "Sistema de Predicción de Ventas Retail",
                "tags": ["Streamlit", "Pandas", "Scikit-Learn"],
                "desc": "Dashboard interactivo para optimizar stock prediciendo demanda futura con Random Forest.",
                "link": "https://pandaspractica-ale.streamlit.app/"
            },
            {
                "title": "Sistema de Fidelidad / Customer Loyalty System",
                "tags": ["Django", "Python", "QR Codes"],
                "desc": "Aplicación web completa con generación de QR, registro de visitas y dashboard administrativo. Diseño premium y adaptable para negocios.",
                "link": "https://registro-fidelidad-x6u5.vercel.app/"
            },
            {
                "title": "Solar Energy Prediction vs. Uncertainty",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Modelo predictivo de irradiación solar utilizando redes neuronales profundas para optimizar la reserva de potencia en redes eléctricas. El desafío principal fue la limpieza de series temporales meteorológicas ruidosas.",
                "link": None
            },
            {
                "title": "Cloudiness Recognition (Deep CNN)",
                "tags": ["Computer Vision", "TensorFlow", "CNN"],
                "desc": "Clasificador automático de nubosidad basado en imágenes satelitales. Implementé una arquitectura CNN personalizada que superó a los métodos tradicionales de umbralización en diversas condiciones de iluminación.",
                "link": "https://jcyta.cenidet.tecnm.mx/revistas/jcyta/10-Vol_6_Num_1_Enero-Junio_2023.pdf"
            },
            {
                "title": "Scalable Telemetry Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud"],
                "desc": "Sistema ETL para datos de sensores remotos. Diseñé el esquema de base de datos SQL y las rutinas de carga en la nube, permitiendo monitorización en tiempo real y análisis histórico sin latencia.",
                "link": None
            }
        ],
        "contact_info": {
            "location": "Cuernavaca, México",
            "email": "alejandropav27@gmail.com",
            "cta": "¿Listo para potenciar tus datos? ¡Conectemos!"
        }
    },
    "EN": {
        "role": "Data Analyst / Machine Learning Engineer",
        "bio_title": "About Me",
        "bio": """
        **Mechatronics Engineer** turned **Data Scientist**.
        
        My passion lies in finding the signal amidst the noise. With an MSc in Control and specialization in Neural Networks, I combine mathematical rigor with modern Data Science tools to solve real-world problems.
        
        <br>
        
        🔹 **Focus:** Predictive Modeling, Deep Learning & Automation.
        🔹 **Mission:** Transform complex data into clear business decisions.
        """,
        "skills_title": "Technical Skills",
        "projects_title": "Project Portfolio",
        "contact_title": "Contact",
        "download_cv": "Download CV",
        "nav": {
            "about": "Profile",
            "skills": "Skills",
            "projects": "Projects",
            "contact": "Contact"
        },
        "skills_cats": {
            "lang": "Languages & Core",
            "ds": "Data Science & ML",
            "tools": "Tools & Cloud"
        },
        "projects": [
            {
                "title": "Retail Sales Prediction System",
                "tags": ["Streamlit", "Pandas", "Scikit-Learn"],
                "desc": "Interactive dashboard for stock optimization, predicting future demand using Random Forest.",
                "link": "https://pandaspractica-ale.streamlit.app/"
            },
            {
                "title": "Loyalty System / Sistema de Fidelidad",
                "tags": ["Django", "Python", "QR Codes"],
                "desc": "Full-stack loyalty web app with QR generation, visit tracking, and admin dashboard. Premium design and business-ready.",
                "link": "https://registro-fidelidad-x6u5.vercel.app/"
            },
            {
                "title": "Solar Energy Prediction vs. Uncertainty",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Predictive model for solar irradiation using deep neural networks to optimize power reserve in electrical grids. Addressed the challenge of noisy meteorological time series data.",
                "link": None
            },
            {
                "title": "Cloudiness Recognition (Deep CNN)",
                "tags": ["Computer Vision", "TensorFlow", "CNN"],
                "desc": "Automated cloudiness classifier based on satellite images. Implemented a custom CNN architecture that outperformed traditional thresholding methods under various lighting conditions.",
                "link": "https://jcyta.cenidet.tecnm.mx/revistas/jcyta/10-Vol_6_Num_1_Enero-Junio_2023.pdf"
            },
            {
                "title": "Scalable Telemetry Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud"],
                "desc": "ETL system for remote sensor data. Designed the SQL database schema and cloud loading routines, enabling real-time monitoring and historical analysis with zero latency.",
                "link": None
            }
        ],
        "contact_info": {
            "location": "Cuernavaca, Mexico",
            "email": "alejandropav27@gmail.com",
            "cta": "Ready to leverage your data? Let's connect!"
        }
    }
}

# --- CUSTOM CSS ---
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        /* Modern Dark & Gradient Theme */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #FAFAFA;
        }
        
        /* Typography */
        h1, h2, h3 {
            font-weight: 700;
        }
        h1 {
            background: -webkit-linear-gradient(45deg, #3b82f6, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Cards */
        .project-card {
            background-color: rgba(30, 41, 59, 0.7);
            padding: 25px;
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.1);
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .project-card:hover {
            transform: translateY(-5px);
            border-color: #3b82f6;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.2);
        }
        
        /* Skills Badges */
        .skill-badge {
            display: inline-block;
            padding: 6px 12px;
            margin: 4px;
            background: linear-gradient(90deg, #1e293b, #334155);
            border-radius: 20px;
            font-size: 0.85em;
            color: #60a5fa;
            border: 1px solid #475569;
            transition: 0.2s;
        }
        /* Animated Gradient Orb */
        @keyframes float {
            0% { transform: translate(0px, 0px) scale(1); }
            33% { transform: translate(30px, -50px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
            100% { transform: translate(0px, 0px) scale(1); }
        }

        .hero-animation {
            width: 300px;
            height: 300px;
            background: linear-gradient(45deg, #3b82f6, #06b6d4, #8b5cf6);
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.6;
            animation: float 10s ease-in-out infinite;
            margin: auto;
        }

        .skill-badge:hover {
            background: #3b82f6;
            color: white;
            border-color: #3b82f6;
        }

        a.project-link {
            text-decoration: none;
            color: #FAFAFA;
        }
        a.project-link:hover h3 {
             color: #3b82f6;
             transition: color 0.3s ease;
        }
        </style>
    """, unsafe_allow_html=True)

# --- MAIN APP ---
def main():
    local_css()

    # Sidebar
    with st.sidebar:
        st.header("Alejandro Peña")
        # Language Switcher
        st.divider()
        lang_choice = st.radio("Language / Idioma", options=["Español", "English"], horizontal=True)
        lang = "ES" if lang_choice == "Español" else "EN"
        data = CONTENT[lang]
        
        st.divider()
        st.write(f"📍 {data['contact_info']['location']}")
        st.write(f"📧 {data['contact_info']['email']}")
    
    # Hero Section
    col_hero_text, col_hero_img = st.columns([1.5, 1])
    with col_hero_text:
        st.title("Alejandro Peña Vargas")
        st.subheader(data['role'])
        st.markdown("---")
        st.markdown(data['bio'], unsafe_allow_html=True)
        
    with col_hero_img:
        # CSS Animation
        st.markdown('<div class="hero-animation"></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Skills Section
    st.header(data['skills_title'])
    
    sk_c1, sk_c2, sk_c3 = st.columns(3)
    with sk_c1:
        st.markdown(f"**{data['skills_cats']['lang']}**")
        st.markdown("""
        <div style="margin-top:10px;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">SQL</span>
            <span class="skill-badge">MATLAB</span>
        </div>
        """, unsafe_allow_html=True)

    with sk_c2:
        st.markdown(f"**{data['skills_cats']['ds']}**")
        st.markdown("""
        <div style="margin-top:10px;">
            <span class="skill-badge">Machine Learning</span>
            <span class="skill-badge">Deep Learning</span>
            <span class="skill-badge">Computer Vision</span>
            <span class="skill-badge">NLP</span>
        </div>
        """, unsafe_allow_html=True)

    with sk_c3:
        st.markdown(f"**{data['skills_cats']['tools']}**")
        st.markdown("""
        <div style="margin-top:10px;">
            <span class="skill-badge">Git</span>
            <span class="skill-badge">AWS/GCP</span>
            <span class="skill-badge">Docker</span>
            <span class="skill-badge">Streamlit</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Projects Section
    st.header(data['projects_title'])
    
    # Using columns for grid layout
    for i, project in enumerate(data['projects']):
        title_html = f"<h3>{project['title']}</h3>"
        if project['link']:
            title_html = f"<a href='{project['link']}' target='_blank' class='project-link'><h3>{project['title']} 🔗</h3></a>"
        
        st.markdown(f"""
        <div class="project-card">
            {title_html}
            <p style="color:#94a3b8; font-size:0.9em;">{' • '.join(project['tags'])}</p>
            <p>{project['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Contact Section
    st.header(data['contact_title'])
    
    c_col1, c_col2 = st.columns([1, 1])
    with c_col1:
        st.markdown(f"### {data['contact_info']['cta']}")
        st.markdown(f"""
        <div style="background:#1e293b; padding:20px; border-radius:10px; border:1px solid #334155;">
            <p style="font-size:1.2em;">📧 <b>{data['contact_info']['email']}</b></p>
            <p>📍 {data['contact_info']['location']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c_col2:

        # Simple CSS geometric shape for contact
        st.markdown("""
        <div style="
            width: 150px; 
            height: 150px; 
            margin: auto; 
            border: 2px solid #3b82f6; 
            border-radius: 50%; 
            display: flex; 
            align-items: center; 
            justify_content: center;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
        ">
            <span style="font-size: 3em;">✉️</span>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
>>>>>>> 7ae78c02fadb77a9cc247b8d91f213bc1d902d76
