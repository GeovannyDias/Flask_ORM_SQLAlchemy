from app import db


class Inscriptions(db.Model):
    __tablename__ = 'inscriptions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    FK_inscriptions_users = db.relationship('Users', foreignKeys=[user_id])
    FK_inscriptions_subjects = db.relationship('Subjects', foreignKeys=[subject_id])

    def __init__(self, state, user_id, subject_id, created_at, updated_at):
        self.state = state
        self.user_id = user_id
        self.subject_id = subject_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
   