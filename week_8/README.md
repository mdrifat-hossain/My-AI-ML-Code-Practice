# AI Agent: LinkedIn Post Generator (Module 21)

An AI Agent built with **LangChain** that generates professional, structured LinkedIn posts
from a topic and a target language — powered by **Google Gemini's free tier** (no credit card
required).

## 🎯 Objective
Given a **topic** (e.g., "AI in Healthcare") and a **language** (e.g., English, Bengali,
Spanish), the agent uses a LangChain LLM Chain to produce a 2–4 paragraph, ready-to-publish
LinkedIn post.

## 🧠 How it works
1. A `PromptTemplate` defines the agent's role, instructions, and desired output structure
   (hook → body → call-to-action → hashtags).
2. An `LLMChain` binds that template to an LLM (`ChatGoogleGenerativeAI`, `gemini-2.5-flash`
   by default — free tier).
3. `generate_linkedin_post(topic, language)` fills in the template and returns the model's
   output as a clean string.

## 📁 Files
| File | Purpose |
|---|---|
| `AI_LinkedIn_Post_Agent.ipynb` | Main notebook — run in Google Colab or Jupyter |
| `agent.py` | Equivalent standalone script — run locally (VS Code / terminal) |
| `requirements.txt` | Python dependencies |

## 🔑 Get a free API key
1. Go to https://aistudio.google.com/apikey
2. Sign in with a Google account and click "Create API key" — free, no credit card.

## ▶️ Run it in Google Colab (recommended for the demo)
1. Upload `AI_LinkedIn_Post_Agent.ipynb` to Colab (or open it from this GitHub repo via
   File → Open Notebook → GitHub).
2. Run cells top to bottom.
3. When prompted, paste your free Gemini API key.
4. Use the final interactive cell to generate a post from your own topic + language.

## ▶️ Run it locally (VS Code)
```bash
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_key_here" > .env
python agent.py
```

## 🔁 Swapping the LLM provider
LangChain makes the model swappable. Replace the `llm = ChatGoogleGenerativeAI(...)` line with, e.g.:
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")   # paid
```
or
```python
from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile")   # also has a free tier
```
Everything else (prompt template, chain, function) stays the same.

## 📽️ Demo video checklist
- Explain the objective (10–15 sec)
- Show the prompt template + chain code (20–30 sec)
- Run the agent live with an English topic
- Run it again with a non-English language (e.g., Bengali) to prove multilingual support
- Show the final formatted post (hook, body, hashtags)
