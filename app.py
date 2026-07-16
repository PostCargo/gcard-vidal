import streamlit as st
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
# DATOS DE LA TARJETA (editar aquí si algo cambia)
# =========================================================
LOGO_PATH = "logo.png"
LOGO_FALLBACK_URL = "https://placehold.co/600x220/0A1F44/FFFFFF?text=PostCargo+SAS&font=raleway"

PERFIL_PATH = "vidal_urrego.jpeg"
PERFIL_FALLBACK_URL = "https://placehold.co/400x400/1E3A8A/FFFFFF?text=V.U.&font=raleway"

NOMBRE = "Vidal Urrego Silva"
CARGO = "Gerente General"
EMPRESA = "PostCargo SAS"
TAGLINE = "Operador Logístico Especializado en Reexpediciones"

VIDEO_URL = "https://drive.google.com/file/d/171UVVbs3kwxcek2YbAPnChCXT5H4LezN/view?usp=sharing"
MAPS_URL = "https://maps.app.goo.gl/ASSDb6szm8FLSJfZ7"
WEB_URL = "https://www.postcargo.co"

EMAIL = "vidal.urrego@postcargo.co"
CEL_TEXTO = "311 565 3897"
CEL_LINK = "+573115653897"
TEL_TEXTO = "(601) 300 1431"
TEL_LINK = "+576013001431"
DIRECCION = "Carrera 97 No. 24 C - 23 Bodega 10, Muelle Industrial 1 - Bogotá, Colombia"

# =========================================================
# ESTILOS (CSS mínimo: colores, tipografía, ocultar chrome de Streamlit)
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

    /* ---- Fondo corporativo azul oscuro / azul rey ---- */
    .stApp {
        background-color: #0A1F44;
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

    /* ---- Foto de perfil circular y elegante (Agrandada a 290px para impacto total) ---- */
    .pc-perfil-wrap img {
        width: 290px !important;
        height: 290px !important;
        object-fit: cover;
        border-radius: 50%;
        border: 4px solid #E5E7EB;
        box-shadow: 0 6px 18px rgba(0,0,0,0.4);
        display: block;
        margin: 0 auto;
    }

    /* ---- Bloques de texto centrados (nombre, cargo, tagline) ---- */
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
        margin: 2px 0 0 0;
    }
    .pc-empresa {
        text-align: center;
        color: #93A5C4;
        font-size: 14px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 4px 0 0 0;
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
    .pc-cobertura {
        text-align: center;
        color: #FFFFFF;
        font-weight: 600;
        font-size: 15px;
        margin: 0;
    }
    .pc-footer-note {
        text-align: center;
        color: #6B7A99;
        font-size: 12px;
        margin-top: 12px;
    }

    /* ---- Enlaces de texto (correo, teléfono) ---- */
    a {
        color: #9DC6FF !important;
        text-decoration: none !important;
        font-weight: 500;
    }
    a:hover {
        color: #FFFFFF !important;
    }

    /* ---- Botones nativos (st.link_button) ---- */
    div.stLinkButton > a {
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FUNCIÓN AUXILIAR: carga segura de imágenes con respaldo
# =========================================================
def mostrar_imagen_segura(ruta_local, url_respaldo, width=None, use_container_width=False, texto_marcador="PostCargo"):
    """
    Intenta mostrar una imagen local. Si no existe o falla,
    usa una imagen de respaldo desde internet. Si eso también
    falla (por ejemplo, sin conexión), muestra un marcador
    visual elegante para que la página nunca se vea rota.
    """
    try:
        if os.path.exists(ruta_local):
            st.image(ruta_local, width=width, use_container_width=use_container_width)
            return
    except Exception:
        pass

    try:
        st.image(url_respaldo, width=width, use_container_width=use_container_width)
        return
    except Exception:
        pass

    st.markdown(
        f"""
        <div style="background-color:#1E3A8A; color:#FFFFFF; text-align:center;
        padding:40px 20px; border-radius:14px; font-weight:700; font-size:18px;">
        {texto_marcador}
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 1. IDENTIDAD DE MARCA — LOGO (Reducido drásticamente con columnas [3.6, 0.8, 3.6])
# =========================================================
col_l1, col_l2, col_l3 = st.columns([3.6, 0.8, 3.6])
with col_l2:
    mostrar_imagen_segura(LOGO_PATH, LOGO_FALLBACK_URL, use_container_width=True, texto_marcador="PostCargo SAS")

st.write("")

# =========================================================
# 1B. FOTO DE PERFIL (Centrada perfectamente debajo del logo y agrandada a width=290)
# =========================================================
st.markdown('<div class="pc-perfil-wrap" style="display: flex; justify-content: center; width: 100%;">', unsafe_allow_html=True)
mostrar_imagen_segura(PERFIL_PATH, PERFIL_FALLBACK_URL, width=290, texto_marcador="V. Urrego")
st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 2. INFORMACIÓN DE DON VIDAL
# =========================================================
st.markdown(f"<p class='pc-nombre'>{NOMBRE}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='pc-cargo'>{CARGO}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='pc-empresa'>{EMPRESA}</p>", unsafe_allow_html=True)

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
