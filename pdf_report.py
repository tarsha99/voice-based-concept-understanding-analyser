from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_pdf_report(topic, transcript, score, feedback, suggestions):

    # Create Reports folder if it doesn't exist
    reports_folder = "Reports"
    os.makedirs(reports_folder, exist_ok=True)

    # PDF file path
    filename = os.path.join(reports_folder, "Concept_Evaluation_Report.pdf")

    # Create PDF
    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    # ---------------- Title ----------------
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(
        width / 2,
        height - 40,
        "Voice Based Concept Understanding Report"
    )

    # ---------------- Topic ----------------
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 80, "Topic:")

    c.setFont("Helvetica", 12)
    c.drawString(120, height - 80, topic)

    # ---------------- Transcript ----------------
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 110, "Student Explanation:")

    c.setFont("Helvetica", 11)

    y = height - 130

    for line in transcript.split("\n"):
        c.drawString(60, y, line[:90])
        y -= 18

    # ---------------- Score ----------------
    y -= 15

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Overall Score:")

    c.setFont("Helvetica", 12)
    c.drawString(170, y, f"{score}/10")

    # ---------------- Feedback ----------------
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "AI Feedback:")

    c.setFont("Helvetica", 11)

    y -= 20

    for line in feedback.split("\n"):
        c.drawString(60, y, line[:90])
        y -= 18

    # ---------------- Suggestions ----------------
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Suggestions:")

    c.setFont("Helvetica", 11)

    y -= 20

    for line in suggestions.split("\n"):
        c.drawString(60, y, line[:90])
        y -= 18

    # Save PDF
    c.save()

    # Return PDF file path
    return filename