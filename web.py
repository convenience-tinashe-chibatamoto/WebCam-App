# Importing the necessary modules
import streamlit as st
from PIL import Image
st.subheader("Colour Image to Grayscale Simple Photo Editor")

with st.expander("Start camera"):
    #starting the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    img = Image.open(camera_image)
    #Converting the pillow image to grayscale
    gray_camera_img = img.convert('L')
    #Rendering the pillow image on the web page
    st.image(gray_camera_img)

# Adding a feature that allows users to upload an image from their computer files. Then, the app converts the uploaded image to grayscale and displays it.
uploaded_image = st.file_uploader("Upload Image")
# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)
