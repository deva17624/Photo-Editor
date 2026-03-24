import streamlit  as st
import cv2
import io
import numpy as np
from  PIL import Image 


st.title("Welocme to Photo Editor")

st.subheader("Upload Image")

uploaded_img=st.file_uploader("",type=["png","jpg","jpeg"])

if uploaded_img is not None:
    image=Image.open(uploaded_img)
    img=np.array(image)
    st.subheader("Your Image")
    st.image(img)

    st.subheader("Resize Image")
    width = st.slider("Width", 100, img.shape[1]+1000, img.shape[1])
    height = st.slider("Height", 100, img.shape[0]+1000, img.shape[0])
    img = cv2.resize(img, (width, height))
    st.image(img)
    
    st.subheader("Brightness and contrast Adjustment")
    brightness=st.slider("Brightness",-100,100,0)
    contrast=st.slider("Contrast",0,5,1)
    img=cv2.convertScaleAbs(img,alpha=contrast,beta=brightness)
    st.image(img)

    st.subheader("Grey Scale")
    if st.checkbox("Greyscale"):
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    st.image(img)

    st.subheader("Blur Effect")
    blur=st.slider("Blur",1,20,1,step=2)
    img=cv2.GaussianBlur(img,(blur,blur),0)
    st.image(img)


    st.subheader("Warm Effect")
    if st.checkbox("Warm Effect"):
        kernel=np.array([10,20,30],dtype="int8")
        img=cv2.add(img,kernel)
    st.image(img)


    st.subheader("Shaper effect")
    if st.checkbox("Sharpen"):
        kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        img=cv2.filter2D(img,-1,kernel)
    st.image(img)

    st.subheader("Edge Dection ")
    if st.checkbox("Edge Detection"):
        img=cv2.Canny(img,100,200)
    st.image(img)

    st.subheader("Sketch type")
    if st.checkbox("Sketch"):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        inv=255 -gray
        blur=cv2.GaussianBlur(inv,(21,21),0)
        img=cv2.divide(gray,255-blur,scale=256)
    st.image(img)


    st.subheader("Dowmload a image")
    buf=io.BytesIO()
    Image.fromarray(img).save(buf,format="PNG")
    st.download_button(label="Download Image",data=buf.getvalue(),file_name="Edited_image.png",)
    









