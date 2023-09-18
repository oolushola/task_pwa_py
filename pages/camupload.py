import streamlit as st
from PIL import Image


def uploadImage(selectFile):
    image_select = Image.open(selectFile)
    image_upload_gray = image_select.convert("L")
    st.image(image_upload_gray)


selectFile = st.file_uploader("Choose a file")
print(selectFile)


with st.expander('Start Camera'):
    camera = st.camera_input("Camera")


if camera:
    img = Image.open(camera)
    gray_img = img.convert("P")
    st.image(gray_img)

    print(gray_img)

if selectFile:
    uploadImage(selectFile)
