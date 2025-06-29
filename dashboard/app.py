import streamlit as st
import requests

st.set_page_config(page_title="Risk Profile Classifier")
st.title("🌐 Interactive Risk Profiler")

if "current" not in st.session_state:
    st.session_state.current = None

if "answers" not in st.session_state:
    st.session_state.answers = []

# Only get the first question when user clicks "Start Quiz"
if st.button("Start Quiz"):
    try:
        res = requests.get("http://localhost:8000/question")
        if res.status_code == 200:
            st.session_state.current = res.json()
            st.session_state.answers = []
        else:
            st.error(f"Server error: {res.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to server: {e}")
        st.info("Make sure the FastAPI server is running on http://localhost:8000")

if st.session_state.current:
    q = st.session_state.current
    st.write("**" + q["question"] + "**")
    selected = st.radio("Choose one:", q["options"])
    if st.button("Next"):
        try:
            response = requests.post("http://localhost:8000/answer", json={"answer": selected})
            if response.status_code == 200:
                response_data = response.json()
                if "classification" in response_data:
                    st.write("### 🏆 Your Risk Profile:", response_data["classification"])
                    st.session_state.current = None
                else:
                    st.session_state.current = response_data
            else:
                st.error(f"Server error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to server: {e}")
        except requests.exceptions.JSONDecodeError as e:
            st.error(f"Invalid response from server: {e}")