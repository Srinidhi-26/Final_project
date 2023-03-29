from flask_api import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Invent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accessory = db.Column(db.Text, nullable=False)
    quantity_ordered = db.Column(db.Integer, nullable=False)
    quant_remaining = db.Column(db.Integer, nullable=False)
    vendor_name = db.Column(db.Text, nullable=False)
    cp_accessory = db.Column(db.Integer)
    sp_accessory = db.Column(db.Integer)


