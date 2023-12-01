import os
print("Current working directory:", os.getcwd())
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # You can customize this with your resume content
    resume = {
        'name': 'Your Name',
        'title': 'Your Title',
        'education': 'Your Education',
        'experience': [
            {'position': 'Job Title 1', 'company': 'Company 1', 'year': 'Year 1'},
            {'position': 'Job Title 2', 'company': 'Company 2', 'year': 'Year 2'},
            # Add more experiences as needed
        ],
        'skills': ['Skill 1', 'Skill 2', 'Skill 3'],
        'contact': {
            'email': 'your@email.com',
            'phone': '123-456-7890',
            'github': 'your-github',
            'linkedin': 'your-linkedin',
        }
    }
    return render_template('resume.html', resume=resume)

if __name__ == '__main__':
    app.run(debug=True)

