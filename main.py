import streamlit as st
from clarifai.client.model import Model
import base64
from dotenv import load_dotenv
from PIL import  Image
from io import BytesIO
load_dotenv()
import os
from generate_image import generate_image
from understand_image import understand_image
from text_to_speech import text_to_speech
from understand_image import encode_image

clarifai_pat = os.getenv("CLARIFAI_PAT")
openai_api_key = os.getenv("OPEN_AI")

def main():
    st.set_page_config(page_title="Interactive Media Creator", layout="wide")
    st.title("Let's cook anon")

    with st.sidebar:
        st.header("Controls")
        image_description = st.text_area("Description for Image Generation", height=100)
        generate_image_btn = st.button("Generate Image")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Comic Art")
        if generate_image_btn and image_description:
            with st.spinner("Generating image..."):
                image_path = generate_image(image_description, clarifai_pat)
                if image_path:
                    st.image(
                        image_path,
                        caption="Generated Comic Image",
                        use_column_width=True,
                    )
                    st.success("Image generated!")
                else:
                    st.error("Failed to generate image.")

    with col2:
        st.header("Story")
        if generate_image_btn and image_description:
            with st.spinner("Creating a story..."):
                base64_image = encode_image(image_path)
                understood_text = understand_image(base64_image, openai_api_key)
                audio_base64 = text_to_speech(understood_text, openai_api_key)
                st.audio(audio_base64, format="audio/mp3")
                st.success("Audio generated from image understanding!")
                
                
if __name__ == "__main__":
    main()
