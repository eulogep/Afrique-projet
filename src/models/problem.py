from src.models.user import db
from datetime import datetime

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # 'socio-economic' or 'security-stability'
    subcategory = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    region = db.Column(db.String(100), nullable=True)
    severity_level = db.Column(db.Integer, default=1)  # 1-5 scale
    affected_population = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    # Relationship with projects
    projects = db.relationship('Project', backref='related_problem', lazy=True)

    def __repr__(self):
        return f'<Problem {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'subcategory': self.subcategory,
            'country': self.country,
            'region': self.region,
            'severity_level': self.severity_level,
            'affected_population': self.affected_population,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'created_by': self.created_by,
            'projects_count': len(self.projects) if self.projects else 0
        }

