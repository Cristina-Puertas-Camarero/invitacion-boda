import streamlit as st
from PIL import Image
import base64

# Configuración de la página
st.set_page_config(page_title="Invitación de Boda", layout="centered")

# Fondo negro carbón real + estilos
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a !important;
        padding: 0rem 1rem;
    }
    header, footer, .block-container {
        background-color: #1a1a1a !important;
    }
    body {
        background-color: #1a1a1a;
        color: #f5f5dc;
        font-family: 'Georgia', serif;
    }
    .title {
        text-align: center;
        font-size: 42px;
        margin-top: 20px;
        color: #f5f5dc;
        letter-spacing: 1px;
    }
    .subtitle {
        text-align: center;
        font-size: 32px;
        margin-bottom: 10px;
        color: #f5f5dc;
    }
    .ampersand {
        text-align: center;
        font-size: 28px;
        margin-bottom: 10px;
        color: #f5f5dc;
    }
    .quote {
        text-align: center;
        font-size: 20px;
        font-style: italic;
        margin-top: 30px;
        margin-bottom: 10px;
        color: #e0e0d0;
    }
    .quote-source {
        text-align: center;
        font-size: 16px;
        color: #c0c0b0;
        margin-bottom: 40px;
    }
    .details {
        text-align: center;
        font-size: 20px;
        margin-top: 40px;
        margin-bottom: 40px;
        color: #f5f5dc;
        line-height: 1.8;
    }
    .link {
        text-align: center;
        font-size: 18px;
        margin-top: 10px;
        margin-bottom: 40px;
        color: #f5f5dc;
    }
    .footer {
        text-align: center;
        font-size: 18px;
        margin-top: 60px;
        color: #d0d0c0;
        font-style: italic;
    }
    .confirm {
        text-align: center;
        font-size: 20px;
        margin-top: 60px;
        margin-bottom: 40px;
        color: #f5f5dc;
    }
    video {
        width: 100%;
        height: auto;
        max-height: 400px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# Música de fondo con mensaje
def embed_audio(file_path: str):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
            <div style='text-align:center; margin-top:20px;'>
                <p style='color:#f5f5dc;'>Sube el volumen y dale al play...</p>
                <audio controls autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                Tu navegador no soporta audio HTML5.
                </audio>
            </div>
            """
            st.markdown(md, unsafe_allow_html=True)
    except:
        st.warning("No se pudo cargar la canción 'Waitin' On A Sunny Day.mp3'.")

# Espacio visual
st.markdown("<br><br>", unsafe_allow_html=True)
embed_audio("Waitin' On A Sunny Day.mp3")
st.markdown("<br><br>", unsafe_allow_html=True)

# Frase Interestelar
st.markdown('<div class="quote">"El amor es lo único que somos capaces de percibir que trasciende las dimensiones del tiempo y el espacio."</div>', unsafe_allow_html=True)
st.markdown('<div class="quote-source">— Interestelar (Christopher Nolan, 2014)</div>', unsafe_allow_html=True)

# Espacio visual
st.markdown("<br><br>", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="title">¡NOS CASAMOS!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Mariola Tocino</div>', unsafe_allow_html=True)
st.markdown('<div class="ampersand">&</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Miguel Ángel Zarzuela</div>', unsafe_allow_html=True)

# Imagen
try:
    image = Image.open("Laura y Manu.jpeg")
    st.image(image, caption="Everything is illuminated", use_container_width=True)
except:
    st.warning("No se pudo cargar la imagen 'Laura y Manu.jpeg'.")

# Detalles del evento
st.markdown("""
    <div class="details">
        El próximo <strong>7 de noviembre de 2025</strong>, queremos compartir contigo un día que será inolvidable para nosotros.<br><br>
        La <strong>ceremonia</strong> tendrá lugar a las <strong>15:00h</strong> en el <strong>Restaurante Piparra</strong>,<br>
        un rincón especial en El Puerto de Santa María, cerca de casa, para celebrar el amor.<br><br>
        Tras el sí, brindaremos, comeremos y bailaremos juntos en el mismo lugar.<br>
        Será íntimo, será nuestro, y queremos que tú estés allí.
    </div>
""", unsafe_allow_html=True)

# Enlace al restaurante
st.markdown("""
    <div class="link">
        <a href="https://piparra.com" target="_blank" style="color:#f5f5dc;">Conoce el lugar: piparra.com</a>
    </div>
""", unsafe_allow_html=True)

# Espacio antes del vídeo
st.markdown("<br><br>", unsafe_allow_html=True)

# Vídeo embebido sin sonido ni controles (no interrumpe la música)
try:
    video_file = open("ScreenRecording_10-02-2025 16-51-33_1.mov", "rb")
    video_bytes = video_file.read()
    st.markdown("""
        <video autoplay muted loop playsinline style="width:100%; max-height:400px;">
            <source src="data:video/mp4;base64,{0}" type="video/mp4">
            Tu navegador no soporta vídeo HTML5.
        </video>
    """.format(base64.b64encode(video_bytes).decode()), unsafe_allow_html=True)
except:
    st.warning("No se pudo cargar el vídeo 'ScreenRecording_10-02-2025 16-51-33_1.mov'.")

st.markdown("""
    <div class="confirm">
        ¿Contamos contigo?<br><br>
        Confirma tu asistencia con un clic:
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style='text-align:center; margin-top:10px;'>
            <a href="https://wa.me/34620598397?text=Hola%20Mariola,%20confirmo%20mi%20asistencia%20a%20la%20boda!" target="_blank" style="color:#f5f5dc; font-size:18px; text-decoration:none; border:1px solid #f5f5dc; padding:8px 16px; border-radius:5px; display:inline-block;">
                Confirmar con Mariola
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align:center; margin-top:10px;'>
            <a href="https://wa.me/34669892187?text=Hola%20Miguel%20Ángel,%20confirmo%20mi%20asistencia%20a%20la%20boda!" target="_blank" style="color:#f5f5dc; font-size:18px; text-decoration:none; border:1px solid #f5f5dc; padding:8px 16px; border-radius:5px; display:inline-block;">
                Confirmar con Miguel Ángel
            </a>
        </div>
    """, unsafe_allow_html=True)






