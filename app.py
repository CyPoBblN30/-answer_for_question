from flask import Flask, render_template, request


questions = {}
answers = {}


# создаем объект фласка
app = Flask(__name__)


@app.route("/") # создаем url к следующей функции
def home_page(): # создаем views
    return render_template("index.html")


@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        title = request.form.get("title")
        main_text = request.form.get("main_text")
        questions[title] = main_text
        return render_template("question.html", questions=questions)
    elif request.method == "GET":
        return "так по ссылке переходить нельзя "

@app.route("/answer")
def answer_page():
    return render_template('answer_page.html')


@app.route("/add-answer", methods=["POST", "GET"])
def add_answer():
    if request.method == "POST":
        title = request.form.get("title")
        main_text = request.form.get("main_text")
        answers[title] = main_text
        return render_template("answer.html", answers=answers)
    elif request.method == "GET":
        return "так по ссылке переходить нельзя "


# запуск проекта во время тестирования
app.run(debug=True)

