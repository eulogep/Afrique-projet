from src.models.user import db
from datetime import datetime

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    economic_model = db.Column(db.Text, nullable=True)
    profitability_analysis = db.Column(db.Text, nullable=True)
    required_budget = db.Column(db.Float, nullable=True)
    expected_roi = db.Column(db.Float, nullable=True)  # Return on Investment percentage
    implementation_timeline = db.Column(db.String(100), nullable=True)
    target_beneficiaries = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(50), default='proposed')  # proposed, funded, in_progress, completed
    country = db.Column(db.String(100), nullable=True)
    region = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=True)
    
    # Relationship with investments
    investments = db.relationship('Investment', backref='project', lazy=True)

    def __repr__(self):
        return f'<Project {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'economic_model': self.economic_model,
            'profitability_analysis': self.profitability_analysis,
            'required_budget': self.required_budget,
            'expected_roi': self.expected_roi,
            'implementation_timeline': self.implementation_timeline,
            'target_beneficiaries': self.target_beneficiaries,
            'status': self.status,
            'country': self.country,
            'region': self.region,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'created_by': self.created_by,
            'problem_id': self.problem_id,
            'total_investments': sum([inv.amount for inv in self.investments]) if self.investments else 0,
            'investments_count': len(self.investments) if self.investments else 0
        }

