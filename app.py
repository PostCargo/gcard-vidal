import streamlit as st
import base64
import os

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="PostCargo SAS",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================================
# DATOS DE LA TARJETA
# =========================================================
LOGO_PATH = "Logo.png"
LOGO_FALLBACK_URL = "https://placehold.co/600x220/0A1F44/FFFFFF?text=PostCargo+SAS&font=raleway"

TAGLINE = "Con Postcargo sus reexpediciones ya no son un problema"

VIDEO_URL = "https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing"
NEGOCIOS_URL = "https://www.postcargo.co/negocios/"
MAPS_URL = "https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7"
WEB_URL = "https://www.postcargo.co"

EMAIL = "comercial@postcargo.co"
CEL_TEXTO = "311 565 7737"
CEL_LINK = "+573115657737"
TEL_TEXTO = "(601)805 2591"
TEL_LINK = "+576018052591"
DIRECCION = "Carrera 97 No. 24 C - 23 Bodega 10, Muelle Industrial 1 - Bogotá, Colombia"

# =========================================================
# ESTILOS (CSS)
# =========================================================
st.markdown(
    """
    <style>
    /* ---- Ocultar menú, footer y barra de herramientas de Streamlit ---- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden; height: 0; position: fixed;}
    div[data-testid="stDecoration"] {display: none;}
    div[data-testid="stStatusWidget"] {display: none;}
    .stAppDeployButton {display: none;}

    /* ---- Fondo corporativo dinámico con degradado lineal elegante ---- */
    .stApp {
        background: linear-gradient(135deg, #07142b 0%, #0c234b 50%, #15356b 100%) !important;
    }

    /* ---- Layout tipo tarjeta, cómodo en celular ---- */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 1.3rem;
        padding-right: 1.3rem;
        max-width: 480px;
    }

    /* ---- Texto base en blanco / gris claro ---- */
    .stMarkdown p, .stMarkdown li {
        color: #EDEFF4;
        font-size: 15.5px;
    }

    /* ---- Contenedor para centrar el logo corporativo ---- */
    .pc-logo-wrap {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    /* ---- Logo corporativo ampliado ---- */
    .pc-logo-wrap img {
        max-width: 280px !important;
        height: auto !important;
        display: block !important;
    }

    /* ---- Bloques de texto centrados ---- */
    .pc-tagline {
        text-align: center;
        color: #E5E7EB;
        font-style: italic;
        font-size: 15px;
        padding: 0 6px;
        margin: 10px 0;
    }
    .pc-servicios {
        text-align: center;
        color: #F5F6FA;
        background-color: rgba(255,255,255,0.06);
        padding: 12px;
        border-radius: 10px;
        font-size: 14.5px;
        margin-top: 10px;
    }
    
    /* ---- Título de Sección Centrado ---- */
    .pc-section-title {
        text-align: center;
        color: #93A5C4;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* ---- Ítems de Contacto Centrados ---- */
    .pc-contact-item {
        text-align: center;
        color: #EDEFF4;
        font-size: 15.5px;
        margin: 8px 0;
    }

    /* ---- Centrado de la caja st.info / Cobertura Nacional ---- */
    div[data-testid="stAlert"] {
        text-align: center !important;
        justify-content: center !important;
    }
    div[data-testid="stAlert"] > div {
        justify-content: center !important;
        width: 100% !important;
    }

    .pc-footer-note {
        text-align: center;
        color: #6B7A99;
        font-size: 12px;
        margin-top: 12px;
    }

    /* ---- Enlaces de texto ---- */
    a {
        color: #9DC6FF !important;
        text-decoration: none !important;
        font-weight: 500;
    }
    a:hover {
        color: #FFFFFF !important;
    }

    /* =========================================================
       FORZADO DE BOTONES BLANCOS CON TEXTO AZUL OSCURO
       ========================================================= */
    div[data-testid="stLinkButton"] a,
    div[data-testid="stLinkButton"] button,
    .stLinkButton a {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        color: #07142b !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 0.75rem 1rem !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35) !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* Cambia todos los textos e iconos dentro del botón a azul oscuro */
    div[data-testid="stLinkButton"] a *,
    div[data-testid="stLinkButton"] button * {
        color: #07142b !important;
        fill: #07142b !important;
    }

    /* Estado Hover / Al pasar el mouse o tocar en móvil */
    div[data-testid="stLinkButton"] a:hover,
    div[data-testid="stLinkButton"] button:hover {
        background-color: #E2E8F0 !important;
        background: #E2E8F0 !important;
        border-color: #E2E8F0 !important;
        color: #0A1F44 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FUNCIÓN AUXILIAR: Obtiene la ruta de imagen o base64
# =========================================================
def obtener_src_imagen(ruta_local, url_respaldo):
    try:
        if os.path.exists(ruta_local):
            with open(ruta_local, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            extension = ruta_local.split(".")[-1].lower()
            mime_type = "image/jpeg" if extension in ["jpg", "jpeg"] else "image/png"
            return f"data:{mime_type};base64,{data}"
    except Exception:
        pass
    return url_respaldo


# --- Cargar logo en memoria ---
logo_src = obtener_src_imagen(LOGO_PATH, LOGO_FALLBACK_URL)


# =========================================================
# 1. CABECERA CON LOGO
# =========================================================
st.markdown(
    f"""
    <div class="pc-logo-wrap">
        <img src="{logo_src}" alt="PostCargo">
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# =========================================================
# 2. BOTONES DESTACADOS (NEGOCIOS Y PRESENTACIÓN)
# =========================================================
# Botón Principal: Negocios
st.link_button("💼 Negocios", NEGOCIOS_URL, use_container_width=True)

st.write("")

# Botón Secundario: Presentación Corporativa
st.link_button("🎥 Presentación Corporativa", VIDEO_URL, use_container_width=True)

st.write("")

# Texto del tagline y servicios
st.markdown(f"<p class='pc-tagline'>“{TAGLINE}”</p>", unsafe_allow_html=True)

st.markdown(
    """
    <p class="pc-servicios">📦 Paqueteo de Trayecto Especial &nbsp;·&nbsp; ⚙️ Operaciones Especiales &nbsp;·&nbsp; 🚚 Ultima Milla Regional</p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# =========================================================
# 3. DATOS DE CONTACTO
# =========================================================
st.markdown("<p class='pc-section-title'>Contacto</p>", unsafe_allow_html=True)

st.markdown(
    f"""
    <p class="pc-contact-item">📧&nbsp;&nbsp;E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="pc-contact-item">📱&nbsp;&nbsp;Cel: <a href="tel:{CEL_LINK}">{CEL_TEXTO}</a></p>
    <p class="pc-contact-item">☎️&nbsp;&nbsp;Tel: <a href="tel:{TEL_LINK}">{TEL_TEXTO}</a></p>
    <p class="pc-contact-item">🏙️&nbsp;&nbsp;Bogotá - Colombia</p>
    """,
    unsafe_allow_html=True,
)

st.write("")

st.link_button("🌐 www.postcargo.co", WEB_URL, use_container_width=True)
st.write("")

st.link_button(f"📍 {DIRECCION}", MAPS_URL, use_container_width=True)

st.divider()

# =========================================================
# 4. CIERRE
# =========================================================
st.info("🌎 **Cobertura Nacional**")

st.markdown("<p class='pc-footer-note'>PostCargo S.A.S</p>", unsafe_allow_html=True)
