import streamlit as st

st.set_page_config(page_title="Community Health Access", page_icon="🩺", layout="centered")

# Custom CSS for a modern teal and white look with a navigation header
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #fafdff;
        color: #184d4d;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    .nav-header {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 36px;
        background: linear-gradient(90deg, #20b2aa 0%, #43e0c6 100%);
        padding: 18px 0 10px 0;
        border-radius: 0 0 18px 18px;
        margin-bottom: 32px;
        box-shadow: 0 2px 12px rgba(32,178,170,0.07);
    }
    .nav-link {
        color: #fff !important;
        font-size: 1.1em;
        font-weight: 600;
        text-decoration: none;
        padding: 6px 18px;
        border-radius: 8px;
        transition: background 0.2s, color 0.2s;
    }
    .nav-link:hover {
        background: #e6f9f8;
        color: #168c8c !important;
        text-decoration: none;
    }
    .stApp, .stMarkdown, .stTextInput, .stTextArea, .stDateInput, .stTimeInput, .stInfo, .info-box {
        color: #184d4d !important;
    }
    .stButton > button {
        background: linear-gradient(90deg, #20b2aa 0%, #43e0c6 100%);
        color: white;
        border-radius: 12px;
        font-size: 18px;
        border: none;
        padding: 12px 28px;
        box-shadow: 0 2px 8px rgba(32,178,170,0.08);
        transition: 0.2s;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #168c8c 0%, #20b2aa 100%);
        color: #fff;
        box-shadow: 0 4px 16px rgba(32,178,170,0.15);
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #168c8c;
        font-weight: 700;
    }
    label {
        color: #168c8c !important;
        font-weight: 600;
    }
    .info-box {
        background: linear-gradient(90deg, #e6f9f8 0%, #fafdff 100%);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 22px;
        border: 2px solid #20b2aa;
        color: #184d4d !important;
        font-size: 1.12em;
        box-shadow: 0 2px 12px rgba(32,178,170,0.07);
    }
    .modern-card {
        background: #fff;
        border-radius: 14px;
        box-shadow: 0 2px 12px rgba(32,178,170,0.07);
        padding: 24px 28px;
        margin-bottom: 28px;
        border-left: 6px solid #20b2aa;
    }
    .modern-link a {
        color: #168c8c;
        font-weight: 600;
        text-decoration: none;
        transition: color 0.2s;
    }
    .modern-link a:hover {
        color: #43e0c6;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Website navigation header
st.markdown(
    """
    <div class='nav-header'>
        <a class='nav-link' href='#about-us'>About Us</a>
        <a class='nav-link' href='#appointments'>Appointments</a>
        <a class='nav-link' href='#database'>Database</a>
        <a class='nav-link' href='#contact-us'>Contact Us</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🩺 Community Health Access Portal")

st.markdown(
    """
    <div class='info-box' id='about-us'>
    <b>Our Mission</b><br>
    Our product serves as a vital bridge between modern healthcare and accessibility. Designed specifically for underserved communities, our website enables users to schedule virtual doctor appointments and access comprehensive medical databases—completely free of charge. As a non-profit organization, our sole mission is to support and uplift the community. The foundation of our idea is simple yet powerful: everyone deserves access to quality medical care, regardless of cost or location.
    </div>
    """,
    unsafe_allow_html=True
)

st.header("Schedule a Virtual Doctor Appointment", anchor="appointments")
with st.form("appointment_form"):
    with st.container():
        st.markdown("<div class='modern-card'>", unsafe_allow_html=True)
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        date = st.date_input("Preferred Date")
        time = st.time_input("Preferred Time", format="%I:%M %p")
        reason = st.text_area("Reason for Visit")
        submit_appointment = st.form_submit_button("Book Appointment")
        st.markdown("</div>", unsafe_allow_html=True)
    if submit_appointment:
        st.success(f"Appointment requested for {name} on {date} at {time}. We will contact you at {email}.")
        st.balloons()

st.header("Free Medical Database Access", anchor="database")
st.write("Browse trusted resources and information on health topics, conditions, and treatments.")

st.markdown("""
<div class='modern-card modern-link'>
- [MedlinePlus](https://medlineplus.gov/) – Trusted health information for all<br>
- [CDC Health Topics](https://www.cdc.gov/health-topics/) – U.S. Centers for Disease Control<br>
- [World Health Organization](https://www.who.int/health-topics) – Global health topics
</div>
""", unsafe_allow_html=True)

st.header("Contact Us", anchor="contact-us")
st.markdown(
    """
    <div class='modern-card'>
    <b>Email:</b> <a href='mailto:info@communityhealth.org' style='color:#168c8c;'>info@communityhealth.org</a><br>
    <b>Phone:</b> (800) 555-1234<br>
    <b>Address:</b> 123 Health Lane, Care City, USA
    </div>
    """,
    unsafe_allow_html=True
)

st.info("All services are 100% free. No insurance or payment required.")

st.markdown(
    """
    <div style='margin-top:40px; text-align:center;'>
        <span style='color:#168c8c; font-size:1.1em; font-style:italic;'>
            "Of all the forms of inequality, injustice in health is the most shocking and inhuman."<br>
            <b>– Dr. Martin Luther King Jr.</b>
        </span>
    </div>
    """,
    unsafe_allow_html=True
)