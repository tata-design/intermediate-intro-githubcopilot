import streamlit as st

def show_rules():
    """Display the comprehensive FTC Rules and Competition Guide"""
    
    st.header("📜 FTC Robotics Competition Rules & Guidelines")
    
    # Introduction section with modern styling
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #004080; margin-bottom: 2rem;'>
        <b>Master the Rules, Win the Game!</b><br>
        Understanding FTC competition rules is crucial for success. This comprehensive guide covers everything 
        from team requirements to game-specific regulations that will help your team compete effectively and safely.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Video tutorial at the beginning
    st.subheader("🎥 FTC Rules Overview Video")
    st.markdown("Watch this essential video to understand the fundamentals of FTC competition rules:")
    
    # Embed the YouTube video
    st.video("https://www.youtube.com/watch?v=gy6nh_1mA18")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Competition Structure section with colorful styling
    st.subheader("🏆 Competition Structure")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #FF8310; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #FF8310; margin-bottom: 1rem;'>🎮 Game Phases</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            <b>Autonomous Period (30 seconds):</b><br>
            Robots operate independently using pre-programmed instructions<br><br>
            <b>Driver-Controlled Period (2 minutes):</b><br>
            Teams control robots using gamepads to complete objectives<br><br>
            <b>End Game (30 seconds):</b><br>
            Final phase with special scoring opportunities
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #1D63A8; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #1D63A8; margin-bottom: 1rem;'>🏅 Tournament Format</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            <b>Qualification Matches:</b><br>
            Random alliance matches to determine rankings<br><br>
            <b>Alliance Selection:</b><br>
            Top teams choose partners for elimination rounds<br><br>
            <b>Elimination Matches:</b><br>
            Single-elimination tournament to crown champions
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Team Requirements section
    st.subheader("👥 Team Requirements & Eligibility")
    
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #fff8e1 0%, #ffe4b5 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #FF8310; margin-bottom: 2rem;'>
        <h4 style='color: #FF8310; margin-bottom: 1rem;'>📋 Essential Team Information</h4>
        <div style='font-size: 1rem; line-height: 1.6;'>
        <b>Team Size:</b> Minimum 2 members, maximum 15 members per team<br>
        <b>Age Requirements:</b> Students in grades 7-12 (ages 12-18)<br>
        <b>Adult Mentors:</b> Required for guidance and safety oversight<br>
        <b>Registration:</b> Teams must register annually through FIRST<br>
        <b>Roles:</b> Drive team (2 drivers + 1 coach), pit crew, scouts, and programmers
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Robot Specifications section
    st.subheader("🤖 Robot Design Rules & Specifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #28a745; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #28a745; margin-bottom: 1rem;'>📏 Size & Weight Limits</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            <b>Starting Configuration:</b><br>
            • Maximum: 18" x 18" x 18" (45.7cm cube)<br>
            • Weight limit: 42 pounds (19.1 kg)<br><br>
            <b>Expansion Rules:</b><br>
            • Can expand during match<br>
            • No height restrictions during play<br>
            • Must fit in starting configuration
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #dc3545; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #dc3545; margin-bottom: 1rem;'>⚡ Power & Control Systems</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            <b>Control Hub:</b> REV Robotics Control Hub required<br>
            <b>Motors:</b> Maximum 8 motors (specific approved models)<br>
            <b>Servos:</b> Maximum 12 servos total<br>
            <b>Sensors:</b> Unlimited approved sensors allowed<br>
            <b>Battery:</b> One 12V REV battery maximum
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Safety Guidelines section
    st.subheader("🛡️ Safety Guidelines & Regulations")
    
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #ffe6e6 0%, #ffcccc 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #dc3545; margin-bottom: 2rem;'>
        <h4 style='color: #dc3545; margin-bottom: 1rem;'>⚠️ Critical Safety Requirements</h4>
        <div style='font-size: 1rem; line-height: 1.6;'>
        <b>Eye Protection:</b> Safety glasses required in pit area and during robot testing<br>
        <b>Emergency Stop:</b> All robots must have accessible emergency stop capability<br>
        <b>Sharp Edges:</b> No exposed sharp edges or pinch points allowed<br>
        <b>Electrical Safety:</b> All wiring must be properly secured and insulated<br>
        <b>Inspection:</b> All robots must pass safety inspection before competing
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Game Rules section
    st.subheader("🎯 General Game Rules")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #6f42c1; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #6f42c1; margin-bottom: 1rem;'>📜 Core Regulations</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            • Robots must use only approved materials<br>
            • No projectiles or liquids allowed<br>
            • Gracious professionalism expected<br>
            • Referees' decisions are final<br>
            • Teams must follow field reset procedures<br>
            • Fair play and sportsmanship required
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #fd7e14; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #fd7e14; margin-bottom: 1rem;'>🚫 Common Violations</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            • Interfering with opponent's robot<br>
            • Exceeding size limits during inspection<br>
            • Using prohibited materials or components<br>
            • Unsafe robot operation<br>
            • Disrespectful behavior<br>
            • Late for matches or inspection
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Penalties section
    st.subheader("⚖️ Penalties & Consequences")
    
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #ffc107; margin-bottom: 2rem;'>
        <h4 style='color: #856404; margin-bottom: 1rem;'>📊 Penalty System</h4>
        <div style='font-size: 1rem; line-height: 1.6;'>
        <b>Minor Penalties:</b> 10-30 point deductions for rule violations<br>
        <b>Major Penalties:</b> 40+ point deductions for serious infractions<br>
        <b>Yellow Card:</b> Warning for unsportsmanlike conduct<br>
        <b>Red Card:</b> Team disqualification from current match<br>
        <b>Disabled:</b> Robot disabled for unsafe operation
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Resources section
    st.subheader("📚 Official Resources & Documentation")
    
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #004080; margin-bottom: 2rem;'>
        <h4 style='color: #004080; margin-bottom: 1rem;'>🔗 Essential Links</h4>
        <div style='font-size: 1rem; line-height: 1.8;'>
        • <strong>Official Game Manual:</strong> <a href="https://www.firstinspires.org/resource-library/ftc/game-and-season-info" target="_blank" style="color: #004080;">Current Season Rules</a><br>
        • <strong>Robot Inspection Checklist:</strong> <a href="https://www.firstinspires.org/resource-library/ftc/robot-inspection-checklist" target="_blank" style="color: #004080;">Pre-Competition Requirements</a><br>
        • <strong>FTC Forums:</strong> <a href="https://ftcforum.usfirst.org/" target="_blank" style="color: #004080;">Official Q&A Platform</a><br>
        • <strong>FIRST Website:</strong> <a href="https://www.firstinspires.org/robotics/ftc" target="_blank" style="color: #004080;">FIRST Tech Challenge</a><br>
        • <strong>Team Management:</strong> <a href="https://ftc-events.firstinspires.org/" target="_blank" style="color: #004080;">Event Registration</a>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Call to action
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #1D63A8 0%, #0f4d8c 100%); 
                   padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;
                   box-shadow: 0 4px 15px rgba(29, 99, 168, 0.3);'>
        <h3 style='color: white; margin-bottom: 1rem;'>Ready to Compete by the Rules? 🏆</h3>
        <p style='color: white; font-size: 1.1rem; margin-bottom: 1.5rem;'>
        Knowledge of the rules is your competitive advantage. Study them thoroughly, 
        ask questions, and ensure your team is always competition-ready!
        </p>
        <p style='color: #FF8310; font-weight: bold; font-size: 1.2rem;'>
        Fair play wins more than just matches - it builds character! 🤝
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Allow the module to be run independently for testing
if __name__ == "__main__":
    show_rules()

