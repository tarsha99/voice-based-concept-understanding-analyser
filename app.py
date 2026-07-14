import streamlit as st
import re

from gemini_analyzer import analyze_concept
from pdf_report import generate_pdf_report

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("🎤 Voice Based Concept Understanding Analyser")

st.sidebar.info("""
### Instructions

1. Enter your Gemini API Key.
2. Enter the topic.
3. Explain the topic in your own words.
4. Click **Analyze**.
5. View the AI evaluation.
6. Download the PDF report.
""")

# -------------------------------
# Main Title
# -------------------------------

st.title("🎤 Voice Based Concept Understanding Analyser")

st.write(
    "Evaluate a student's conceptual understanding using **Google Gemini AI**."
)

st.divider()

# -------------------------------
# User Inputs
# -------------------------------

api_key = st.text_input(
    "🔑 Enter Gemini API Key",
    type="password"
)

topic = st.text_input(
    "📘 Enter Topic"
)

explanation = st.text_area(
    "📝 Explain the topic in your own words",
    height=220
)

# -------------------------------
# Analyze Button
# -------------------------------

if st.button("🚀 Analyze"):

    if api_key == "":
        st.warning("Please enter your Gemini API Key.")
        st.stop()

    if topic == "":
        st.warning("Please enter the topic.")
        st.stop()

    if explanation == "":
        st.warning("Please explain the topic.")
        st.stop()

    with st.spinner("Analyzing your explanation..."):

        result = analyze_concept(
            topic,
            explanation,
            api_key
        )

    st.success("✅ Analysis Completed Successfully")

    st.divider()

    # -------------------------------
    # AI Evaluation
    # -------------------------------

    st.subheader("📊 AI Evaluation")

    st.markdown(result)

    # -------------------------------
    # Extract Score
    # -------------------------------

    score = 0

    match = re.search(r'(\d+)\s*/\s*10', result)

    if match:
        score = int(match.group(1))

    percentage = score * 10

    # -------------------------------
    # Performance
    # -------------------------------

    st.divider()

    st.subheader("📈 Overall Performance")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            label="Overall Score",
            value=f"{score}/10"
        )

    with col2:

        if score >= 9:
            grade = "A+"
        elif score >= 8:
            grade = "A"
        elif score >= 7:
            grade = "B"
        elif score >= 6:
            grade = "C"
        elif score >= 5:
            grade = "D"
        else:
            grade = "F"

        st.metric(
            label="Grade",
            value=grade
        )

    st.progress(percentage)

    st.write(f"Performance : **{percentage}%**")

    # -------------------------------
    # Generate PDF
    # -------------------------------

    pdf_file = generate_pdf_report(
        topic=topic,
        transcript=explanation,
        score=score,
        feedback=result,
        suggestions="Keep practicing and improve the missing concepts."
    )

    st.divider()

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="Concept_Evaluation_Report.pdf",
            mime="application/pdf"
        )

    st.balloons()

st.divider()

st.caption("Developed using Streamlit + Google Gemini AI")