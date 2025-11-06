# portfolio_app.py
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import requests
from streamlit_extras.metric_cards import style_metric_cards
import json

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Sarang Gulve - Portfolio", page_icon="🚀", layout="wide")

# -----------------------------
# Helper Functions
# -----------------------------
def load_lottie_url(url):
    """Load a Lottie animation from a given URL"""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# -----------------------------
# Load Lottie Animation (Verified Working URL)
# -----------------------------
lottie_ds = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_tno6cg2w.json")

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(135deg, #0a0f1f 0%, #1a1c23 100%);
        background-attachment: fixed;
        color: #fafafa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #00e6e6;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c0f0, #0066ff);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1em;
        font-weight: bold;
        border: none;
    }
    .card {
        background: #1a1c23;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        transition: 0.3s;
    }
    .card:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 25px rgba(0,192,240,0.4);
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
    col1, col2 = st.columns(2)
    with col1:
        st.title("🚀 Sarang Gulve")
        st.subheader("Data Scientist | AI & Remote Sensing Specialist")
        st.write("📍 Nashik, India")
        st.write("✉️ [Email](mailto:saranggulve@gmail.com)")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/sarang-gulve-ab1477250/) | 💻 [GitHub](https://github.com/SARANGGULVE)")
        st.markdown("---")
        st.info("Results-driven Data Scientist with expertise in AI, ML, Python, TensorFlow, SQL, and satellite imagery. Delivered end-to-end projects in agriculture, climate forecasting, and AI-powered applications to drive data-driven solutions.")
    with col2:
        if lottie_ds:
            st_lottie(lottie_ds, height=280, key="home")
        else:
            st.warning("⚠️ Animation failed to load — please check your internet connection.")

    st.markdown("---")
    st.subheader("📊 Quick Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Years of Experience", "1")
    col2.metric("Projects Completed", "10+")
    col3.metric("Research Papers", "0")
    style_metric_cards(background_color="#1a1c23", border_color="#00c0f0", border_left_color="#00e6e6")

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
    st.header("🧠 Skill Radar Chart")

    skills = {
        "Python": 90,
        "Machine Learning": 85,
        "Deep Learning": 80,
        "Remote Sensing": 88,
        "FastAPI": 75,
        "SQL": 70,
        "TensorFlow": 80,
        "Power BI": 65,
    }

    fig = go.Figure(data=go.Scatterpolar(
        r=list(skills.values()),
        theta=list(skills.keys()),
        fill='toself',
        marker_color='#00c0f0'
    ))

    fig.update_layout(
        polar=dict(bgcolor="#1a1c23", radialaxis=dict(visible=True, range=[0,100])),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

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

    st.markdown("---")
    st.subheader("💬 Send a Message")
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message 🚀")

        if submit:
            st.success("Thanks for reaching out! I'll get back to you soon.")

    st.markdown("---")
    try:
        with open("Sarang_Gulve_Resume.pdf", "rb") as file:
            st.download_button("📄 Download My Resume", file, "Sarang_Gulve_Resume.pdf")
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found. Please add 'Sarang_Gulve_Resume.pdf' to your project folder.")

    st.success("Let's collaborate on impactful AI & Data Science projects!")
     
