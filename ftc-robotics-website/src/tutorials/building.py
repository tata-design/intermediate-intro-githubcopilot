import streamlit as st

st.set_page_config(page_title="FTC Robotics - Building Tutorial", page_icon="🤖", layout="centered")

st.markdown(
    """
    <div class='info-box'>
    <b>Welcome to the Building Tutorial!</b><br>
    In this section, we will guide you through the process of assembling your FTC robot. Building a robot involves understanding the components, ensuring structural integrity, and using the right materials. Follow the guidelines below to create a robust and efficient robot.
    </div>
    """,
    unsafe_allow_html=True
)

st.header("1. Understanding Robot Components")

# Add an educational video
st.subheader("📹 Building Tutorial Video")
st.markdown(
    """
    Watch this comprehensive tutorial to get started with building your FTC robot:
    """
)

# Embed the YouTube video
st.video("https://www.youtube.com/watch?v=TmUSGWCiLlU")

st.markdown(
    """
    Your robot will consist of various components, including:
    - **Chassis**: The base structure of your robot.
    - **Motors**: Used for movement.
    - **Sensors**: For detecting the environment.
    - **Controllers**: To manage the robot's functions.
    - **Wiring**: To connect all components.
    """
)

st.header("2. Assembly Guidelines")
st.markdown(
    """
    - **Start with the Chassis**: Ensure it is sturdy and can support all other components.
    - **Secure Motors Properly**: Use screws and brackets to attach motors to the chassis.
    - **Organize Wiring**: Keep wires tidy to avoid tangling and interference with moving parts.
    - **Test Stability**: After assembly, check for any loose parts or instability.
    """
)

st.header("3. Tips for Structural Integrity")
st.markdown(
    """
    - Use lightweight materials to reduce the overall weight of the robot.
    - Reinforce joints with additional brackets or supports.
    - Ensure that the center of gravity is low to prevent tipping.
    """
)

st.header("4. Recommended Materials")
st.markdown(
    """
    - **Aluminum**: Lightweight and strong, ideal for the chassis.
    - **Plastic**: Good for non-load bearing parts.
    - **Wood**: Can be used for prototyping but may not be as durable.
    """
)

st.header("5. Additional Resources")
st.markdown(
    """
    - [FTC Robotics Official Website](https://www.firstinspires.org/robotics/ftc)
    - [Building Tips and Tricks](https://www.ftcforum.us/)
    """
)

st.info("Happy building! Remember, teamwork and creativity are key to a successful FTC robot.")

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
    if st.button("🚀 Join BotBuilders Hub", use_container_width=True, type="primary", key="building_signup_btn"):
        st.switch_page("pages/signup.py")