from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/explain-code', methods=['POST'])
def explain():

    code = request.form['code']
    language = request.form['language']

    if code == '' or language == '':
        explanation = "Please enter both code and language to get an explanation."
    else:
        prompt = f"""
You are an expert programming teacher.

Explain the following {language} code clearly in simple English.

Code:
{code}

Explain:
1. What the code does
2. Important functions or logic
3. Step-by-step working
4. Suggestions for improvement
"""

        response = ollama.chat(
            model='qwen2.5-coder:1.5b',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        explanation = response['message']['content']

    return render_template(
        'index.html',
        explanation=explanation,
        code=code
    )


if __name__ == '__main__':
    app.run(debug=True)