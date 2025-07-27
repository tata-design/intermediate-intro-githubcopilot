import streamlit as st
import warnings
import sys
import os

# Comprehensive warning suppression for ScriptRunContext
warnings.filterwarnings("ignore", ".*ScriptRunContext.*")
warnings.filterwarnings("ignore", ".*missing ScriptRunContext.*")
warnings.filterwarnings("ignore", ".*Thread.*missing ScriptRunContext.*")

# Suppress all UserWarnings from streamlit during import
warnings.filterwarnings("ignore", category=UserWarning, module="streamlit.*")

# Redirect stderr temporarily to suppress the warning at the system level
class NullWriter:
    def write(self, txt): pass
    def flush(self): pass

def suppress_streamlit_warnings():
    """Temporarily suppress stderr to catch system-level warnings"""
    original_stderr = sys.stderr
    sys.stderr = NullWriter()
    return original_stderr

def restore_stderr(original_stderr):
    """Restore stderr"""
    sys.stderr = original_stderr

# Main configuration function
def configure_app():
    """Configure the Streamlit app settings"""
    try:
        st.set_page_config(page_title="FTC Robotics Tutorials", page_icon="🤖", layout="centered")
    except st.StreamlitAPIException:
        # Page config already set, ignore
        pass

# Custom CSS for a modern look with a navigation header
def setup_ui():
    """Set up the UI with custom CSS and page layout"""
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #f0f0f0;
            color: #333;
            font-family: 'Segoe UI', 'Arial', sans-serif;
        }
        .nav-header {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 36px;
            background: linear-gradient(90deg, #005f99 0%, #0077cc 100%);
            padding: 18px 0 10px 0;
            border-radius: 0 0 18px 18px;
            margin-bottom: 32px;
            box-shadow: 0 2px 12px rgba(0,95,153,0.1);
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
            background: #e6f9ff;
            color: #005f99 !important;
            text-decoration: none;
        }
        .stButton > button {
            background: linear-gradient(90deg, #005f99 0%, #0077cc 100%);
            color: white;
            border-radius: 12px;
            font-size: 18px;
            border: none;
            padding: 12px 28px;
            box-shadow: 0 2px 8px rgba(0,95,153,0.12);
            transition: 0.2s;
            font-weight: 600;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #004080 0%, #005f99 100%);
            color: #fff;
            box-shadow: 0 4px 16px rgba(0,95,153,0.2);
        }
        
        /* Modern sidebar styling - white background with orange outline */
        .css-1d391kg, [data-testid="stSidebar"], .css-1lcbmhc, .stSidebar {
            background: white !important;
            border-right: 3px solid #FF8310 !important;
            box-shadow: none !important;
        }
        
        /* Additional sidebar container targeting */
        [data-testid="stSidebar"] > div {
            background: white !important;
        }
        
        /* Sidebar content styling */
        .css-17eq0hr {
            background: transparent !important;
            padding: 1.5rem 1rem;
        }
        
        /* Hide radio button circles but keep functionality */
        .stRadio > div > label > div:first-child {
            display: none !important;
        }
        
        /* Ensure the entire label is clickable */
        .stRadio > div > label {
            position: relative !important;
        }
        
        /* Create invisible clickable area over the entire label */
        .stRadio > div > label::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
            z-index: 1;
        }
        
        /* Radio button container */
        .stRadio > div {
            gap: 0.8rem;
            display: flex;
            flex-direction: column;
        }
        
        /* Clean sidebar title */
        .css-1d391kg .element-container:first-child {
            margin-bottom: 2rem;
        }
        
        /* Logo styling */
        .sidebar-logo {
            display: block;
            margin: 0 auto 1.5rem auto;
            max-width: 120px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(255, 131, 16, 0.2);
        }
        
        /* Radio button labels - clean text-based design */
        .stRadio > div > label {
            background: transparent !important;
            border: none !important;
            border-radius: 0 !important;
            padding: 0.5rem 0 !important;
            margin: 0 !important;
            font-size: 0.95rem !important;
            font-weight: 400 !important;
            color: #1D63A8 !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
            box-shadow: none !important;
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            min-height: auto !important;
            text-align: left !important;
            position: relative !important;
            overflow: visible !important;
            pointer-events: auto !important;
        }
        
        /* Radio button labels hover effect */
        .stRadio > div > label:hover {
            background: transparent !important;
            color: #0f4d8c !important;
            transform: none !important;
            box-shadow: none !important;
            border-radius: 0 !important;
        }
        
        /* Selected radio button - simple underline style */
        .stRadio > div > label[data-checked="true"] {
            background: transparent !important;
            color: #1D63A8 !important;
            border: none !important;
            box-shadow: none !important;
            border-radius: 0 !important;
            transform: none !important;
            font-weight: 600 !important;
            position: relative !important;
        }
        
        /* Add underline to selected item */
        .stRadio > div > label[data-checked="true"]:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: #FF8310;
        }
        
        /* Ensure radio button input is clickable but hidden */
        .stRadio > div > label > div:first-child input[type="radio"] {
            opacity: 0 !important;
            position: absolute !important;
            pointer-events: auto !important;
            width: 100% !important;
            height: 100% !important;
            margin: 0 !important;
            top: 0 !important;
            left: 0 !important;
        }
        
        /* Sidebar navigation title styling */
        .css-1d391kg .css-10trblm,
        .css-1d391kg h3,
        [data-testid="stSidebar"] .css-10trblm,
        [data-testid="stSidebar"] h3 {
            color: #1D63A8 !important;
            font-weight: 700 !important;
            font-size: 1.3em !important;
            margin-bottom: 1.5rem !important;
            text-shadow: none !important;
            text-align: left !important;
        }
        
        /* Main content area - bigger text */
        .main .block-container {
            padding-top: 2rem;
            font-size: 1.1em;
        }
        
        /* Header text bigger */
        h1 {
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            margin-bottom: 2rem !important;
        }
        
        h2 {
            font-size: 2rem !important;
            font-weight: 600 !important;
            margin-bottom: 1.5rem !important;
        }
        
        /* Paragraph text bigger */
        p {
            font-size: 1.2rem !important;
            line-height: 1.6 !important;
        }
        
        /* Info box styling */
        .stAlert {
            font-size: 1.1rem !important;
            padding: 1.5rem !important;
            border-radius: 12px !important;
            border-left: 4px solid #004080 !important;
        }
        
        /* Make all blue text darker and more visible */
        .stMarkdown a {
            color: #004080 !important;
        }
        
        /* Darker blue for info boxes */
        div[data-testid="stAlert"] {
            background-color: #e6f2ff !important;
            border-left-color: #004080 !important;
        }
        
        /* Darker blue for any light blue elements */
        .css-1d391kg .css-10trblm,
        [data-testid="stSidebar"] .css-10trblm,
        [data-testid="stSidebar"] .element-container,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p {
            color: #1D63A8 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Website header (no navigation links since sidebar handles navigation)
    st.markdown(
        """
        <div class='nav-header'>
            <span class='nav-link'>FTC Robotics Learning Platform</span>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_app():
    """Main application rendering logic"""
    
    # Modern, exciting title with gradients and effects
    st.markdown(
        """
        <div style='
            background: white;
            padding: 2.5rem 2rem;
            margin: -1rem -2rem 3rem -2rem;
            border-radius: 0 0 25px 25px;
            border-bottom: 1px solid rgba(29, 99, 168, 0.1);
            box-shadow: 0 4px 20px rgba(29, 99, 168, 0.08);
            text-align: center;
        '>
            <h1 style='
                background: linear-gradient(135deg, #1D63A8 0%, #FF8310 50%, #1D63A8 100%);
                background-size: 200% 200%;
                animation: gradient 3s ease infinite;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 3.5rem !important;
                font-weight: 800 !important;
                margin-bottom: 0.5rem !important;
                text-shadow: 0 4px 8px rgba(29, 99, 168, 0.3);
                letter-spacing: 2px;
            '>
                🤖 BotBuilders Hub
            </h1>
            <div style='
                background: linear-gradient(90deg, #FF8310 0%, #1D63A8 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 1.8rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
                letter-spacing: 1px;
            '>
                FTC Robotics Tutorials & Learning Hub
            </div>
            <div style='
                width: 120px;
                height: 4px;
                background: linear-gradient(90deg, #1D63A8 0%, #FF8310 50%, #1D63A8 100%);
                margin: 0 auto;
                border-radius: 2px;
                box-shadow: 0 2px 8px rgba(255, 131, 16, 0.4);
            '></div>
        </div>
        
        <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add logo and title to sidebar
    with st.sidebar:
        # BotBuilders Hub Logo
        try:
            st.image("MyImages/BotBuilders Hub Logo.jpeg", width=140, use_container_width=False)
        except:
            # Fallback if logo file is not found
            st.markdown(
                """
                <div style='text-align: center; margin-bottom: 1.5rem;'>
                    <div style='background: linear-gradient(135deg, #1D63A8 0%, #FF8310 100%); 
                               width: 140px; height: 100px; border-radius: 15px; 
                               display: flex; flex-direction: column; align-items: center; justify-content: center; 
                               margin: 0 auto; box-shadow: 0 4px 12px rgba(255, 131, 16, 0.3);'>
                        <div style='color: white; font-weight: bold; font-size: 16px; text-align: center; line-height: 1.2;
                                   text-shadow: 0 1px 2px rgba(0,0,0,0.3);'>
                            🤖 BotBuilders<br>
                            <span style='font-size: 14px; opacity: 0.9;'>Hub</span>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Add title similar to Robocorp
        st.markdown(
            """
            <div style='margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid #e0e0e0;'>
                <h3 style='color: #1D63A8; font-weight: 700; font-size: 1.3rem; margin: 0; text-align: left;'>
                    BotBuilders Hub
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Sidebar navigation
    section = st.sidebar.radio(
        "",
        ("🏠 Home", "💻 Coding Tutorial", "📐 CAD Tutorial", "🔨 Building Tutorial", "📋 Rules", "🏆 Points System")
    )

    if section == "🏠 Home":
        st.header("🎉 Welcome to BotBuilders Hub!")
        
        # Hero section with welcoming message
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                       padding: 2rem; border-radius: 15px; border-left: 4px solid #004080; margin-bottom: 2rem;
                       text-align: center; box-shadow: 0 4px 15px rgba(0, 64, 128, 0.1);'>
            <h2 style='color: #004080; margin-bottom: 1rem;'>🚀 Ready to Build Amazing Robots?</h2>
            <p style='font-size: 1.3rem; color: #333; margin-bottom: 1.5rem;'>
            Welcome to your ultimate FTC Robotics learning destination! Whether you're a beginner or looking to advance your skills, 
            we've got everything you need to succeed in the exciting world of robotics.
            </p>
            <p style='font-size: 1.1rem; color: #555;'>
            🎯 <strong>Mission:</strong> Empowering the next generation of robotics engineers through hands-on learning and innovation.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # What you'll learn section
        st.subheader("🔧 What You'll Master Here")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(
                """
                <div style='background: white; padding: 1.2rem; border-radius: 12px; border-top: 4px solid #FF8310; 
                           box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; min-height: 200px; 
                           display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <h3 style='color: #FF8310; margin-bottom: 0.8rem; font-size: 1.1rem;'>💻 Coding</h3>
                <p style='font-size: 0.85rem; line-height: 1.3; margin: 0; text-align: center; padding: 0 0.5rem;'>Learn to program your robot with Python, Java, and modern development tools. From basic movements to advanced AI integration.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            st.markdown(
                """
                <div style='background: white; padding: 1.2rem; border-radius: 12px; border-top: 4px solid #1D63A8; 
                           box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; min-height: 200px; 
                           display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <h3 style='color: #1D63A8; margin-bottom: 0.8rem; font-size: 1.1rem;'>🔨 Building</h3>
                <p style='font-size: 0.85rem; line-height: 1.3; margin: 0; text-align: center; padding: 0 0.5rem;'>Master mechanical design, assembly techniques, and structural engineering to create robust and efficient robots.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col3:
            st.markdown(
                """
                <div style='background: white; padding: 1.2rem; border-radius: 12px; border-top: 4px solid #28a745; 
                           box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; min-height: 200px; 
                           display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <h3 style='color: #28a745; margin-bottom: 0.8rem; font-size: 1.1rem;'>📐 CAD Design</h3>
                <p style='font-size: 0.85rem; line-height: 1.3; margin: 0; text-align: center; padding: 0 0.5rem;'>Design professional robot parts using industry-standard CAD software like Fusion 360, SolidWorks, and more.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        # Quick start section
        st.subheader("🚀 Quick Start Guide")
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #fff8e1 0%, #ffe4b5 100%); 
                       padding: 1.5rem; border-radius: 12px; border-left: 4px solid #FF8310; margin-bottom: 2rem;
                       box-shadow: 0 2px 8px rgba(255, 131, 16, 0.1);'>
            <div style='font-size: 1.1rem; margin-bottom: 1rem;'><strong>New to FTC Robotics?</strong> Here's how to get started:</div>
            <ol style='margin: 0; padding-left: 1.5rem; font-size: 1rem; line-height: 1.6;'>
                <li style='margin-bottom: 0.5rem;'><strong>Start Building</strong> - Learn mechanical assembly and understand robot components</li>
                <li style='margin-bottom: 0.5rem;'><strong>Program Your Robot</strong> - Master coding basics and control systems</li>
                <li style='margin-bottom: 0.5rem;'><strong>Design Improvements with CAD</strong> - Create custom parts and optimize your robot</li>
                <li style='margin-bottom: 0.5rem;'><strong>Review Rules & Scoring</strong> - Master competition requirements and strategies</li>
            </ol>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Features section
        st.subheader("✨ Why Choose BotBuilders Hub?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                """
                <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #1D63A8; 
                           box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem; height: 350px;
                           display: flex; flex-direction: column; justify-content: flex-start;'>
                <div style='font-size: 0.9rem; line-height: 1.5;'>
                <strong style='color: #1D63A8;'>🎥 Interactive Video Tutorials</strong><br>
                Step-by-step video guides for every skill level<br><br>
                
                <strong style='color: #1D63A8;'>📚 Comprehensive Resources</strong><br>
                Everything from beginner basics to advanced techniques<br><br>
                
                <strong style='color: #1D63A8;'>🏆 Competition Ready</strong><br>
                Learn the rules, scoring, and winning strategies
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            st.markdown(
                """
                <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #FF8310; 
                           box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem; height: 350px;
                           display: flex; flex-direction: column; justify-content: flex-start;'>
                <div style='font-size: 0.9rem; line-height: 1.5;'>
                <strong style='color: #FF8310;'>🔧 Hands-On Learning</strong><br>
                Practical projects and real-world applications<br><br>
                
                <strong style='color: #FF8310;'>🤝 Peer Powered Learning</strong><br>
                We started BotBuilders Hub based on our own robotics journey—built by teens to help other teens learn, build, and grow in tech.<br>
                
                <strong style='color: #FF8310;'>🚀 Industry Tools</strong><br>
                Work with professional software and techniques
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
            <h3 style='color: white; margin-bottom: 1rem;'>Ready to Start Your Robotics Journey? 🤖</h3>
            <p style='color: white; font-size: 1.1rem; margin-bottom: 1.5rem;'>
            Use the sidebar to explore our tutorials and start building amazing robots today!
            </p>
            <p style='color: #FF8310; font-weight: bold; font-size: 1.2rem;'>
            Your next breakthrough is just one tutorial away! 💡
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif section == "💻 Coding Tutorial":
        # Import and show the comprehensive coding tutorial
        from tutorials.coding import show_coding_tutorial
        show_coding_tutorial()
    elif section == "📐 CAD Tutorial":
        st.header("CAD Tutorial for FTC Robotics")
        
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                       padding: 1.5rem; border-radius: 12px; border-left: 4px solid #004080; margin-bottom: 2rem;'>
            <b>Introduction to CAD</b><br>
            Computer-Aided Design (CAD) software is essential for designing robot parts in FTC Robotics. 
            This tutorial will guide you through the basics of using CAD software effectively.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.subheader("Getting Started with CAD")
        
        # Add the YouTube video
        st.subheader("📹 CAD Tutorial Video")
        st.markdown("Watch this comprehensive tutorial to get started with CAD for FTC Robotics:")
        
        # Embed the YouTube video
        st.video("https://www.youtube.com/watch?v=wS9xyiaxYZM&t=3s")
        
        st.markdown(
            """
            CAD software allows you to create precise drawings and models of your robot components. 
            Here are some popular CAD tools used in FTC Robotics:
            
            - **Fusion 360**: A powerful CAD tool that is free for students and educators.
            - **Tinkercad**: A user-friendly, web-based CAD tool suitable for beginners.
            - **SolidWorks**: A professional-grade CAD software often used in engineering.

            Choose a tool that fits your skill level and project requirements.
            """
        )
        
        st.subheader("Tips for Effective CAD Design")
        st.markdown(
            """
            - **Start Simple**: Begin with basic shapes and gradually add complexity to your designs.
            - **Use Constraints**: Apply constraints to ensure parts fit together correctly.
            - **Plan Your Design**: Sketch your ideas on paper before starting in CAD to save time.
            - **Test Fit**: If possible, 3D print your designs to test their fit and functionality before finalizing.

            Remember, practice makes perfect! The more you use CAD software, the more proficient you'll become.
            """
        )
        
        st.subheader("Resources for Learning CAD")
        st.markdown(
            """
            Here are some resources to help you learn more about CAD:
            - [Fusion 360 Learning Resources](https://www.autodesk.com/products/fusion-360/learn-and-support)
            - [Tinkercad Tutorials](https://www.tinkercad.com/learn)
            - [SolidWorks Tutorials](https://www.solidworks.com/sw/resources/tutorials.htm)

            Explore these resources to enhance your CAD skills and improve your robot designs!
            """
        )
    elif section == "🔨 Building Tutorial":
        st.header("Building Your FTC Robot")
        
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                       padding: 1.5rem; border-radius: 12px; border-left: 4px solid #004080; margin-bottom: 2rem;'>
            <b>Welcome to the Building Tutorial!</b><br>
            In this section, we will guide you through the process of assembling your FTC robot. 
            Building a robot involves understanding the components, ensuring structural integrity, and using the right materials.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.subheader("Understanding Robot Components")
        
        # Add the YouTube video
        st.subheader("📹 Building Tutorial Video")
        st.markdown("Watch this comprehensive tutorial to get started with building your FTC robot:")
        
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
        
        st.subheader("Assembly Guidelines")
        st.markdown(
            """
            - **Start with the Chassis**: Ensure it is sturdy and can support all other components.
            - **Secure Motors Properly**: Use screws and brackets to attach motors to the chassis.
            - **Organize Wiring**: Keep wires tidy to avoid tangling and interference with moving parts.
            - **Test Stability**: After assembly, check for any loose parts or instability.
            """
        )
        
        st.subheader("Tips for Structural Integrity")
        st.markdown(
            """
            - Use lightweight materials to reduce the overall weight of the robot.
            - Reinforce joints with additional brackets or supports.
            - Ensure that the center of gravity is low to prevent tipping.
            """
        )
    elif section == "📋 Rules":
        # Import and show the comprehensive rules guide
        from rules import show_rules
        show_rules()
    elif section == "🏆 Points System":
        st.header("Points System")
        st.markdown("Learn how the points system works in FTC Robotics competitions. (Add your content here!)")

    st.info("All tutorials and resources are free to access. Happy learning!")

    # Professional Footer with better spacing
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Footer with styled background
    st.markdown(
        """
        <div style='
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            padding: 3rem 2rem 2rem 2rem;
            margin: 2rem -2rem -2rem -2rem;
            border-radius: 15px 15px 0 0;
            color: white;
        '>
        """,
        unsafe_allow_html=True
    )
    
    # Footer content with better spacing
    col1, spacer1, col2, spacer2, col3, spacer3, col4 = st.columns([3, 0.5, 3, 0.5, 3, 0.5, 3])
    
    with col1:
        st.markdown(
            """
            <div style='padding: 1rem 0;'>
                <h3 style='color: #FF8310; margin-bottom: 1.5rem; font-size: 1.3rem; font-weight: 600;'>🤖 BotBuilders Hub</h3>
                <p style='color: #ecf0f1; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;'>
                    Empowering the next generation of robotics engineers through comprehensive FTC learning resources.
                </p>
                <p style='color: #bdc3c7; font-size: 0.9rem; font-style: italic;'>
                    Built by students, for students.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style='padding: 1rem 0;'>
                <h4 style='color: #1D63A8; margin-bottom: 1.5rem; font-size: 1.2rem; font-weight: 600;'>Quick Links</h4>
                <div style='display: flex; flex-direction: column; gap: 0.8rem;'>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>• Tutorials</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>• Competition Rules</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>• Getting Started</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>• Resources</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div style='padding: 1rem 0;'>
                <h4 style='color: #1D63A8; margin-bottom: 1.5rem; font-size: 1.2rem; font-weight: 600;'>Follow Us</h4>
                <div style='display: flex; flex-direction: column; gap: 0.8rem; margin-bottom: 1.5rem;'>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>📷 Instagram</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>📘 Facebook</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>🐦 Twitter</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>📺 YouTube</p>
                </div>
                <p style='color: #bdc3c7; font-size: 0.9rem; font-style: italic;'>
                    Join our community of young robotics enthusiasts!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            """
            <div style='padding: 1rem 0;'>
                <h4 style='color: #1D63A8; margin-bottom: 1.5rem; font-size: 1.2rem; font-weight: 600;'>Contact Us</h4>
                <div style='display: flex; flex-direction: column; gap: 0.8rem; margin-bottom: 1.5rem;'>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>📧 hello@botbuildershub.com</p>
                    <p style='color: #ecf0f1; margin: 0; font-size: 1rem;'>💬 Discord: BotBuilders Community</p>
                </div>
                <p style='color: #bdc3c7; font-size: 0.9rem; font-style: italic;'>
                    Questions? We're here to help!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Footer bottom section
    st.markdown(
        """
        <hr style='border: none; border-top: 1px solid #4a5568; margin: 2rem 0 1.5rem 0;'>
        <div style='display: flex; justify-content: space-between; align-items: center; padding: 0 1rem;'>
            <p style='color: #bdc3c7; font-size: 0.9rem; margin: 0;'>
                © 2025 BotBuilders Hub. FTC Robotics Learning Platform. All Rights Reserved
            </p>
            <div>
                <span style='color: #bdc3c7; font-size: 0.9rem;'>Privacy Policy</span>
                <span style='color: #4a5568; margin: 0 0.5rem;'>|</span>
                <span style='color: #bdc3c7; font-size: 0.9rem;'>Terms and Conditions</span>
            </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main execution
if __name__ == "__main__":
    # Only run if being executed directly (not imported)
    try:
        original_stderr = suppress_streamlit_warnings()
        configure_app()
        restore_stderr(original_stderr)
        setup_ui()
        render_app()
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    # When running through streamlit run command
    original_stderr = suppress_streamlit_warnings()
    configure_app()
    restore_stderr(original_stderr)
    setup_ui()
    render_app()