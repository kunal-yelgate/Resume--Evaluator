import json
import os

from dotenv import load_dotenv
from openai import APIConnectionError, AuthenticationError, BadRequestError, OpenAI, RateLimitError


load_dotenv(override=True)


def _mask_api_key(api_key):
    if not api_key:
        return ""

    if len(api_key) <= 12:
        return api_key[:4] + "********"

    return f"{api_key[:8]}************"


def _create_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing.")

    if os.getenv("DEBUG_OPENAI_KEY") == "1":
        print(f"Using OpenAI key: {_mask_api_key(api_key)}")

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
  "interview_questions": []
}}

Resume:
{resume_text}
"""

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "You are a strict hiring assistant that returns valid JSON only.",
                },
                {"role": "user", "content": prompt},
            ],
        )

        content = response.output_text.strip()
        start = content.find("{")
        end = content.rfind("}") + 1
        parsed = json.loads(content[start:end])

        return {
            "skills": parsed.get("skills", []),
            "missing_skills": parsed.get("missing_skills", []),
            "roadmap": parsed.get("roadmap", []),
            "interview_questions": parsed.get("interview_questions", []),
        }

    except AuthenticationError:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": "OpenAI authentication failed. Check OPENAI_API_KEY.",
        }

    except APIConnectionError:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": "Unable to connect to the OpenAI API.",
        }

    except RateLimitError as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": f"OpenAI quota exceeded or rate limit reached: {str(e)}",
        }

    except BadRequestError as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": f"OpenAI request was invalid: {str(e)}",
        }

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": f"Failed to analyze resume: {str(e)}",
        }