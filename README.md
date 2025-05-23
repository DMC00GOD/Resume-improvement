# Resume vs Job Matcher with LLM

This tool helps job seekers compare their resume with job descriptions using free LLM APIs (like OpenRouter running Mistral/Mixtral).

## 💡 Features
- Upload PDF resume and paste job description
- Extracts skills and compares them
- Shows matched skills, missing skills, and improvement suggestions
- Powered by Mixtral 8x7B via OpenRouter API
- Built with Python + Streamlit

## 🧠 Tech Stack
- **Frontend/UI**: Streamlit
- **LLM API**: OpenRouter (Mixtral model)
- **Resume Parsing**: PyMuPDF
- **API Requests**: requests

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/resume_job_matcher.git
cd resume_job_matcher
pip install -r requirements.txt
streamlit run app.py
```

## 🔐 API Key
Edit `llm_client.py` and paste your API key like this:
```python
OPENROUTER_API_KEY = "sk-your-key-here"
```

## 🧪 Example Prompt Result
Example output includes:
- ✅ Key matched skills (Python, SQL, AWS, Tableau...)
- ❌ Missing skills (LLM integration, security clearance...)
- 📌 Suggestions to update your resume (tailored summary, add skills...)

## 📸 Screenshots
_Add screenshot of app here once running._

## 💼 Resume Tips Integration (Coming Soon)
- Add learning resources for missing skills
- Export match analysis to PDF
- Score your resume (0–100%)

---
Made with ❤️ to help you land the right job.
