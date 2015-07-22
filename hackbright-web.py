from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add")
def student_add():
    """Add a student."""

    return render_template("student_add.html")


@app.route("/new-student-confirm", methods=["POST"])
def confirm_new_student():
    """Confirm the information about the student just added."""

    info = request.form.get('fname', 'lname', 'github')
    firstname, lastname, github = info
    html = render_template("confirm_new_student.html",
                            firstname=firstname,
                            lastname=lastname,
                            github=github)
    return html

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html


if __name__ == "__main__":
    app.run(debug=True)