from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def home_page():
    """This is the home page with links to search and add."""

    return render_template("home.html")


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)


    all_grades = hackbright.get_all_grades_by_github(github)
    project_list=[]
    grade_list=[]
    for item in all_grades:
        project_list.append(item[0])
        grade_list.append(item[1])

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            grade_list=grade_list,
                            project_list=project_list)
    return html
    # else: 
    #     # return 




@app.route("/student-add")
def student_add():
    """Add a student."""

    return render_template("student_add.html")


@app.route("/new-student-confirm", methods=["POST"])
def confirm_new_student():
    """Confirm the information about the student just added."""

    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    github = request.form.get('github')

    hackbright.make_new_student(firstname, lastname, github)

    html = render_template("confirm_new_student.html",
                            firstname=firstname,
                            lastname=lastname,
                            github=github)
    return html

if __name__ == "__main__":
    app.run(debug=True)