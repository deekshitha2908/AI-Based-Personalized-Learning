# AI-Based Personalized Learning System

## Project Overview

The AI-Based Personalized Learning System is a web application developed using Python and Streamlit. It allows students to practice quizzes, evaluate their performance, and receive topic-wise feedback and revision recommendations.

The project demonstrates how personalized feedback can help students identify their learning strengths and areas that need improvement.

## Features

- Practice quizzes in Python and Data Structures.
- Multiple-choice questions from a built-in question bank.
- Automatic answer evaluation.
- Topic-wise performance analysis.
- Performance-based feedback and revision recommendations.
- Simple and beginner-friendly user interface.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Libraries:** Random, Streamlit

## Project Structure

```text
AI-Based-Personalized-Learning/
│
├── .gitignore
├── README.md
│
└── app/
    ├── app.py
    ├── README.md
    └── requirements.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Based-Personalized-Learning.git
```

### 2. Navigate to the project folder

```bash
cd AI-Based-Personalized-Learning/app
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

## How It Works

1. The student selects a subject and topic.
2. The application displays questions from its built-in question bank.
3. The student answers the questions.
4. The application evaluates the answers and calculates scores.
5. Topic-wise performance is displayed.
6. The student receives feedback and revision recommendations based on performance.

## Current Implementation

This prototype uses predefined questions and rule-based performance analysis. It does not require an external API key or database.

## Future Enhancements

- Machine-learning-based student performance prediction.
- AI-generated personalized quizzes.
- Student progress tracking.
- More subjects and learning resources.

## Author

Developed as an academic project.