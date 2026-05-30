# Explain My Code

## Overview

Explain My Code is an AI-powered web application that helps developers and students understand source code by generating simple, human-readable explanations. Users can paste code snippets, select the programming language, and receive an AI-generated explanation describing the code's functionality, logic, workflow, and possible improvements.

The application uses Flask as the backend framework and Ollama with the Qwen 2.5 Coder model for local AI inference, allowing code explanations without relying on external APIs or internet connectivity after setup.

---

## Features

- AI-powered code explanation
- Supports multiple programming languages
- Simple and responsive user interface
- Local AI processing using Ollama
- Privacy-friendly (code never leaves your machine)
- No API costs or rate limits
- Step-by-step explanation generation
- Suggestions for code improvement
- Modern Bootstrap-based design

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- HTMX
- JavaScript

### Backend
- Python
- Flask

### Artificial Intelligence
- Ollama
- Qwen 2.5 Coder 1.5B

---

## Project Architecture

```text
User
 │
 ▼
Frontend (HTML + Bootstrap + HTMX)
 │
 ▼
Flask Backend
 │
 ▼
Ollama
 │
 ▼
Qwen 2.5 Coder 1.5B
 │
 ▼
Generated Explanation
```

---

## Installation

### Step 1: Install Python

Download and install Python:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

### Step 2: Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

### Step 3: Download the AI Model

Open Command Prompt or Terminal and run:

```bash
ollama pull qwen2.5-coder:1.5b
```

Verify the model:

```bash
ollama list
```

---

### Step 4: Install Project Dependencies

Navigate to the project directory:

```bash
cd ExplainMyCode
```

Install required packages:

```bash
pip install flask ollama
```

---

## Running the Application

### Start Flask

```bash
python app.py
```

You should see:

```text
Running on http://127.0.0.1:5000
```

Open the URL in your browser.

---

## Usage

1. Open the application.
2. Select a programming language.
3. Paste your source code.
4. Click **Explain Code**.
5. Wait for the AI model to analyze the code.
6. Read the generated explanation.

---

## Example

### Input Code

```python
def greet(name):
    return f"Hello, {name}"

print(greet("John"))
```

### Generated Explanation

**What the code does**

This code defines a function named `greet` that accepts a parameter called `name` and returns a greeting message. The function is then called with the value `"Jewel"` and the result is printed.

**Step-by-step working**

1. The function `greet()` is created.
2. The parameter `name` receives the value `"Jewel"`.
3. A formatted greeting string is generated.
4. The function returns the greeting.
5. The greeting is printed to the console.

**Suggestions**

- Add comments to improve readability.
- Include input validation if necessary.

---

## Supported Programming Languages

- JavaScript
- Java
- Python
- C#
- C++
- C
- PHP
- Go
- Ruby
- TypeScript
- Swift
- Kotlin
- Rust
- Dart

---

## Advantages

- Completely free to use
- No external API dependency
- No token usage costs
- Works offline
- Secure and privacy-friendly
- Easy to deploy locally
- Fast response times for small code snippets

---

## Future Enhancements

- Syntax highlighting
- Chat-style AI explanations
- Code optimization suggestions
- Bug detection and debugging hints
- Explanation history
- Save explanations as PDF
- Multiple AI model support
- Theme customization
- File upload support
- Source code download

---

### Example Markdown Screenshot Embedding




---

## Learning Outcomes

This project demonstrates:

- Flask web development
- AI integration using Ollama
- Prompt engineering
- Frontend and backend communication
- Form handling in Flask
- Local LLM deployment
- Responsive web design

---

This project is developed for educational, learning, and portfolio purposes.

---
