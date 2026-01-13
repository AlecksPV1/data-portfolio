import streamlit as st
import PIL.Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alejandro Peña | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- BILINGUAL CONTENT DICTIONARY ---
CONTENT = {
    "ES": {
        "role": "Data Analyst / Machine Learning Engineer",
        "bio_title": "Sobre Mí",
        "bio": """
        Maestro en Electrónica de Control con una sólida base matemática y especialización en Redes Neuronales.
        
        Transicioné de la Ingeniería Mecatrónica al mundo de los Datos impulsado por mi pasión por descubrir patrones ocultos y optimizar procesos. 
        Mi enfoque actual combina la **algoritmia avanzada** y el **modelado predictivo** para resolver problemas complejos de negocio y científicos.
        
        Busco aportar valor transformando datos crudos en estrategias accionables mediante Deep Learning y Análisis Estadístico.
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
                "title": "Solar Energy Prediction Model & Tesis",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Este proyecto aborda la incertidumbre en la generación de energía renovable. Desarrollé técnicas de **Deep Learning** para el análisis de series temporales, logrando predecir la irradiación solar con alta precisión para optimizar la reserva de potencia en la red eléctrica. Se priorizó la limpieza de datos meteorológicos y la selección de características (Feature Engineering) para mejorar la robustez del modelo."
            },
            {
                "title": "Cloudiness Image Recognition (CNN)",
                "tags": ["Computer Vision", "TensorFlow/PyTorch", "CNN"],
                "desc": "Implementación de una **Red Neuronal Convolucional (CNN)** de arquitectura profunda para la clasificación y segmentación automatizada de nubosidad en imágenes satelitales. El proyecto demostró la capacidad de procesar datos no estructurados (imágenes) y extraer patrones visuales complejos para aplicaciones meteorológicas."
            },
            {
                "title": "Cloud-Based Telemetry Data Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud Pipelines"],
                "desc": "Diseño de un sistema escalable para la ingestión y almacenamiento de datos masivos provenientes de sensores remotos. Me enfoqué en la arquitectura de datos, diseñando consultas **SQL** eficientes y pipelines de carga en la nube para asegurar la integridad y disponibilidad de los datos para su posterior análisis."
            }
        ],
        "contact_info": {
            "location": "Ubicación: Cuernavaca, México",
            "email": "Email: alejandropav27@gmail.com",
            "cta": "¿Tienes un proyecto de datos o una vacante? ¡Hablemos!"
        }
    },
    "EN": {
        "role": "Data Analyst / Machine Learning Engineer",
        "bio_title": "About Me",
        "bio": """
        MSc in Control Electronics with a strong mathematical foundation and specialization in Neural Networks.
        
        I transitioned from Mechatronics Engineering to Data Science driven by my passion for uncovering hidden patterns and optimizing processes.
        My current focus combines **advanced algorithmics** and **predictive modeling** to solve complex business and scientific problems.
        
        I aim to deliver value by transforming raw data into actionable strategies through Deep Learning and Statistical Analysis.
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
                "title": "Solar Energy Prediction Model & Thesis",
                "tags": ["Deep Learning", "Time Series", "Python"],
                "desc": "Addressed uncertainty in renewable energy generation. I developed **Deep Learning** techniques for time series analysis, achieving high-precision solar irradiation prediction to optimize power reserve. Enhanced model robustness through rigorous meteorological data cleaning and Feature Engineering."
            },
            {
                "title": "Cloudiness Image Recognition (CNN)",
                "tags": ["Computer Vision", "TensorFlow/PyTorch", "CNN"],
                "desc": "Implemented a deep **Convolutional Neural Network (CNN)** for automated classification and segmentation of cloudiness in satellite images. Demonstrated the capability to process unstructured data (images) and extract complex visual patterns for meteorological applications."
            },
            {
                "title": "Cloud-Based Telemetry Data Pipeline",
                "tags": ["IoT Data", "SQL", "Cloud Pipelines"],
                "desc": "Designed a scalable system for ingesting and storing massive data from remote sensors. Focused on data architecture, designing efficient **SQL** queries and cloud loading pipelines to ensure data integrity and availability for downstream analysis."
            }
        ],
        "contact_info": {
            "location": "Location: Cuernavaca, Mexico",
            "email": "Email: alejandropav27@gmail.com",
            "cta": "Have a data project or opening? Let's talk!"
        }
    }
}

