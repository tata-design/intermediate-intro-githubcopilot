import streamlit as st

st.set_page_config(page_title="CAD Tutorial for FTC Robotics", page_icon="🤖", layout="centered")

st.markdown(
    """
    <div class='info-box'>
    <b>Introduction to CAD</b><br>
    Computer-Aided Design (CAD) software is essential for designing robot parts in FTC Robotics. This tutorial will guide you through the basics of using CAD software effectively.
    </div>
    """,
    unsafe_allow_html=True
)

st.header("Getting Started with CAD")

# Add an educational video
st.subheader("📹 CAD Tutorial Video")
st.markdown(
    """
    Watch this comprehensive tutorial to get started with CAD for FTC Robotics:
    """
)

# Embed the YouTube video you provided
st.video("https://www.youtube.com/watch?v=wS9xyiaxYZM&t=3s")

st.markdown(
    """
    CAD software allows you to create precise drawings and models of your robot components. Here are some popular CAD tools used in FTC Robotics:
    - **Fusion 360**: A powerful CAD tool that is free for students and educators.
    - **Tinkercad**: A user-friendly, web-based CAD tool suitable for beginners.
    - **SolidWorks**: A professional-grade CAD software often used in engineering.
    - **Onshape**: A cloud-based CAD platform that's free for public projects and offers real-time collaboration features.

    Choose a tool that fits your skill level and project requirements.
    """
)

st.header("Tips for Effective CAD Design")
st.markdown(
    """
    - **Start Simple**: Begin with basic shapes and gradually add complexity to your designs.
    - **Use Constraints**: Apply constraints to ensure parts fit together correctly.
    - **Plan Your Design**: Sketch your ideas on paper before starting in CAD to save time.
    - **Test Fit**: If possible, 3D print your designs to test their fit and functionality before finalizing.

    Remember, practice makes perfect! The more you use CAD software, the more proficient you'll become.
    """
)

st.header("Best Practices for 3D Modeling")
st.markdown(
    """
    - **Keep It Organized**: Use layers and groups to keep your design organized.
    - **Optimize for Printing**: If you plan to 3D print your designs, consider the printer's capabilities and limitations.
    - **Document Your Process**: Keep notes on your design decisions and iterations for future reference.

    By following these best practices, you'll create effective and efficient designs for your FTC robot.
    """
)

st.header("Resources for Learning CAD")
st.markdown(
    """
    Here are some resources to help you learn more about CAD:
    - [Fusion 360 Learning Resources](https://www.autodesk.com/products/fusion-360/learn-and-support)
    - [Tinkercad Tutorials](https://www.tinkercad.com/learn)
    - [SolidWorks Tutorials](https://www.solidworks.com/sw/resources/tutorials.htm)

    Explore these resources to enhance your CAD skills and improve your robot designs!
    """
)

# Call to action section
st.markdown("---")
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #1D63A8 0%, #0f4d8c 100%); 
               padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;
               box-shadow: 0 4px 15px rgba(29, 99, 168, 0.3);'>
    <h3 style='color: white; margin-bottom: 1rem;'>Ready to Start Your Robotics Journey? 🤖</h3>
    <p style='color: white; font-size: 1.1rem; margin-bottom: 1.5rem;'>
    Join our community and get access to comprehensive tutorials, expert guidance, and start building amazing robots today!
    </p>
    <p style='color: #FF8310; font-weight: bold; font-size: 1.2rem;'>
    Your next breakthrough is just one tutorial away! 💡
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add signup button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Join BotBuilders Hub", use_container_width=True, type="primary", key="cad_signup_btn"):
        st.switch_page("pages/signup.py")