"""
BotBuilders Hub - FTC Robotics Learning Platform
Main application entry point for Streamlit Community Cloud deployment
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main application
from home import configure_app, setup_ui, render_app, suppress_streamlit_warnings, restore_stderr

if __name__ == "__main__":
    # Configure and run the application
    original_stderr = suppress_streamlit_warnings()
    configure_app()
    restore_stderr(original_stderr)
    setup_ui()
    render_app()
