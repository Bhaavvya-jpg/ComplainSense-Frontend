import streamlit as st

if "complaints" not in st.session_state:
    st.session_state.complaints = []
import streamlit as st

st.set_page_config(
    page_title="Complaint Portal",
    page_icon="📋",
    layout="wide"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login page
if not st.session_state.logged_in:

    st.title("Complaint Management System")
    st.subheader("Login")

    email = st.text_input("Email Address")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if email.strip() and password:
            st.session_state.logged_in = True
            st.session_state.email = email
            st.rerun()

        else:
            st.error("Please enter your credentials.")

else:
    st.success("Welcome to the Complaint Portal!")
    st.write(f"Logged in as: {st.session_state.email}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
