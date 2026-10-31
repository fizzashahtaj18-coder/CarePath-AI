"""CarePath AI: app skeleton (CPA-14).

Placeholder page only. The real screens are built in Sprints 1-4
(see docs/06-agile/agile-and-jira-guide.md).

Run locally:  streamlit run app/streamlit_app.py
"""
import streamlit as st

st.set_page_config(page_title="CarePath AI", page_icon=None, layout="centered")

st.title("CarePath AI")
st.caption(
    "Helps you organize appointment instructions. It does not give medical advice."
)
st.info(
    "Prototype under construction. This portfolio project uses synthetic data only. "
    "It is not HIPAA compliant and not clinically validated."
)

st.markdown(
    "**Coming in Sprint 1:** paste your appointment instructions and get a draft "
    "checklist where every item shows its source."
)
