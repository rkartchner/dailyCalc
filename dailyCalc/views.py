import functools, random
from datetime import date
from . import exerciseList
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

from . import db

bp = Blueprint('views', __name__)

'''
@bp.route('/')
def index():
	exercises = exerciseList.generateList()
	checkedList = [{'id':1,'name':x,'checked':False} for x in exercises]
	return render_template('index.html',items=checkedList)
'''

@bp.route('/', methods=["GET"])
@bp.route('/home', methods=["GET"])
def home():
	checklist = exerciseList.generateList()
	return render_template('index.html',items=checklist)
'''
    if request.method == "POST":
        todo_name = request.form["todo_name"]
        if todo_name:
            moreExercises = exerciseList.generateList()
            moreList  = [{'id':random.randint(1,1000),'name':x,'checked':False} for x in moreExercises]
            return render_template('index.html', items=checkedList)
    defaultExercises = exerciseList.generateList()
    checkedList = [{'id': 1, 'name': x, 'checked': False} for x in defaultExercises]
    return render_template('index.html', items=checkedList)
'''

@bp.route("/checked/<int:todo_id>", methods=["POST"])
def checked_todo(todo_id):

	checklist = exerciseList.generateList()

	for todo in checklist:
		if todo['id'] == todo_id:
			todo['checked'] = not todo['checked']
			if todo['checked']:
				daba = db.get_db()
				daba.execute("INSERT OR IGNORE INTO exercises (exercisenumber, checked_on) VALUES (?,?)",(todo['name'], date.today()))
				daba.commit()
			break
	exerciseList.saveChecklist(checklist)
	return redirect(url_for("views.home"))

@bp.route('/more_work', methods=["POST"])
def add_more_work():
	exerciseList.moreWork()
	return redirect(url_for('views.home'))

@bp.route("/history")
def history():
	daba = db.get_db()
	rows = daba.execute("SELECT exercisenumber, checked_on FROM exercises ORDER BY checked_on DESC").fetchall()
	return render_template("history.html", items=rows)
