import streamlit as st
import warnings

# Suppress the ScriptRunContext warning
warnings.filterwarnings("ignore", ".*ScriptRunContext.*", category=UserWarning)

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
            background: linear-gradient(90deg, #0077cc 0%, #00aaff 100%);
            padding: 18px 0 10px 0;
            border-radius: 0 0 18px 18px;
            margin-bottom: 32px;
            box-shadow: 0 2px 12px rgba(0,119,204,0.07);
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
            background: linear-gradient(90deg, #0077cc 0%, #00aaff 100%);
            color: white;
            border-radius: 12px;
            font-size: 18px;
            border: none;
            padding: 12px 28px;
            box-shadow: 0 2px 8px rgba(0,119,204,0.08);
            transition: 0.2s;
            font-weight: 600;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #005f99 0%, #0077cc 100%);
            color: #fff;
            box-shadow: 0 4px 16px rgba(0,119,204,0.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Website navigation header (visual only)
    st.markdown(
        """
        <div class='nav-header'>
            <span class='nav-link'>Tutorials</span>
            <span class='nav-link'>Rules</span>
            <span class='nav-link'>Points System</span>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_app():
    """Main application rendering logic"""
    st.title("🤖 FTC Robotics Tutorials")

    # Sidebar navigation
    section = st.sidebar.radio(
        "Navigate to:",
        ("Home", "Coding Tutorial", "CAD Tutorial", "Building Tutorial", "Rules", "Points System")
    )

    if section == "Home":
        st.header("Welcome!")
        st.markdown(
            """
            Explore our comprehensive tutorials to learn about coding, CAD design, and building FTC robots.
            Use the sidebar to navigate to different sections.
            """
        )
    elif section == "Coding Tutorial":
        st.header("Coding Tutorial")
        st.markdown("Learn how to program your FTC robot using Python and other tools. (Add your content here!)")
    elif section == "CAD Tutorial":
        st.header("CAD Tutorial")
        st.markdown("Discover how to design robot parts using CAD software. (Add your content here!)")
    elif section == "Building Tutorial":
        st.header("Building Tutorial")
        st.markdown("Get tips and tricks for building strong and efficient FTC robots. (Add your content here!)")
    elif section == "Rules":
        st.header("FTC Rules")
        st.markdown("Understand the official rules for FTC competitions. (Add your content here!)")
    elif section == "Points System":
        st.header("Points System")
        st.markdown("Learn how the points system works in FTC Robotics competitions. (Add your content here!)")

    st.info("All tutorials and resources are free to access. Happy learning!")

# Main execution
if __name__ == "__main__":
    # Only run if being executed directly (not imported)
    try:
        configure_app()
        setup_ui()
        render_app()
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    # When running through streamlit run command
    configure_app()
    setup_ui()
    render_app()