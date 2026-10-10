
import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Очистка печати", page_icon="🔮")
st.title("🔮 Очистка печати от фона")
st.write("Загрузите фотографию, и нейросеть полностью сотрет бумагу.")

uploaded_file = st.file_uploader("Выберите фото с печатью", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Исходное фото", use_container_width=True)
    
    with st.spinner("Нейросеть удаляет фон... Пожалуйста, подождите."):
        output = remove(image)
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
    st.image(output, caption="Результат (прозрачный PNG)", use_container_width=True)
    st.download_button(label="📥 Скачать очищенную печать", data=byte_im, file_name="stamp_clear.png", mime="image/png")
