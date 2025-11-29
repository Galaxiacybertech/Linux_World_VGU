import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="VGU Student Dashboard",
    layout="wide"
)
st.markdown("""s
<style>
body {
    background-color: #f6f7fb;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background: rgba(255,255,255,0.85);
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 22px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}
h1, h2, h3 {
    color: #1f3a5f;
}
.label {
    color: #555;
}
.stButton>button {
    background-color: #3baea0;
    color: white;
    border-radius: 8px;
    font-weight: 500;
}
.stButton>button:hover {
    background-color: #2f8f83;
}
.footer {
    text-align: center;
    color: #777;
    font-size: 14px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="card">
<h1>VGU Student Performance Dashboard</h1>
<p class="label">A simple and clean dashboard to manage student subject-wise marks</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("Overview")
st.write("You can write:", 10 + 5)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Student Details")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Enter your name")

with col2:
    age = st.number_input("Enter your age", min_value=1, max_value=100)

with col3:
    course = st.selectbox("Select course", ["BCA", "B.Tech", "MCA"])

st.write(f"Name: {name} | Age: {age} | Course: {course}")

if st.button("Confirm Details"):
    st.success("Details saved successfully")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("File Upload")
file = st.file_uploader("Upload your file")
if file:
    file.read()
    st.success("File uploaded successfully")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Enter Subject Marks")

student_name = st.text_input("Student name for marks table")
subject = st.selectbox("Select subject", ["Python", "C++", "Java", "Data Structures"])
marks = st.number_input("Marks obtained", min_value=0, max_value=100)

if "student_data" not in st.session_state:
    st.session_state.student_data = []

if st.button("Add Marks"):
    if student_name and marks > 0:
        st.session_state.student_data.append({
            "Student Name": student_name,
            "Subject": subject,
            "Marks": marks
        })
        st.success("Marks added")
    else:
        st.warning("Please enter valid data")

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.student_data:
    df = pd.DataFrame(st.session_state.student_data)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Marks Table")
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Average Marks (Line)")
        st.line_chart(df.pivot_table(index="Subject", values="Marks", aggfunc="mean"))
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Average Marks (Bar)")
        st.bar_chart(df.pivot_table(index="Subject", values="Marks", aggfunc="mean"))
        st.markdown("</div>", unsafe_allow_html=True)

    # PIE CHART — SMALL & SUBTLE
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Subject-wise Distribution")

    subject_marks = df.groupby("Subject")["Marks"].sum()
    fig, ax = plt.subplots(figsize=(2.8, 2.8))
    ax.pie(
        subject_marks,
        labels=subject_marks.index,
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 9}
    )
    ax.axis("equal")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("""
<div class="footer">
VGU Streamlit Dashboard • Clean UI Version
</div>
""", unsafe_allow_html=True)