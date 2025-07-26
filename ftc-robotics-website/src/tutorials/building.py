import streamlit as st

st.set_page_config(page_title="FTC Robotics - Building Tutorial", page_icon="🤖", layout="centered")

st.title("Building Your FTC Robot")

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