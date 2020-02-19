"""
Questions format:
[{id: str, submission_time: time_stamp (int), view_number: int, vote_number: int, title: str, message: str, image: url(str)},
...
]

Answers format:
[{id: str,submission_time: time_stamp (int), vote_number: int, question_id: int, message: str, image: url(str)},
...
]
"""

from flask import Flask, render_template, request, redirect
import data_manager
import util
import time

app = Flask(__name__)


@app.route("/")
def start():

    sorted_questions = sorted(data_manager.QUESTIONS, key= lambda i: i['submission_time'], reverse=1)
    return render_template("index.html", sorted_questions=sorted_questions)

@app.route("/list")
def show_questions_list():
    sorted_questions = sorted(data_manager.QUESTIONS, key= lambda i: i['submission_time'], reverse=1)
    return render_template("list.html", sorted_questions = sorted_questions )

@app.route("/list/<sorted_by>/<int:direction>")
def show_questions(sorted_by,direction):
    sorted_questions = sorted(data_manager.QUESTIONS, key= lambda i: i[sorted_by], reverse= direction)
    return render_template("list.html", sorted_questions=sorted_questions)



@app.route("/questions/<question_id>")
def show_answers(question_id):
    question_title = data_manager.QUESTIONS[int(question_id)]['title']
    question_message = data_manager.QUESTIONS[int(question_id)]['message']
    answers = util.find_answers_by_question(question_id, data_manager.ANSWERS)

    return render_template('questions.html', question_title=question_title,
                           question_message=question_message, answers=answers)


@app.route("/answer")
@app.route("/answer/<answer_id>")
def add_answer(answer_id=None):
    return 'Test'



if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000
    )