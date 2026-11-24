if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.stop()
import streamlit as st

st.title("Submit a Complaint")

st.write("Please provide the details of your complaint.")

with st.form("complaint_form"):

    category = st.selectbox(
        "Complaint Category",
        [
            "Hostel",
            "Internet",
            "Infrastructure",
            "Transport",
            "Academic",
            "Other"
        ]
    )

    subject = st.text_input(
        "Complaint Subject"
    )

    description = st.text_area(
        "Describe your complaint",
        height=150
    )

    priority = st.radio(
        "Priority",
        ["Low", "Medium", "High"],
        horizontal=True
    )

    submitted = st.form_submit_button(
        "Submit Complaint"
    )
if submitted:
    if not subject.strip():
        st.error("Subject is required.")
    elif not description.strip():
        st.error("Description is required.")
    else:
        complaint = {
            "ID": len(st.session_state.complaints) + 1,
            "Category": category,
            "Subject": subject,
            "Description": description,
            "Priority": priority,
            "Status": "Pending"
        }
        st.session_state.complaints.append(complaint)
        st.success("Complaint submitted successfully!")