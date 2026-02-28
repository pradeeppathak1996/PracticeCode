from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ------------------ MODEL ------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(100))

# Create tables
with app.app_context():
    db.create_all()

# ------------------ CREATE ------------------

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()

    user = User(
        name=data.get("name"),
        email=data.get("email"),
        address=data.get("address")
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201

# ------------------ READ ALL ------------------
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []

    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "address": u.address
        })

    return jsonify(result)

# ------------------ READ SINGLE ------------------
@app.route("/user/<int:id>", methods=["GET"])
def get_single_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "address": user.address
    })

# ------------------ UPDATE ------------------
@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()

    user.name = data.get("name")
    user.email = data.get("email")
    user.address = data.get("address")

    db.session.commit()
    return jsonify({"message": "User updated"})

# ------------------ DELETE ------------------
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)