# --- CUSTOM CSS ---
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        
        /* Minimalist Dark Theme Adjustments */
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #E0E0E0;
            font-weight: 600;
        }
        
        h1 {
            font-size: 3rem;
            background: -webkit-linear-gradient(45deg, #007CF0, #00DFD8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Card-like styling for projects */
        .project-card {
            background-color: #161B22;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #30363D;
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        .project-card:hover {
            transform: scale(1.01);
            border-color: #007CF0;
        }
        
        /* Sidebar adjustments */
        section[data-testid="stSidebar"] {
            background-color: #161B22;
        }
        
        /* Skills badges */
        .skill-badge {
            display: inline-block;
            padding: 5px 10px;
            margin: 3px;
            background-color: #21262D;
            border-radius: 15px;
            font-size: 0.9em;
            color: #58A6FF;
            border: 1px solid #30363D;
        }
        </style>
    """, unsafe_allow_html=True)

# --- MAIN APP ---
def main():
    local_css()

    # --- SIDEBAR ---
    with st.sidebar:
        # Placeholder for profile image, looking professional
        # st.image("path/to/profile.png", width=150) # Uncomment if image provided
        st.markdown(f"## Alejandro Peña Vargas")
        
        # Language Selector
        lang_choice = st.radio("Language / Idioma", options=["Español", "English"], horizontal=True)
        lang = "ES" if lang_choice == "Español" else "EN"
        
        data = CONTENT[lang]
        
        st.markdown("---")
        
        # Navigation
        st.write(f"**{data['nav']['contact']}**")
        st.info("alejandropav27@gmail.com")
        st.caption(data['contact_info']['location'])
        
        st.markdown("---")
        # Could add a CV download button here if file exists
        # with open("cv.pdf", "rb") as file:
        #     st.download_button(label=data['download_cv'], data=file, file_name="Alejandro_Pena_CV.pdf")

    # --- HERO SECTION ---
    st.title("Alejandro Peña Vargas")
    st.markdown(f"### {data['role']}")
    st.markdown("---")

    # --- ABOUT ME ---
    st.header(data['bio_title'])
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(data['bio'])
    with col2:
        # Highlighting Key Competencies visually
        st.metric(label="Degree", value="MSc Control Electronics")
        st.metric(label="Focus", value="Data & ML")

    st.markdown("---")

    # --- SKILLS ---
    st.header(data['skills_title'])
    
    sk_c1, sk_c2, sk_c3 = st.columns(3)
    
    with sk_c1:
        st.subheader(data['skills_cats']['lang'])
        st.markdown("""
        - <span class="skill-badge">Python (Numpy, Pandas, Scikit-learn)</span>
        - <span class="skill-badge">SQL</span>
        - <span class="skill-badge">MATLAB</span>
        """, unsafe_allow_html=True)
        
    with sk_c2:
        st.subheader(data['skills_cats']['ds'])
        st.markdown("""
        - <span class="skill-badge">Machine Learning</span>
        - <span class="skill-badge">Deep Learning</span>
        - <span class="skill-badge">Computer Vision</span>
        - <span class="skill-badge">Data Visualization</span>
        """, unsafe_allow_html=True)
        
    with sk_c3:
        st.subheader(data['skills_cats']['tools'])
        st.markdown("""
        - <span class="skill-badge">Git & GitHub</span>
        - <span class="skill-badge">Cloud Services</span>
        - <span class="skill-badge">LaTeX</span>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- PROJECTS ---
    st.header(data['projects_title'])
    
    for project in data['projects']:
        # Creating a visually distinct container for each project
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p><i>Stack: {', '.join(project['tags'])}</i></p>
            <p>{project['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- CONTACT ---
    st.header(data['contact_title'])
    st.markdown(f"#### {data['contact_info']['cta']}")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"📧 **Email:** alejandropav27@gmail.com")
    with c2:
        st.markdown(f"📍 **{data['contact_info']['location']}**")

if __name__ == "__main__":
    main()
