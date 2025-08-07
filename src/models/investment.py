from src.models.user import db
from datetime import datetime

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), default='USD')
    investment_type = db.Column(db.String(50), nullable=False)  # loan, grant, equity, donation
    status = db.Column(db.String(50), default='pending')  # pending, approved, disbursed, completed
    terms = db.Column(db.Text, nullable=True)
    expected_return = db.Column(db.Float, nullable=True)
    investment_date = db.Column(db.DateTime, default=datetime.utcnow)
    maturity_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    investor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    
    # Relationships
    investor = db.relationship('User', backref='investments')

    def __repr__(self):
        return f'<Investment {self.amount} {self.currency} for Project {self.project_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'currency': self.currency,
            'investment_type': self.investment_type,
            'status': self.status,
            'terms': self.terms,
            'expected_return': self.expected_return,
            'investment_date': self.investment_date.isoformat() if self.investment_date else None,
            'maturity_date': self.maturity_date.isoformat() if self.maturity_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'investor_id': self.investor_id,
            'project_id': self.project_id
        }

