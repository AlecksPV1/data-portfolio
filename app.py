import streamlit as st
import requests
from streamlit_lottie import st_lottie

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alejandro Peña | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ASSETS & ANIMATIONS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Pre-load animations
lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json" # Data Science / Coding
lottie_contact = "https://assets3.lottiefiles.com/packages/lf20_v7ftxo.json" # Mail/Contact
lottie_analysis = "https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json" # Developer

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
                "title": "Solar Energy Prediction vs. Uncertainty",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Modelo predictivo de irradiación solar utilizando redes neuronales profundas para optimizar la reserva de potencia en redes eléctricas. El desafío principal fue la limpieza de series temporales meteorológicas ruidosas."
            },
            {
                "title": "Cloudiness Recognition (Deep CNN)",
                "tags": ["Computer Vision", "TensorFlow", "CNN"],
                "desc": "Clasificador automático de nubosidad basado en imágenes satelitales. Implementé una arquitectura CNN personalizada que superó a los métodos tradicionales de umbralización en diversas condiciones de iluminación."
            },
            {
                "title": "Scalable Telemetry Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud"],
                "desc": "Sistema ETL para datos de sensores remotos. Diseñé el esquema de base de datos SQL y las rutinas de carga en la nube, permitiendo monitorización en tiempo real y análisis histórico sin latencia."
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
                "title": "Solar Energy Prediction vs. Uncertainty",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Predictive model for solar irradiation using deep neural networks to optimize power reserve in electrical grids. Addressed the challenge of noisy meteorological time series data."
            },
            {
                "title": "Cloudiness Recognition (Deep CNN)",
                "tags": ["Computer Vision", "TensorFlow", "CNN"],
                "desc": "Automated cloudiness classifier based on satellite images. Implemented a custom CNN architecture that outperformed traditional thresholding methods under various lighting conditions."
            },
            {
                "title": "Scalable Telemetry Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud"],
                "desc": "ETL system for remote sensor data. Designed the SQL database schema and cloud loading routines, enabling real-time monitoring and historical analysis with zero latency."
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
        .skill-badge:hover {
            background: #3b82f6;
            color: white;
            border-color: #3b82f6;
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
        # Lottie Animation
        lottie_json = load_lottieurl(lottie_coding)
        if lottie_json:
            st_lottie(lottie_json, height=300, key="coding")
        else:
            st.image("https://source.unsplash.com/random/400x400?data,tech", use_column_width=True)

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
        # If we have multiple projects, maybe 2 per row? For now, stacked cards look good.
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
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
        lottie_mail = load_lottieurl(lottie_contact)
        if lottie_mail:
            st_lottie(lottie_mail, height=200, key="contact")

if __name__ == "__main__":
    main()
