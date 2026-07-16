import streamlit as st
import base64
import os

# ==========================================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Vidal Urrego Silva | PostCargo",
    page_icon="📇",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def get_base64_image(image_path: str, fallback_url: str) -> str:
    """
    Codifica una imagen local a Base64 para incrustarla en el HTML.
    Si el archivo no existe, no se puede leer, o falla la ruta en el
    servidor (Streamlit Community Cloud, HF Spaces, etc.), retorna una
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


# URLs de respaldo (placeholders) por si logo.png o vidal_urrego.png
# no se encuentran en el servidor de despliegue.
FALLBACK_LOGO = "https://placehold.co/500x200/0a1a3f/ffffff?text=PostCargo"
FALLBACK_PROFILE = "https://placehold.co/400x400/16326e/ffffff?text=Vidal+Urrego"

logo_src = get_base64_image("logo.png", FALLBACK_LOGO)
profile_src = get_base64_image("vidal_urrego.png", FALLBACK_PROFILE)


# ==========================================================
# BLOQUE 1: CSS PURO (cadena normal, SIN f-string)
# Se inyecta por separado del HTML para que las llaves { } de
# CSS nunca se mezclen con las variables de Python y así evitar
# errores de sintaxis o que el HTML se muestre como texto crudo.
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
[data-testid="stHeader"] {background: transparent !important; height: 0 !important; display: none !important;}
#stDecoration {display: none !important;}

html, body {
    margin: 0 !important;
    padding: 0 !important;
}

/* ---------- FONDO GENERAL DE LA APP ---------- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0a1a3f 0%, #16326e 100%);
}

[data-testid="stAppViewContainer"] > .main {
    padding: 0 !important;
}

.block-container {
    padding: 0 !important;
    margin: 0 auto !important;
    max-width: 480px !important;
}

/* ---------- TARJETA / CONTENEDOR PRINCIPAL ---------- */
.gcard {
    width: 100%;
    box-sizing: border-box;
    padding: 40px 26px 34px 26px;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #ffffff;
}

/* ---------- LOGO ---------- */
.logo-img {
    width: 78%;
    max-width: 300px;
    height: auto;
    margin-bottom: 6px;
}

.hr-soft {
    width: 60px;
    height: 3px;
    border-radius: 3px;
    background: rgba(255,255,255,0.25);
    margin: 22px 0;
    border: none;
}

/* ---------- FOTO Y DATOS DEL EJECUTIVO ---------- */
.profile-photo {
    width: 148px;
    height: 148px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid rgba(255,255,255,0.85);
    box-shadow: 0 12px 28px rgba(0,0,0,0.28);
    margin-bottom: 18px;
}

.profile-name {
    font-size: 24px;
    font-weight: 700;
    color: #ffffff;
    margin: 0;
    text-align: center;
    letter-spacing: 0.3px;
}

.profile-title {
    font-size: 14.5px;
    font-weight: 600;
    color: #a9c2e8;
    margin: 6px 0 2px 0;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1.3px;
}

.profile-company {
    font-size: 13px;
    font-weight: 500;
    color: #7d9bce;
    margin: 0;
    text-align: center;
    letter-spacing: 0.5px;
}

/* ---------- LISTA DE CONTACTO ---------- */
.contact-list {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: 6px;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 14px;
    text-decoration: none;
    color: #eef3fb;
    font-size: 15.5px;
    font-weight: 500;
    padding: 13px 6px;
    border-bottom: 1px solid rgba(255,255,255,0.10);
    transition: all 0.2s ease;
}

a.contact-item:active,
a.contact-item:hover {
    color: #ffffff;
    background-color: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding-left: 12px;
}

.contact-icon {
    font-size: 19px;
    width: 24px;
    text-align: center;
    flex-shrink: 0;
}

/* ---------- BLOQUE DE DIRECCIÓN ---------- */
.address-block {
    width: 100%;
    box-sizing: border-box;
    background-color: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 14px;
    padding: 16px 18px;
    margin-top: 16px;
    text-decoration: none;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    transition: all 0.2s ease;
}

.address-block:hover,
.address-block:active {
    background-color: rgba(255,255,255,0.10);
    transform: translateY(-1px);
}

.address-label {
    font-size: 11px;
    font-weight: 700;
    color: #a9c2e8;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin: 0 0 5px 0;
}

.address-text {
    font-size: 13.5px;
    color: #e5ecf8;
    line-height: 1.55;
    margin: 0;
}

/* ---------- SECCIÓN CORPORATIVA ---------- */
.section-label {
    width: 100%;
    font-size: 11.5px;
    font-weight: 700;
    color: #7d9bce;
    text-transform: uppercase;
    letter-spacing: 1.6px;
    margin-bottom: 12px;
}

.tagline {
    font-size: 15.5px;
    color: #e5ecf8;
    text-align: center;
    font-weight: 500;
    font-style: italic;
    margin: 0 0 22px 0;
    line-height: 1.5;
    max-width: 360px;
}

.services-wrap {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 26px;
}

.service-pill {
    background-color: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    color: #ffffff;
    font-size: 13.5px;
    font-weight: 600;
    padding: 9px 18px;
    border-radius: 30px;
}

.cta-button {
    display: block;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
    background-color: #ffffff;
    color: #0a1a3f;
    font-weight: 700;
    font-size: 15px;
    padding: 15px 20px;
    border-radius: 12px;
    text-decoration: none;
    letter-spacing: 0.3px;
    box-shadow: 0 10px 22px rgba(0,0,0,0.25);
    transition: all 0.2s ease;
    margin-bottom: 8px;
}

.cta-button:hover,
.cta-button:active {
    transform: translateY(-2px);
    box-shadow: 0 14px 28px rgba(0,0,0,0.32);
}

/* ---------- PIE DE PÁGINA ---------- */
.card-footer {
    text-align: center;
    margin-top: 30px;
    padding-top: 22px;
    border-top: 1px solid rgba(255,255,255,0.12);
    width: 100%;
}

.footer-coverage {
    font-size: 12.5px;
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
    transition: all 0.2s ease;
}

.footer-link:hover {
    border-bottom: 1px solid #ffffff;
    color: #cfe0f7;
}

/* ---------- AJUSTES MÓVILES ---------- */
@media (max-width: 480px) {
    .gcard {
        padding: 32px 20px 28px 20px;
    }
    .profile-photo {
        width: 130px;
        height: 130px;
    }
    .logo-img {
        max-width: 240px;
    }
}

</style>
"""

