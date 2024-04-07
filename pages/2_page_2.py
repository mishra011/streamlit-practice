import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)