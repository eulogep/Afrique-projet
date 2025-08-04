from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    user_type = db.Column(db.String(50), nullable=False, default='entrepreneur')  # entrepreneur, investor, expert, organization
    country = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    expertise_areas = db.Column(db.Text, nullable=True)  # JSON string of areas
    investment_capacity = db.Column(db.Float, nullable=True)  # For investors
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_type': self.user_type,
            'country': self.country,
            'bio': self.bio,
            'expertise_areas': self.expertise_areas,
            'investment_capacity': self.investment_capacity,
            'verified': self.verified,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
