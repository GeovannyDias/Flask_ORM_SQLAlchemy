from app import db

class Users(db.Model):
    # Name Table
    __tablename__ = 'users'
    # Name columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    state = db.Column(db.Boolean())
    token = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    # Method that will run the first time we create a new User
    def __init__(self, firstname, lastname, email, password, state, token,
                 created_at, updated_at):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.state = state
        self.token = token
        self.created_at = created_at
        self.updated_a = updated_at

    # Method to represent the object when we query for it
    def __repr__(self):
        return '<id {}>'.format(self.id)

    # Method to return serialize data
    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'password': self.password,
            'state': self.state,
            'token': self.token,
            'created_at': self.created_at,
            'updated_a': self.updated_a,
            'code': 'OK',
            'message': 'Usuario registrado con exito'
        }
