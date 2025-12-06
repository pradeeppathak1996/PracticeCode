from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite DB (simple)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Model (Table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

# Create DB
with app.app_context():
    db.create_all()


# ------------------ CREATE ------------------
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


# -------------------- READ --------------------

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []

    for u in users:
        output.append({
            "id": u.id,
            "name": u.name,
            "email": u.email
        })

    return jsonify(output)

# --------------------Single READ --------------------

@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    user = User.query.get(id)

    if not user:
        return {"message": "User not found"}, 404

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

# -------------------- UPDATE --------------------

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    data = request.json

    user.name = data["name"]
    user.email = data["email"]

    db.session.commit()

    return jsonify({"message": "User updated"})


# -------------------- DELETE --------------------

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)