
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ccreating Column Tache for tasks

class Tache(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    created_at = db.Column(
        db.DateTime, nullable = False, default = datetime.utcnow)
    
    def __repr__(self):
        return f"Todo {self.name}"
