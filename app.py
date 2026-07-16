import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Vidal Urrego | PostCargo SAS",
    page_icon="📇",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base64_image("logo.png")
foto_b64 = get_base64_image("vidal_urrego.png")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        div[data-testid="stToolbar"] {visibility: hidden;}
        div[data-testid="stDecoration"] {visibility: hidden;}
        div[data-testid="stStatusWidget"] {visibility: hidden;}

        .stApp {
            background: linear-gradient(160deg, #0a1a3f 0%, #0f2557 45%, #16326e 100%);
        }

        .block-container {
            max-width: 420px;
            padding-top: 1.5rem;
            padding-bottom: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        html, body, [class*="css"] {
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        }

        .logo-container {
            text-align: center;
            margin-bottom: 18px;
        }
        .logo-container img {
            max-width: 160px;
            width: 100%;
            height: auto;
        }

        .card-executive {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 20px;
            padding: 28px 20px 22px 20px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
            margin-bottom: 20px;
        }

        .profile-photo {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #ffffff;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4);
            margin-bottom: 16px;
        }

        .exec-name {
            color: #ffffff;
            font-size: 26px;
            font-weight: 700;
            margin: 4px 0 2px 0;
            letter-spacing: 0.3px;
        }

        .exec-role {
            color: #d8e2f7;
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 2px;
        }

        .exec-company {
            color: #9fb3d9;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-top: 4px;
        }

        .divider {
            height: 1px;
            background: rgba(255, 255, 255, 0.2);
            margin: 18px 0;
        }

        .address-box {
            background: #f4f6fb;
            color: #10193a;
            border-radius: 14px;
            padding: 16px 18px;
            text-align: left;
            margin-bottom: 22px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        }
        .address-box strong {
            display: block;
            font-size: 14px;
            color: #0f2557;
            margin-bottom: 6px;
        }
        .address-box span {
            font-size: 13.5px;
            line-height: 1.5;
            color: #2b3a5c;
        }

        .action-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 15px;
            margin-bottom: 12px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 700;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
            transition: transform 0.15s ease;
            border: none;
        }
        .action-btn:active {
            transform: scale(0.96);
        }

        .btn-call {
            background-color: #1fa855;
            color: #ffffff !important;
        }
        .btn-email {
            background-color: #e8770d;
            color: #ffffff !important;
        }
        .btn-maps {
            background-color: #1a56c4;
            color: #ffffff !important;
        }
        .btn-video {
            background-color: #ffffff;
            color: #0f2557 !important;
            border: 1px solid #d7deee;
        }

        .footer-tag {
            text-align: center;
            color: #7f93bf;
            font-size: 11px;
            margin-top: 10px;
            letter-spacing: 0.5px;
        }
    </style>
""", unsafe_allow_html=True)

if logo_b64:
    st.markdown(f"""
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_b64}" alt="PostCargo SAS">
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-container"><h2 style="color:white;">PostCargo SAS</h2></div>', unsafe_allow_html=True)

if foto_b64:
    foto_html = f'<img src="data:image/png;base64,{foto_b64}" class="profile-photo">'
else:
    foto_html = '<div class="profile-photo" style="background:#3a4d7a;display:flex;align-items:center;justify-content:center;color:white;font-size:40px;">VU</div>'

st.markdown(f"""
    <div class="card-executive">
        {foto_html}
        <div class="exec-name">Vidal Urrego</div>
        <div class="exec-role">Gerente General</div>
        <div class="exec-company">PostCargo SAS</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="address-box">
        <strong>📍 Dirección Principal:</strong>
        <span>
            Carrera 97 No. 24 C – 23 Bodega 10<br>
            Muelle Industrial 1 - Bogotá – Colombia
        </span>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <a href="tel:+573115653897" class="action-btn btn-call">
        📞 Llamar al Celular
    </a>

    <a href="mailto:vidal.urrego@postcargo.co?subject=Contacto%20Comercial%20-%20PostCargo" class="action-btn btn-email">
        ✉️ Enviar Correo
    </a>

    <a href="https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7" target="_blank" class="action-btn btn-maps">
        📍 Cómo Llegar
    </a>

    <a href="https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing" target="_blank" class="action-btn btn-video">
        ▶️ Video: ¿Quiénes Somos?
    </a>
""", unsafe_allow_html=True)

st.markdown('<div class="footer-tag">PostCargo SAS · Soluciones Logísticas</div>', unsafe_allow_html=True)
