import json
import os

from openai import OpenAI


def _create_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Set it in your environment before running the app."
        )

    return OpenAI(api_key=api_key)


def analyze_resume(resume_text, user_goal):
    client = _create_openai_client()

    prompt = f"""You are a senior software engineer and high-level interviewer.
Evaluate the following resume text based on the user's goal.

User goal: "{user_goal}"

Return only JSON:
{{
  "skills": [],
  "missing_skills": [],
  "roadmap": [],
  "strengths": [],
  "interview_questions": []
}}

Resume:
{resume_text}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "You are a strict hiring assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        content = response.choices[0].message.content.strip()
        start = content.find("{")
        end = content.rfind("}") + 1
        return json.loads(content[start:end])

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "strengths": [],
            "interview_questions": [],
            "error": f"Failed to analyze resume: {str(e)}",
        }