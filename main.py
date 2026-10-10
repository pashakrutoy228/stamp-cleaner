import streamlit as st
from rembg import remove
from PIL import Image
import io

# Принудительно задаем светлую тему оформления
st.set_page_config(page_title="Очистка печати", page_icon="🔮", layout="centered")

# Внедряем CSS-стили, чтобы победить черный экран
st.markdown("""
    <style>
    /* Делаем главный фон белым, а текст темным */
    .stApp {
        background-color: #ffffff !important;
        color: #111111 !important;
    }
    /* Делаем зону загрузки файлов ярко-серой с рамкой */
    .stFileUploader {
        background-color: #f0f2f6 !important;
        border: 2px dashed #007BFF !important;
        padding: 20px !important;
        border-radius: 10px !important;
    }
    /* Перекрашиваем все тексты и заголовки в черный цвет */
    h1, h2, h3, p, label, span {
        color: #111111 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔮 Очистка печати от фона")
st.write("Загрузите фотографию, чтобы удалить бумагу и оставить только оттиск печати.")

# Кнопка загрузки файла
uploaded_file = st.file_uploader("Выберите файл изображения (JPG или PNG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Исходное фото")
    
    with st.spinner("Нейросеть удаляет фон... Пожалуйста, подождите."):
        output = remove(image)
        
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
    st.image(output, caption="Результат без фона")
    st.download_button(label="📥 Скачать печать в PNG", data=byte_im, file_name="stamp_clear.png", mime="image/png")
