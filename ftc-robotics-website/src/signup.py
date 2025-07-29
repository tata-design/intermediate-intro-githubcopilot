import streamlit as st

st.set_page_config(page_title="Sign Up - BotBuilders Hub", page_icon="🤖", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .signup-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    
    .signup-header {
        text-align: center;
        color: #1D63A8;
        margin-bottom: 2rem;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    .signup-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
        font-size: 1.2rem;
    }
    
    .form-section {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    
    .benefits-box {
        background: linear-gradient(135deg, #FF8310 0%, #ff6b10 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .success-message {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 1rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="signup-container">
        <h1 class="signup-header">🤖 Join BotBuilders Hub</h1>
        <p class="signup-subtitle">Start your robotics journey with us today!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Benefits section
st.markdown(
    """
    <div class="benefits-box">
        <h3 style="margin-top: 0;">What You'll Get:</h3>
        <ul style="margin: 0; padding-left: 1.5rem;">
            <li>🎯 Access to comprehensive FTC robotics tutorials</li>
            <li>💻 Step-by-step coding guides and examples</li>
            <li>🔧 Building tips and best practices</li>
            <li>📐 CAD design tutorials and resources</li>
            <li>📋 Latest FTC rules and competition updates</li>
            <li>🤝 Community support and mentorship</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Sign up form
st.markdown(
    """
    <div class="form-section">
        <h3 style="color: #1D63A8; margin-top: 0;">Sign Up Information</h3>
    </div>
    """,
    unsafe_allow_html=True
)

with st.form("signup_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("First Name *", placeholder="Enter your first name")
        email = st.text_input("Email Address *", placeholder="your.email@example.com")
        phone = st.text_input("Phone Number", placeholder="(555) 123-4567")
    
    with col2:
        last_name = st.text_input("Last Name *", placeholder="Enter your last name")
        school = st.text_input("School/Organization", placeholder="Your school or team name")
        grade = st.selectbox("Grade Level", ["Select Grade", "6th Grade", "7th Grade", "8th Grade", "9th Grade", "10th Grade", "11th Grade", "12th Grade", "College", "Mentor/Coach"])
    
    st.markdown("### Experience Level")
    experience = st.radio(
        "What's your robotics experience?",
        ["Complete Beginner", "Some Experience", "Intermediate", "Advanced"],
        horizontal=True
    )
    
    st.markdown("### Areas of Interest")
    col1, col2 = st.columns(2)
    
    with col1:
        building = st.checkbox("🔧 Robot Building & Design")
        coding = st.checkbox("💻 Programming & Code")
        cad = st.checkbox("📐 CAD & 3D Design")
    
    with col2:
        strategy = st.checkbox("🎯 Strategy & Game Analysis")
        competition = st.checkbox("🏆 Competition Preparation")
        mentoring = st.checkbox("🤝 Mentoring Others")
    
    goals = st.text_area("Goals & Expectations", placeholder="Tell us what you hope to achieve with robotics...")
    
    newsletter = st.checkbox("📧 Subscribe to our newsletter for updates and tips")
    terms = st.checkbox("I agree to the terms and conditions *")
    
    submitted = st.form_submit_button("🚀 Join BotBuilders Hub", use_container_width=True)
    
    if submitted:
        if not first_name or not last_name or not email or not terms:
            st.error("Please fill in all required fields (*) and accept the terms and conditions.")
        else:
            st.markdown(
                """
                <div class="success-message">
                    <h3 style="margin: 0;">🎉 Welcome to BotBuilders Hub!</h3>
                    <p style="margin: 0.5rem 0 0 0;">Thank you for joining us! Check your email for a welcome message with next steps.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # You could add actual form processing here
            # For now, we'll just show success message
            
            st.balloons()

# Additional resources section
st.markdown("---")

st.markdown(
    """
    <div class="form-section">
        <h3 style="color: #1D63A8; margin-top: 0;">🔗 Quick Start Resources</h3>
        <p>While you're here, check out these helpful resources to get started:</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("src/home.py")

with col2:
    if st.button("📋 FTC Rules", use_container_width=True):
        st.switch_page("src/rules.py")

with col3:
    if st.button("🎓 Tutorials", use_container_width=True):
        st.switch_page("src/home.py")

# Contact information
st.markdown(
    """
    <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-top: 2rem; text-align: center;">
        <h4 style="color: #1D63A8; margin-top: 0;">Need Help?</h4>
        <p style="margin: 0.5rem 0;">
            📧 Email us at: <strong>support@botbuildershub.com</strong><br>
            🤝 Join our Discord community for instant help and discussions
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
