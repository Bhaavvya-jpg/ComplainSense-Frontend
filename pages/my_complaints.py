
import streamlit as st
import pandas as pd

st.title("My Complaints")

complaints = st.session_state.get("complaints", [])

if complaints:
    df = pd.DataFrame(complaints)
    st.dataframe(df, use_container_width=True)
else:
    st.info("You haven't submitted any complaints yet.")
import streamlit as st
import pandas as pd

st.title("My Complaints")

complaints = st.session_state.get("complaints", [])

if complaints:
    df = pd.DataFrame(complaints)
    
    st.subheader("Complaint History")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    selected_id = st.selectbox(
        "Select Complaint ID",
        df["ID"]
    )
else:
    st.info("You haven't submitted any complaints yet.")

selected = df[df["ID"] == selected_id].iloc[0]

st.subheader("Complaint Details")

st.write("Subject:", selected["Subject"])
st.write("Category:", selected["Category"])
st.write("Status:", selected["Status"])
