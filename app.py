import streamlit as st
import base64
import os

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="Vidal Urrego Silva | PostCargo SAS",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================================
# DATOS DE LA TARJETA
# =========================================================
LOGO_PATH = "logo.jpeg"
LOGO_FALLBACK_URL = "https://placehold.co/600x220/0A1F44/FFFFFF?text=PostCargo+SAS&font=raleway"

PERFIL_PATH = "vidal_urrego.jpeg"
PERFIL_FALLBACK_URL = "https://placehold.co/400x400/1E3A8A/FFFFFF?text=V.U.&font=raleway"

NOMBRE = "Vidal Urrego Silva"
CARGO = "Gerente General"
TAGLINE = "Operador Logístico Especializado en Reexpediciones"

VIDEO_URL = "https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing"
MAPS_URL = "https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7"
WEB_URL = "https://www.postcargo.co"

EMAIL = "vidal.urrego@postcargo.co"
CEL_TEXTO = "311 565 3897"
CEL_LINK = "+573115653897"
TEL_TEXTO = "(601)805 2591"
TEL_LINK = "+576013001431"
DIRECCION = "Carrera 97 No. 24 C - 23 Bodega 10, Muelle Industrial 1 - Bogotá, Colombia"

# =========================================================
# ESTILOS (CSS mínimo con Degradado Diagonal Corporativo)
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

    /* ---- Contenedor para centrar la foto de perfil ---- */
    .pc-perfil-wrap {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* ---- Foto de perfil circular y centrada ---- */
    .pc-perfil-wrap img {
        width: 260px !important;
        height: 260px !important;
        object-fit: cover !important;
        border-radius: 50% !important;
        border: 4px solid #E5E7EB !important;
        box-shadow: 0 6px 18px rgba(0,0,0,0.4) !important;
        display: block !important;
    }

    /* ---- Contenedor para centrar el logo corporativo ---- */
    .pc-logo-wrap {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin-top: 5px;
        margin-bottom: 5px;
    }

    /* ---- Logo corporativo súper pequeño ---- */
    .pc-logo-wrap img {
        max-width: 90px !important;
        height: auto !important;
        display: block !important;
    }

    /* ---- Bloques de texto centrados ---- */
    .pc-nombre {
        text-align: center;
        color: #FFFFFF;
        font-size: 26px;
        font-weight: 700;
        margin: 14px 0 0 0;
    }
    .pc-cargo {
        text-align: center;
        color: #D8DEE9;
        font-size: 17px;
        font-weight: 500;
        margin: 2px 0 10px 0;
    }
    .pc-tagline {
        text-align: center;
        color: #E5E7EB;
        font-style: italic;
        font-size: 15px;
        padding: 0 6px;
        margin: 0;
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
    .pc-section-title {
        color: #93A5C4;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
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

    /* ---- Botones ---- */
    div.stLinkButton > a {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background-color: rgba(255,255,255,0.08) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }
    div.stLinkButton > a:hover {
        background-color: rgba(255,255,255,0.15) !important;
        border-color: rgba(255,255,255,0.4) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FUNCIÓN AUXILIAR: Obtiene la ruta de imagen o base64
# =========================================================
def obtener_src_imagen(ruta_local, url_respaldo):
    """
    Intenta leer el archivo local y codificarlo en Base64 para cargarlo de forma
    segura y rápida sin depender de rutas rotas en el servidor.
    Si falla, retorna la URL de respaldo.
    """
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


# --- Cargar imágenes en memoria ---
foto_src = obtener_src_imagen(PERFIL_PATH, PERFIL_FALLBACK_URL)
logo_src = obtener_src_imagen(LOGO_PATH, LOGO_FALLBACK_URL)


# =========================================================
# 1. FOTO DE PERFIL — CABECERA (Centrado Absoluto Asegurado)
# =========================================================
st.markdown(
    f"""
    <div class="pc-perfil-wrap">
        <img src="{foto_src}" alt="Vidal Urrego Silva">
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 2. INFORMACIÓN DE DON VIDAL & LOGO DEBAJO DE SU CARGO
# =========================================================
st.markdown(f"<p class='pc-nombre'>{NOMBRE}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='pc-cargo'>{CARGO}</p>", unsafe_allow_html=True)

# Logo corporativo súper pequeño y perfectamente centrado abajo de "Gerente General"
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
# 3. INFORMACIÓN CORPORATIVA
# =========================================================
st.markdown(f"<p class='pc-tagline'>“{TAGLINE}”</p>", unsafe_allow_html=True)

st.markdown(
    """
    <p class="pc-servicios">📦 Paqueteo &nbsp;·&nbsp; 🚚 Mensajería &nbsp;·&nbsp; ⚙️ Operaciones Especiales</p>
    """,
    unsafe_allow_html=True,
)

st.write("")

col_v1, col_v2, col_v3 = st.columns([1, 4, 1])
with col_v2:
    st.link_button("🎥 Más Información (Video)", VIDEO_URL, use_container_width=True)

st.divider()

# =========================================================
# 4. DATOS DE CONTACTO
# =========================================================
st.markdown("<p class='pc-section-title'>Contacto</p>", unsafe_allow_html=True)

st.markdown(f"📧&nbsp;&nbsp;[{EMAIL}](mailto:{EMAIL})")
st.markdown(f"📱&nbsp;&nbsp;Cel: [{CEL_TEXTO}](tel:{CEL_LINK})")
st.markdown(f"☎️&nbsp;&nbsp;Tel: [{TEL_TEXTO}](tel:{TEL_LINK})")
st.markdown("🏙️&nbsp;&nbsp;Bogotá - Colombia")

st.write("")

st.link_button(f"📍 {DIRECCION}", MAPS_URL, use_container_width=True)

st.divider()

# =========================================================
# 5. CIERRE
# =========================================================
st.info("🌎 **Cobertura Nacional e Internacional**")

col_w1, col_w2, col_w3 = st.columns([1, 3, 1])
with col_w2:
    st.link_button("🌐 www.postcargo.co", WEB_URL, use_container_width=True)

st.markdown("<p class='pc-footer-note'>PostCargo SAS</p>", unsafe_allow_html=True)
