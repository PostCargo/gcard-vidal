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
