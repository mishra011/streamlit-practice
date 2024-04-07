import streamlit as st

st.markdown("# Audio Recorder Page")
st.sidebar.markdown("# Audio Recorder Page 🎈")


from st_audiorec import st_audiorec

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')