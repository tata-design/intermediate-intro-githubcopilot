import streamlit as st

st.set_page_config(page_title="Tutoring Signup Form", page_icon="🎓", layout="centered", initial_sidebar_state="auto")

# Custom CSS for lavender theme and fun style
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #E6E6FA;
    }
    .stTextInput > div > div > input {
        background-color: #f8f6ff;
        border: 2px solid #b57edc;
        border-radius: 10px;
        color: #4b306a;
        font-size: 18px;
        padding: 8px;
    }
    .stButton > button {
        background-color: #b57edc;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        border: none;
        padding: 10px 24px;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background-color: #a084ca;
        color: #fff;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #7c5e99;
    }
    .purple-label label {
        color: #7c5e99 !important;
        font-weight: bold;
    }
    .welcome-purple {
        color: #7c5e99;
        font-size: 1.08em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌸 Tutoring Signup Form 🌸")

st.markdown(
    """
    <div style='background-color:#f8f6ff; border-radius:10px; padding:18px; margin-bottom:18px; border:1.5px solid #b57edc;'>
    <b class='welcome-purple'>Welcome!</b><br>
    <span class='welcome-purple'>I’m a tenth grader from Sugar Land, TX, attending Logos Preparatory Academy with a 4.0 GPA and advanced two levels in math. I aspire to become a biomedical engineer and doctor, and I’m active in my community through MYC, NSBE, and SWE. I founded Ivy Charms, a handmade knitting business where I built a local supply chain and hired family members. My technical skills include HTML, CAD, and Java, and I’m a standout coder on my school’s robotics team. I also helped build and program a GoBilda robot with my brother. Outside academics, I enjoy volleyball, tennis, reading dystopian novels, and drawing book covers. I’m excited about the Summer Mentorship Program to grow my coding skills, collaborate on group projects, and learn from tech companies like Microsoft.</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Fill out the form below to join our fun tutoring community!")

with st.form("signup_form"):
    with st.container():
        first_name = st.text_input("First Name ✨", key="first_name", label_visibility="visible")
        background = st.text_input("Background 🌈", key="background", label_visibility="visible")
        list_of_courses = st.text_input("List of Courses 📚", key="courses", label_visibility="visible")
        email_address = st.text_input("Email Address 📧", key="email", label_visibility="visible")
        last_name = st.text_input("Last Name ✨", key="last_name", label_visibility="visible")

    # Apply purple color to all labels using a custom class
    st.markdown(
        '''<script>
        const labels = window.parent.document.querySelectorAll('label');
        labels.forEach(label => label.classList.add('purple-label'));
        </script>''',
        unsafe_allow_html=True
    )

    submitted = st.form_submit_button("Sign Up!")
    
    if submitted:
        st.balloons()
        st.success(f"Thank you for signing up, {first_name} {last_name}! 🎉")
        st.write(f"**Background:** {background}")
        st.write(f"**List of courses:** {list_of_courses}")
        st.write(f"**Email address:** {email_address}")