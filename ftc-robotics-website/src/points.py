# filepath: /ftc-robotics-website/ftc-robotics-website/src/points.py
import streamlit as st

st.title("FTC Robotics Points System")

st.markdown(
    """
    ## Points System Overview
    The points system in FTC Robotics competitions is designed to reward teams for completing various tasks and achieving specific goals during the match. Understanding how points are awarded is crucial for teams to strategize effectively.

    ## Points Breakdown
    Here is a detailed breakdown of how points are awarded in the competition:

    - **Autonomous Period (30 seconds)**:
        - Completing a specific task: **10 points**
        - Moving the robot to a designated area: **5 points**
        - Scoring in the autonomous zone: **15 points**

    - **Teleoperated Period (2 minutes)**:
        - Scoring points by placing game elements in scoring zones: **5 points each**
        - Completing specific tasks as outlined in the game manual: **10 points**
        - Assisting alliance partners: **3 points**

    - **Endgame (30 seconds)**:
        - Hanging from the structure: **20 points**
        - Completing a final task: **15 points**

    ## Strategy Tips
    - Focus on maximizing points during the autonomous period, as it can give your team a significant advantage.
    - Collaborate with alliance partners to achieve shared goals and maximize scoring opportunities.
    - Always refer to the official game manual for the most accurate and up-to-date points system information.

    ## Conclusion
    Understanding the points system is essential for developing effective strategies and ensuring your team can perform at its best during competitions. Good luck!
    """,
    unsafe_allow_html=True
)