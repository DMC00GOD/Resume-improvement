import requests

# Replace with your real OpenRouter API key
OPENROUTER_API_KEY = "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"

def get_llm_analysis(resume_text, job_description):
    prompt = f"""
You are an expert career advisor AI.

Compare the following resume and job description. Complete these tasks clearly and thoroughly:

1. List key matched skills in bullet points.
2. List missing but required skills (focus on tools, frameworks, techniques).
3. Give detailed, specific suggestions to improve the resume.
4. For each missing skill, provide 1–2 **high-quality learning resources** (YouTube, Coursera, docs).
5. Finish with a match score out of 100%, clearly written as: Match Score: XX%

Keep your tone direct and helpful. Use bullet points for readability.

Resume:
{resume_text}

Job Description:
{job_description}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mixtral-8x7b-instruct",  # You can try llama3 too
        "temperature": 0.7,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if not response.ok:
        print("ERROR:", response.status_code, response.text)
        response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
