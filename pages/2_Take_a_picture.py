import streamlit as st

st.markdown("# Take a picture ❄️")
st.sidebar.markdown("# Take a picture ❄️")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)