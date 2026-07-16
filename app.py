import streamlit as st
import base64
import os

# Configuración de página expandida para lograr el Layout 50/50 horizontal
st.set_page_config(
    page_title="Vidal Urrego Silva | PostCargo",
    page_icon="📇",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- MANEJO ROBUSTO DE IMÁGENES ---
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

# Urls de respaldo por si el hosting de la nube tiene problemas con las rutas
logo_src = f"data:image/png;base64,{logo_b64}" if logo_b64 else "https://www.postcargo.co/wp-content/uploads/2021/07/logo-postcargo.png"
foto_src = f"data:image/png;base64,{foto_b64}" if foto_b64 else "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"

# --- INYECCIÓN DE ESTILOS CSS GENERALES ---
st.markdown("""
    <style>
        /* Ocultar elementos nativos de Streamlit */
        #MainMenu, footer, header, div[data-testid="stToolbar"], 
        div[data-testid="stDecoration"], div[data-testid="stStatusWidget"],
        div[data-testid="stSidebarCollapsedControl"] {
            visibility: hidden; display: none !important;
        }

        html, body, [class*="css"] {
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: #ffffff;
        }

        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* CONTENEDOR SPLIT HORIZONTAL 50/50 */
        .split-container {
            display: flex;
            width: 100vw;
            min-height: 100vh;
        }

        /* MITAD IZQUIERDA: DON VIDAL (FONDO BLANCO) */
        .left-panel {
            flex: 1;
            background: #ffffff;
            color: #10193a;
            padding: 60px 50px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .profile-photo {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #0f2557;
            box-shadow: 0 6px 20px rgba(15, 37, 87, 0.15);
            margin-bottom: 20px;
        }

        .exec-name {
            font-size: 28px;
            font-weight: 800;
            color: #0f2557;
            margin-bottom: 4px;
        }

        .exec-role {
            font-size: 16px;
            font-weight: 500;
            color: #5b6c8f;
            margin-bottom: 30px;
        }

        .contact-list {
            width: 100%;
            max-width: 320px;
            text-align: left;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 4px;
            color: #24304f !important;
            text-decoration: none !important;
            font-size: 15px;
            border-bottom: 1px solid #eef1f7;
            transition: color 0.15s ease;
        }

        .contact-item:hover {
            color: #0f2557 !important;
            font-weight: 500;
        }

        .address-link {
            display: block;
            margin-top: 18px;
            padding: 16px;
            background: #f4f6fb;
            border-radius: 12px;
            color: #24304f !important;
            text-decoration: none !important;
            font-size: 14px;
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
            margin-bottom: 4px;
        }

        /* MITAD DERECHA: EMPRESA (FONDO AZUL REY) */
        .right-panel {
            flex: 1;
            background: linear-gradient(160deg, #0a1a3f 0%, #0f2557 45%, #16326e 100%);
            color: #ffffff;
            padding: 60px 50px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .company-logo {
            max-width: 280px;
            width: 90%;
            height: auto;
            margin-bottom: 18px;
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.3));
        }

        .tagline {
            font-size: 16px;
            color: #c3d0ee;
            font-weight: 500;
            margin-bottom: 30px;
            max-width: 320px;
            line-height: 1.4;
        }

        .services-list {
            list-style: none;
            padding: 0;
            margin: 0 0 35px 0;
            text-align: left;
        }

        .services-list li {
            font-size: 15.5px;
            color: #ffffff;
            padding: 6px 0;
            font-weight: 500;
        }

        /* Botón Estilizado Fino para el Video */
        .video-btn {
            display: inline-block;
            padding: 12px 28px;
            background: #ffffff;
            color: #0f2557 !important;
            border-radius: 8px;
            text-decoration: none !important;
            font-size: 14px;
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 35px;
            transition: transform 0.2s;
        }

        .video-btn:active {
            transform: scale(0.97);
        }

        .company-footer {
            font-size: 12.5px;
            color: #9fb3d9;
            line-height: 1.6;
            border-top: 1px solid rgba(255,255,255,0.15);
            padding-top: 15px;
            width: 80%;
            max-width: 300px;
        }

        .company-footer a {
            color: #ffffff !important;
            text-decoration: none !important;
            font-weight: 600;
        }

        /* RESPONSIVE: APILADO EN CELULARES */
        @media (max-width: 768px) {
            .split-container {
                flex-direction: column;
                min-height: unset;
            }
            .right-panel {
                order: 1;
                padding: 50px 25px 40px 25px;
            }
            .left-panel {
                order: 2;
                padding: 40px 25px 50px 25px;
            }
            .company-logo {
                max-width: 240px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- RENDERIZADO DEL CONTENIDO HTML ---
st.markdown(f"""
    <div class="split-container">

        <!-- LADO IZQUIERDO: SECCIÓN PERSONAL (DON VIDAL) -->
        <div class="left-panel">
            <img src="{foto_src}" class="profile-photo" alt="Vidal Urrego Silva">
            <div class="exec-name">Vidal Urrego Silva</div>
            <div class="exec-role">Gerente General</div>

            <div class="contact-list">
                <a href="mailto:vidal.urrego@postcargo.co?subject=Contacto%20Desde%20Tarjeta%20Digital" class="contact-item">
                    ✉️ {sidebar_context.get('correo_vidal', 'vidal.urrego@postcargo.co')}
                </a>
                <a href="tel:+573115653897" class="contact-item">
                    📱 Cel: 311 565 3897
                </a>
                <a href="tel:+576013001431" class="contact-item">
                    ☎️ Tel: (601) 300 1431
                </a>
                <div class="contact-item" style="border-bottom: none;">
                    📍 Bogotá - Colombia
                </div>

                <a href="https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7" target="_blank" class="address-link">
                    <strong>📍 Dirección Principal</strong>
                    Carrera 97 No. 24 C – 23 Bodega 10<br>
                    Muelle Industrial 1 - Bogotá – Colombia
                </a>
            </div>
        </div>

        <!-- LADO DERECHO: SECCIÓN CORPORATIVA (POSTCARGO) -->
        <div class="right-panel">
            <img src="{logo_src}" class="company-logo" alt="PostCargo">
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
