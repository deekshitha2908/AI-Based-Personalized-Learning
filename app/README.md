# Personalized Learning Website — Free Version

This Streamlit app uses a built-in question bank instead of the OpenAI API.

## Features
- Python and Data Structures quizzes
- Select up to five topics
- Multiple-choice questions
- Automatic scoring and topic-wise feedback
- Rule-based revision recommendations
- No API key, API credits, or database required

## Available topics
- Python: Variables, Conditions, Loops, Functions, Lists
- Data Structures: Arrays, Linked Lists, Stacks, Queues, Trees

## Run on Windows / VS Code
Open PowerShell in this folder, then run:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown by Streamlit, usually http://localhost:8501.

Questions are predefined and can be expanded or reviewed against your course material. The quiz provides practice feedback, not a complete measure of ability.
