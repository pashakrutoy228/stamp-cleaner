import streamlit as st
from rembg import remove
from PIL import Image
import io

# Настройка страницы
st.set_page_config(page_title="Очистка печати", layout="centered")

st.title("🔮 Очистка печати от фона")
st.write("Загрузите фотографию, чтобы полностью удалить бумагу и оставить только оттиск.")

# Стандартная кнопка загрузки
uploaded_file = st.file_uploader("Выберите файл изображения (JPG или PNG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Открываем картинку
    image = Image.open(uploaded_file)
    st.image(image, caption="Исходное фото")
    
    # Запускаем обработку нейросетью прямо внутри сервера
    with st.spinner("Нейросеть удаляет фон... Пожалуйста, подождите."):
        output = remove(image)
        
        # Переводим в байты для кнопки скачивания
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
    st.image(output, caption="Результат без фона")
    st.download_button(
        label="📥 Скачать печать в PNG", 
        data=byte_im, 
        file_name="stamp_clear.png", 
        mime="image/png"
    )
