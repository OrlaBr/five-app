import os
# !hiding password
from os import path
if path.exists("env.py"):
    import env
# import tools
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
# creating link to database
app.config["MONGO_DBNAME"] = 'five-app'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# index page
@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html")


# about page
@app.route('/about')
def about():
    return render_template("about.html")


# random page
@app.route('/random')
def random():
    return render_template("random.html")


# add_ram page
@app.route('/add_ram')
def add_ram():
    return render_template('add_ram.html',
                           categories=mongo.db.categories.find())


# tasks page
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

# add tasks page
@app.route('/add_task')
def add_task():
    return render_template('addtask.html',
                           categories=mongo.db.categories.find())

# editing tasks delete, edit add, update task to mongodb
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittask.html', task=the_task,
                            categories=all_categories)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update({'_id': ObjectId(task_id)},
        {
            'task_name': request.form.get('task_name'),
            'category_name': request.form.get('category_name'),
            'task_description': request.form.get('task_description'),
        })
    return redirect(url_for('get_tasks'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))

# getting categories from database
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                            categories=mongo.db.categories.find())

# editing categories update, delete, insert, on database
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                            category=mongo.db.categories.find_one(
                                {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('add_ram'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
