import streamlit as st
from video import generate_video

st.title("🏁 World Cup Race Generator")

group = st.text_input("Group Name")

t1 = st.text_input("Team 1")
t2 = st.text_input("Team 2")
t3 = st.text_input("Team 3")
t4 = st.text_input("Team 4")

if st.button("Generate Video 🎬"):

    teams = [t1, t2, t3, t4]

    if "" in teams or group == "":
        st.error("Fill all fields")
    else:
        path = generate_video(group, teams)
        st.success("Done!")
        st.video(path)
