if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.stop()
import streamlit as st
import pandas as pd

st.title("Dashboard")

st.write("Welcome to your Complaint Management Portal.")

# Sample data for frontend development
complaints = [
    {
        "ID": 101,
        "Subject": "Internet not working",
        "Category": "Internet",
        "Status": "Pending"
    },
    {
        "ID": 102,
        "Subject": "Water supply issue",
        "Category": "Hostel",
        "Status": "Resolved"
    },
    {
        "ID": 103,
        "Subject": "Classroom maintenance",
        "Category": "Infrastructure",
        "Status": "Pending"
    }
]

df = pd.DataFrame(complaints)

total = len(df)
pending = len(df[df["Status"] == "Pending"])
resolved = len(df[df["Status"] == "Resolved"])

# Dashboard cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Complaints", total)
col2.metric("Pending", pending)
col3.metric("Resolved", resolved)

st.divider()

st.subheader("Recent Complaints")

st.dataframe(df, use_container_width=True)
