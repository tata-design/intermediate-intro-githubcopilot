import streamlit as st

st.set_page_config(page_title="About Us - Community Health Access", page_icon="🩺", layout="centered")

st.title("About Us")

st.markdown(
    """
    <div style='background: linear-gradient(90deg, #e6f9f8 0%, #fafdff 100%); border-radius: 14px; padding: 22px; margin-bottom: 22px; border: 2px solid #20b2aa; color: #184d4d; font-size: 1.12em; box-shadow: 0 2px 12px rgba(32,178,170,0.07);'>
    <b>Our Mission</b><br>
    Community Health Access is a non-profit organization dedicated to bridging the gap between modern healthcare and accessibility. We serve underserved communities by providing free virtual doctor appointments and access to comprehensive medical databases. Our mission is to support and uplift the community, ensuring everyone has access to quality medical care, regardless of cost or location.<br><br>
    <b>What We Do</b><br>
    - Free virtual doctor appointments<br>
    - Access to trusted medical resources<br>
    - Community support and outreach<br><br>
    <b>Our Values</b><br>
    Compassion, Equity, Accessibility, and Empowerment
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<a href="/workspaces/intermediate-intro-githubcopilot/home.py" style="color:#168c8c; font-weight:600;">← Back to Home</a>
""", unsafe_allow_html=True)
