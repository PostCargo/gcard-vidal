import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Vidal Urrego | PostCargo SAS",
    page_icon="📇",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# Manejo robusto de imágenes (fallback si no existen o fallan)
# ---------------------------------------------------------
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        return None
    return None

logo_b64 = get_base64_image("logo.png")
foto_b64 = get_base64_image("vidal_urrego.png")

if foto_b64:
    foto_html = f'<img src="data:image/png;base64,{foto_b64}" class="profile-photo">'
else:
    foto_html = '<div class="profile-photo photo-fallback">VU</div>'

if logo_b64:
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" class="company-logo">'
else:
    logo_html = '<div class="logo-fallback">PostCargo SAS</div>'

# ---------------------------------------------------------
# CSS Global
# ---------------------------------------------------------
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        div[data-testid="stToolbar"] {visibility: hidden;}
        div[data-testid="stDecoration"] {visibility: hidden;}
        div[data-testid="stStatusWidget"] {visibility: hidden;}
        div[data-testid="stSidebarCollapsedControl"] {visibility: hidden;}

        html, body, [class*="css"] {
            font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        }

        .stApp {
            background: #ffffff;
        }

        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* -------------------- CONTENEDOR SPLIT 50/50 -------------------- */
        .split-container {
            display: flex;
            width: 100%;
            min-height: 100vh;
        }

        /* -------------------- MITAD IZQUIERDA (PERSONAL) -------------------- */
        .left-panel {
            flex: 1;
            background: #ffffff;
            color: #10193a;
            padding: 60px 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .profile-photo {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #e2e6f0;
            box-shadow: 0 6px 20px rgba(15, 37, 87, 0.15);
            margin-bottom: 22px;
        }

        .photo-fallback {
            display: flex;
            align-items: center;
            justify-content: center;
            background: #0f2557;
            color: #ffffff;
            font-size: 44px;
            font-weight: 700;
        }

        .exec-name {
            font-size: 26px;
            font-weight: 800;
            color: #0f2557;
            letter-spacing: 0.3px;
            margin-bottom: 4px;
        }

        .exec-role {
            font-size: 15.5px;
            font-weight: 500;
            color: #5b6c8f;
            margin-bottom: 26px;
        }

        .contact-list {
            width: 100%;
            max-width: 300px;
            text-align: left;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 4px;
            color: #24304f;
            text-decoration: none;
            font-size: 14.5px;
            border-bottom: 1px solid #eef1f7;
            transition: opacity 0.15s ease;
        }

        .contact-item:hover {
            opacity: 0.7;
        }

        .contact-icon {
            font-size: 16px;
            width: 20px;
            text-align: center;
        }

        .address-link {
            display: block;
            margin-top: 14px;
            padding: 14px 16px;
            background: #f4f6fb;
            border-radius: 12px;
            color: #24304f;
            text-decoration: none;
            font-size: 13.5px;
            line-height: 1.5;
            border: 1px solid #e6eaf3;
            transition: background 0.15s ease;
        }

        .address-link:hover {
            background: #ecf0f9;
        }

        .address-link strong {
            display: block;
            color: #0f2557;
            font-size: 13px;
            margin-bottom: 4px;
        }

        /* -------------------- MITAD DERECHA (EMPRESA) -------------------- */
        .right-panel {
            flex: 1;
            background: linear-gradient(160deg, #0a1a3f 0%, #0f2557 45%, #16326e 100%);
            color: #ffffff;
            padding: 60px 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .company-logo {
            max-width: 260px;
            width: 85%;
            height: auto;
            margin-bottom: 14px;
            filter: drop-shadow(0 4px 14px rgba(0,0,0,0.35));
        }

        .logo-fallback {
            font-size: 30px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 1px;
            margin-bottom: 14px;
        }

        .tagline {
            font-size: 14.5px;
            color: #c3d0ee;
            font-weight: 500;
            margin-bottom: 28px;
            max-width: 280px;
            line-height: 1.5;
        }

        .services-list {
            list-style: none;
            padding: 0;
            margin: 0 0 30px 0;
            text-align: left;
        }

        .services-list li {
            font-size: 15px;
            color: #ffffff;
            padding: 7px 0;
            font-weight: 500;
            letter-spacing: 0.2px;
        }

        .video-btn {
            display: inline-block;
            padding: 12px 26px;
            border-top: 1px solid rgba(255,255,255,0.5);
            border-bottom: 1px solid rgba(255,255,255,0.5);
            color: #ffffff;
            text-decoration: none;
            font-size: 13.5px;
            font-weight: 600;
            letter-spacing: 0.3px;
            margin-bottom: 34px;
            transition: background 0.2s ease;
        }

        .video-btn:hover {
            background: rgba(255, 255, 255, 0.08);
        }

        .company-footer {
            font-size: 12px;
            color: #9fb3d9;
            line-height: 1.6;
        }

        .company-footer a {
            color: #d8e2f7;
            text-decoration: none;
            font-weight: 600;
        }

        .company-footer a:hover {
            text-decoration: underline;
        }

        /* -------------------- RESPONSIVE MOBILE-FIRST -------------------- */
        @media (max-width: 768px) {
            .split-container {
                flex-direction: column;
                min-height: unset;
            }

            .right-panel {
                order: 1;
                padding: 40px 24px 34px 24px;
            }

            .left-panel {
                order: 2;
                padding: 40px 24px 50px 24px;
            }

            .company-logo {
                max-width: 210px;
            }

            .profile-photo, .photo-fallback {
                width: 120px;
                height: 120px;
            }

            .contact-list, .address-link {
                max-width: 100%;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Estructura HTML (Split 50/50)
# ---------------------------------------------------------
st.markdown(f"""
    <div class="split-container">

        <!-- ===================== MITAD IZQUIERDA: PERSONAL ===================== -->
        <div class="left-panel">
            {foto_html}
            <div class="exec-name">Vidal Urrego Silva</div>
            <div class="exec-role">Gerente General</div>

            <div class="contact-list">
                <a href="mailto:vidal.urrego@postcargo.co?subject=Contacto%20Desde%20Tarjeta%20Digital" class="contact-item">
                    <span class="contact-icon">✉️</span> vidal.urrego@postcargo.co
                </a>
                <a href="tel:+573115653897" class="contact-item">
                    <span class="contact-icon">📱</span> Cel: 311 565 3897
                </a>
                <a href="tel:+576013001431" class="contact-item">
                    <span class="contact-icon">☎️</span> Tel: (601) 300 1431
                </a>
                <div class="contact-item" style="border-bottom: none;">
                    <span class="contact-icon">📍</span> Bogotá - Colombia
                </div>

                <a href="https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7" target="_blank" class="address-link">
                    <strong>Dirección Principal</strong>
                    Carrera 97 No. 24 C – 23 Bodega 10<br>
                    Muelle Industrial 1 - Bogotá – Colombia
                </a>
            </div>
        </div>

        <!-- ===================== MITAD DERECHA: EMPRESA ===================== -->
        <div class="right-panel">
            {logo_html}
            <div class="tagline">Operador Logístico Especializado en Reexpediciones</div>

            <ul class="services-list">
                <li>• Paqueteo</li>
                <li>• Mensajería</li>
                <li>• Operaciones Especiales</li>
            </ul>

            <a href="https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing" target="_blank" class="video-btn">
                ℹ️ Más Información (Video)
            </a>

            <div class="company-footer">
                Cobertura Nacional e Internacional<br>
                <a href="https://www.postcargo.co" target="_blank">www.postcargo.co</a>
            </div>
        </div>

    </div>
""", unsafe_allow_html=True)
