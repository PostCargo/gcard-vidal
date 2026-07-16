import streamlit as st
import base64
import os

# ==========================================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Vidal Urrego Silva | PostCargo",
    page_icon="📇",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def get_base64_image(image_path: str, fallback_url: str) -> str:
    """
    Codifica una imagen local a Base64 para incrustarla en el HTML.
    Si el archivo no existe, no se puede leer, o falla la ruta en el
    servidor (por ejemplo en Streamlit Cloud / HF Spaces), retorna una
    URL de respaldo para que la página nunca se muestre rota o vacía.
    """
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                encoded = base64.b64encode(img_file.read()).decode("utf-8")
            ext = image_path.split(".")[-1].lower()
            mime = "png" if ext == "png" else "jpeg"
            return f"data:image/{mime};base64,{encoded}"
        return fallback_url
    except Exception:
        return fallback_url


# URLs de respaldo (placeholders) en caso de que logo.png o vidal_urrego.png
# no se encuentren en el servidor de despliegue.
FALLBACK_LOGO = "https://placehold.co/500x200/0a1a3f/ffffff?text=PostCargo"
FALLBACK_PROFILE = "https://placehold.co/400x400/f8f9fa/16326e?text=Vidal+Urrego"

logo_src = get_base64_image("logo.png", FALLBACK_LOGO)
profile_src = get_base64_image("vidal_urrego.png", FALLBACK_PROFILE)


# ==========================================================
# BLOQUE 1: CSS PURO (cadena normal, sin f-string)
# Se inyecta por separado del HTML para evitar SyntaxError
# por llaves { } de CSS mezcladas con variables de Python.
# ==========================================================
CSS_STYLES = """
<style>

/* ---------- LIMPIEZA DE INTERFAZ NATIVA DE STREAMLIT ---------- */
#MainMenu {visibility: hidden !important;}
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}
[data-testid="collapsedControl"] {display: none !important;}
#stDecoration {display: none !important;}

html, body {
    margin: 0 !important;
    padding: 0 !important;
    height: 100% !important;
    overflow-x: hidden !important;
}

[data-testid="stAppViewContainer"] {
    padding: 0 !important;
    margin: 0 !important;
}

[data-testid="stAppViewContainer"] > .main {
    padding: 0 !important;
    margin: 0 !important;
}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
    height: 0 !important;
    display: none !important;
}

/* ---------- CONTENEDOR PRINCIPAL SPLIT 50/50 ---------- */
.card-container {
    display: flex;
    flex-direction: row;
    width: 100vw;
    min-height: 100vh;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
}

.col-personal, .col-corporate {
    width: 50%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px 40px;
}

/* ---------- COLUMNA IZQUIERDA: PERSONAL (CLARA) ---------- */
.col-personal {
    background-color: #ffffff;
    color: #1b2a4a;
    order: 1;
}

.profile-photo {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    object-fit: cover;
    border: 5px solid #ffffff;
    outline: 1px solid #eef1f5;
    box-shadow: 0 15px 35px rgba(22, 50, 110, 0.22);
    margin-bottom: 24px;
}

.profile-name {
    font-size: 28px;
    font-weight: 700;
    color: #14213d;
    margin: 0;
    text-align: center;
    letter-spacing: 0.3px;
}

.profile-title {
    font-size: 15px;
    font-weight: 600;
    color: #5b7291;
    margin: 4px 0 32px 0;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1.4px;
}

.contact-list {
    width: 100%;
    max-width: 340px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 30px;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: #22345c;
    font-size: 15.5px;
    font-weight: 500;
    padding: 6px 2px;
    border-bottom: 1px solid #eef1f5;
    transition: all 0.25s ease;
}

a.contact-item:hover {
    color: #16326e;
    padding-left: 8px;
    border-bottom: 1px solid #16326e;
}

.contact-icon {
    font-size: 18px;
    width: 22px;
    text-align: center;
    flex-shrink: 0;
}

.address-block {
    width: 100%;
    max-width: 340px;
    background-color: #f8f9fa;
    border: 1px solid #e6e9ee;
    border-radius: 14px;
    padding: 18px 20px;
    text-decoration: none;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    transition: all 0.25s ease;
    box-shadow: 0 4px 14px rgba(20, 33, 61, 0.05);
}

.address-block:hover {
    box-shadow: 0 10px 24px rgba(20, 33, 61, 0.13);
    transform: translateY(-2px);
}

.address-label {
    font-size: 11.5px;
    font-weight: 700;
    color: #16326e;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin: 0 0 4px 0;
}

.address-text {
    font-size: 13.5px;
    color: #3c4a63;
    line-height: 1.5;
    margin: 0;
}

/* ---------- COLUMNA DERECHA: CORPORATIVA (AZUL) ---------- */
.col-corporate {
    background: linear-gradient(160deg, #0a1a3f 0%, #16326e 100%);
    color: #ffffff;
    order: 2;
    justify-content: space-between;
}

.corporate-top {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.logo-img {
    max-width: 280px;
    width: 80%;
    height: auto;
    margin-bottom: 18px;
}

.tagline {
    font-size: 15px;
    color: #a9c2e8;
    text-align: center;
    font-weight: 400;
    margin-bottom: 40px;
    letter-spacing: 0.3px;
    max-width: 320px;
    line-height: 1.5;
}

.services-list {
    width: 100%;
    max-width: 300px;
    text-align: left;
    margin-bottom: 40px;
}

.services-title {
    font-size: 12px;
    color: #7d9bce;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 700;
    margin: 0 0 14px 0;
}

.service-item {
    font-size: 16.5px;
    font-weight: 500;
    color: #ffffff;
    margin: 0 0 12px 0;
    padding-left: 4px;
}

.cta-button {
    display: inline-block;
    background-color: #ffffff;
    color: #0a1a3f;
    font-weight: 700;
    font-size: 14.5px;
    padding: 14px 36px;
    border-radius: 30px;
    text-decoration: none;
    letter-spacing: 0.4px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.22);
    transition: all 0.25s ease;
    margin-bottom: 10px;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.32);
}

.corporate-footer {
    text-align: center;
    margin-top: auto;
    padding-top: 30px;
}

.footer-coverage {
    font-size: 13px;
    color: #a9c2e8;
    font-weight: 600;
    letter-spacing: 0.6px;
    margin: 0 0 6px 0;
}

.footer-link {
    font-size: 14.5px;
    color: #ffffff;
    font-weight: 700;
    text-decoration: none;
    border-bottom: 1px solid rgba(255,255,255,0.4);
    padding-bottom: 2px;
    transition: all 0.25s ease;
}

.footer-link:hover {
    border-bottom: 1px solid #ffffff;
    color: #cfe0f7;
}

/* ---------- RESPONSIVE / MOBILE-FIRST ----------
   En pantallas pequeñas las columnas se apilan verticalmente.
   La sección corporativa (azul) va ARRIBA para priorizar el
   branding, y la sección personal (clara) va ABAJO. */
@media (max-width: 768px) {
    .card-container {
        flex-direction: column;
        min-height: 100vh;
        height: auto;
    }
    .col-personal, .col-corporate {
        width: 100%;
        padding: 44px 24px;
    }
    .col-personal {
        order: 2;
    }
    .col-corporate {
        order: 1;
        padding-top: 52px;
    }
    .profile-photo {
        width: 140px;
        height: 140px;
    }
    .logo-img {
        max-width: 220px;
    }
    .contact-list, .address-block, .services-list {
        max-width: 100%;
    }
}

</style>
"""