# ==========================================================
# BLOQUE 2: HTML (f-string SOLO con variables de imagen).
# No se usa ni un solo estilo inline con llaves, por lo que
# el f-string es 100% seguro de renderizar.
# ==========================================================
HTML_CONTENT = f"""
<div class="gcard">

    <img src="{logo_src}" class="logo-img" alt="PostCargo SAS">

    <hr class="hr-soft">

    <img src="{profile_src}" class="profile-photo" alt="Vidal Urrego Silva">
    <p class="profile-name">Vidal Urrego Silva</p>
    <p class="profile-title">Gerente General</p>
    <p class="profile-company">PostCargo SAS</p>

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
            <p class="address-text">Carrera 97 No. 24 C – 23 Bodega 10 Muelle Industrial 1<br>Bogotá – Colombia</p>
        </div>
    </a>

    <hr class="hr-soft">

    <p class="section-label">Sobre la Empresa</p>
    <p class="tagline">"Operador Logístico Especializado en Reexpediciones"</p>

    <div class="services-wrap">
        <span class="service-pill">📦 Paqueteo</span>
        <span class="service-pill">✉️ Mensajería</span>
        <span class="service-pill">⚙️ Operaciones Especiales</span>
    </div>

    <a href="https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing" target="_blank" rel="noopener noreferrer" class="cta-button">
        ℹ️ Más Información (Video)
    </a>

    <div class="card-footer">
        <p class="footer-coverage">Cobertura Nacional e Internacional</p>
        <a href="https://www.postcargo.co" target="_blank" rel="noopener noreferrer" class="footer-link">www.postcargo.co</a>
    </div>

</div>
"""

# ==========================================================
# RENDERIZADO
# ==========================================================
st.markdown(CSS_STYLES, unsafe_allow_html=True)
st.markdown(HTML_CONTENT, unsafe_allow_html=True)
