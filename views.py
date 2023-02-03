
from flask import Flask, render_template, request, redirect
from models import Tache, db

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        new_tache = Tache(name = name)
        try:
            db.session.add(new_tache)
            db.session.commit()
            return redirect("/")
        except Exception:
            return "!!!"
    else:
        taches = Tache.query.order_by(Tache.created_at)
    return render_template("index.html", taches = taches)

# delete tasks

@app.route("/delete/<int:id>/")
def delete(id):
    tache = Tache.query.get_or_404(id)
    try:
        db.session.delete(tache)
        db.session.commit()
        return redirect("/")
    except Exception:
        return "A problem occured when deleting !!!"


@app.route("/update/<int:id>/", methods = ["GET", "POST"])
def update(id):
    tache = Tache.query.get_or_404(id)
    if request.method == "POST":
        tache.name = request.form["name"]
        try:
            db.session.commit()
            return redirect("/")
        except Exception:
            return "A problem occured when updating !!!"
    else:
        title = "Update"
        return render_template("update.html", title = title, tache = tache)


@app.route("/about/")
def about():
    return render_template("about.html")

