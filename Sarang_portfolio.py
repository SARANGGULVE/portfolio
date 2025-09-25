# portfolio_app.py
import streamlit as st
from streamlit_option_menu import option_menu

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Sarang Gulve - Portfolio", page_icon="🚀", layout="wide")

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #fafafa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #00c0f0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c0f0, #0066ff);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1em;
        font-weight: bold;
    }
    .card {
        background: #1a1c23;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Navigation
# -----------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Experience", "Projects", "Skills", "Education", "Contact"],
        icons=["house", "briefcase", "folder", "tools", "mortarboard", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# -----------------------------
# Home
# -----------------------------
if selected == "Home":
    st.title("🚀 Sarang Gulve")
    st.subheader("Data Scientist | AI & Remote Sensing Specialist")
    st.write("📍 Nashik, India | ✉️ [Email](mailto:saranggulve@gmail.com) | 🔗 [LinkedIn](https://www.linkedin.com/in/sarang-gulve-ab1477250/) | 💻 [GitHub](https://github.com/SARANGGULVE)")
    st.markdown("---")
    st.info("Results-driven Data Scientist with expertise in AI, ML, Python, TensorFlow, SQL, and satellite imagery. Delivered end-to-end projects in agriculture, climate forecasting, and AI-powered applications to drive data-driven solutions.")

# -----------------------------
# Experience
# -----------------------------
elif selected == "Experience":
    st.header("💼 Professional Experience")
    
    st.markdown("""<div class="card">
    <h3>PlanetEye FarmAI | Data Scientist</h3>
    <i>Mar 2025 - Jul 2025</i>
    <ul>
        <li>Built ML/DL models for predictive analysis using Sentinel-1/2 imagery</li>
        <li>Developed FastAPI endpoints handling 1000+ satellite image requests daily</li>
        <li>Automated vegetation, water, and moisture indices using Earth Engine</li>
    </ul></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <h3>Digital Hercules Innovations | Data Analyst</h3>
    <i>Sep 2024 - Feb 2025</i>
    <ul>
        <li>Performed statistical analysis and predictive modeling for business datasets</li>
        <li>Created interactive Power BI dashboards reducing reporting time</li>
        <li>Built preprocessing pipelines to optimize datasets for analysis</li>
    </ul></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <h3>ESDS Software Solutions | Data Scientist Intern</h3>
    <i>Jun 2022 - Jul 2022</i>
    <ul>
        <li>Developed ML classification model achieving high accuracy</li>
        <li>Deployed real-time AI applications using FastAPI and Streamlit</li>
    </ul></div>""", unsafe_allow_html=True)

# -----------------------------
# Projects
# -----------------------------
elif selected == "Projects":
    st.header("📂 Projects")
    projects = {
        "🌱 Agricultural Crop Land Monitoring": {
            "link": "https://github.com/SARANGGULVE/Agricultural-Crop-land-monitoring-",
            "desc": "Comprehensive monitoring system using Sentinel-1/2 and Earth Engine API."
        },
        "🥥 Sugarcane Crop Identification": {
            "link": "https://github.com/SARANGGULVE/Sugarcane-Corp-Identification-",
            "desc": "Automated system to identify sugarcane crop using satellite imagery and ML."
        },
        "🍂 Plant Disease Detection (CNN)": {
            "link": "https://github.com/SARANGGULVE/Plant-Disease-detection-System-",
            "desc": "CNN-based detection system for plant diseases with high accuracy."
        },
        "🗣️ AWAAJAI Dubbing System": {
            "link": "https://github.com/SARANGGULVE/AI_Dubbing_AWAAJ",
            "desc": "Multilingual AI dubbing system with speech recognition and TTS."
        }
    }

    for title, details in projects.items():
        st.markdown(f"""<div class="card">
        <h3>{title}</h3>
        <p>{details['desc']}</p>
        <a href="{details['link']}" target="_blank">🔗 View on GitHub</a>
        </div>""", unsafe_allow_html=True)

# -----------------------------
# Skills
# -----------------------------
elif selected == "Skills":
    st.header("🛠️ Technical Skills")
    skills = {
        "Python": 90,
        "Machine Learning": 85,
        "Deep Learning": 80,
        "Remote Sensing & GIS": 88,
        "FastAPI & Streamlit": 75,
        "SQL & Databases": 70,
        "TensorFlow & PyTorch": 80,
        "Power BI & Visualization": 65,
    }

    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

# -----------------------------
# Education
# -----------------------------
elif selected == "Education":
    st.header("🎓 Education")
    st.markdown("""<div class="card">
    <h3>B.E. in AI & Data Science</h3>
    <p>Savitribai Phule Pune University (2021 – 2024)</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <h3>Diploma in Computer Science</h3>
    <p>Loknete Gopalraoji Gulve Polytechnic, Nashik (2019 – 2021)</p>
    </div>""", unsafe_allow_html=True)

# -----------------------------
# Contact
# -----------------------------
elif selected == "Contact":
    st.header("📬 Contact Me")
    st.write("📞 Phone: +91 9370065435")
    st.write("✉️ Email: [saranggulve@gmail.com](mailto:saranggulve@gmail.com)")
    st.write("🔗 LinkedIn: [Profile](https://www.linkedin.com/in/sarang-gulve-ab1477250/)")
    st.write("💻 GitHub: [SARANGGULVE](https://github.com/SARANGGULVE)")
    st.success("Let's collaborate on impactful AI & Data Science projects!")
