import google.generativeai as genai


def analyze_concept(topic, explanation, api_key):
    """
    Analyze the student's concept understanding using Google Gemini.
    """

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Load Gemini model
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Prompt for Gemini
    prompt = f"""
You are an experienced AI teacher.

Evaluate the student's understanding of the given topic.

Topic:
{topic}

Student Explanation:
{explanation}

Analyze the explanation carefully and provide the response in exactly this format.

----------------------------------------

Overall Score: __ / 10

Grade: __

Strengths:
• Point 1
• Point 2
• Point 3

Weaknesses:
• Point 1
• Point 2
• Point 3

Suggestions:
• Point 1
• Point 2
• Point 3

Overall Feedback:
Write a short paragraph (4–5 lines) describing the student's conceptual understanding.

----------------------------------------

Rules:
- Give a realistic score.
- Be encouraging and constructive.
- Mention important concepts that are missing.
- Keep the response professional.
"""

    # Generate response
    response = model.generate_content(prompt)

    return response.text