# ==========================================================
# BLOQUE 2: HTML (f-string SOLO con variables de imagen,
# sin llaves de estilo mezcladas, para evitar errores de
# compilación en el f-string).
# ==========================================================
HTML_CONTENT = f"""
<div class="card-container">

    <div class="col-personal">
        <img src="{profile_src}" class="profile-photo" alt="Vidal Urrego Silva">
        <h1 class="profile-name">Vidal Urrego Silva</h1>
        <p class="profile-title">Gerente General</p>

        <div class="contact-list">
            <a href="mailto:vidal.urrego@postcargo.co?subject=Contacto%20Desde%20Tarjeta%20Digital" class="contact-item">
                <span class="contact-icon">✉️</span>
                <span>vidal.urrego@postcargo.co</span>
            </a>
            <a href="tel:+573115653897" class="contact-item">
                <span class="contact-icon">📱</span>
                <span>Cel: 311 565 3897</span>
            </a>
            <a href="tel:+576013001431" class="contact-item">
                <span class="contact-icon">☎️</span>
                <span>Tel: (601) 300 1431</span>
            </a>
            <div class="contact-item">
                <span class="contact-icon">📍</span>
                <span>Bogotá - Colombia</span>
            </div>
        </div>

        <a href="https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7" target="_blank" rel="noopener noreferrer" class="address-block">
            <span class="contact-icon">🏢</span>
            <div>
                <p class="address-label">Oficina Principal</p>
                <p class="address-text">Carrera 97 No. 24 C – 23 Bodega 10, Muelle Industrial 1<br>Bogotá – Colombia</p>
            </div>
        </a>
    </div>

    <div class="col-corporate">
        <div class="corporate-top">
            <img src="{logo_src}" class="logo-img" alt="PostCargo">
            <p class="tagline">Operador Logístico Especializado en Reexpediciones</p>

            <div class="services-list">
                <p class="services-title">Nuestros Servicios</p>
                <p class="service-item">• Paqueteo</p>
                <p class="service-item">• Mensajería</p>
                <p class="service-item">• Operaciones Especiales</p>
            </div>

            <a href="https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing" target="_blank" rel="noopener noreferrer" class="cta-button">
                Más Información ▶
            </a>
        </div>

        <div class="corporate-footer">
            <p class="footer-coverage">Cobertura Nacional e Internacional</p>
            <a href="https://www.postcargo.co" target="_blank" rel="noopener noreferrer" class="footer-link">www.postcargo.co</a>
        </div>
    </div>

</div>
"""

# ==========================================================
# RENDERIZADO
# ==========================================================
st.markdown(CSS_STYLES, unsafe_allow_html=True)
st.markdown(HTML_CONTENT, unsafe_allow_html=True)
