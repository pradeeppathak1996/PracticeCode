from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

# CREATE
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "address": data.get("address")
    }

    users.append(user)
    return jsonify({"message": "User created", "user": user})

# READ ALL
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# READ SINGLE
@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    if id < len(users):
        return jsonify(users[id])
    return jsonify({"message": "User not found"}), 404

# UPDATE
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    if id < len(users):
        data = request.get_json()

        users[id]["name"] = data.get("name")
        users[id]["email"] = data.get("email")
        users[id]["address"] = data.get("address")

        return jsonify({"message": "User updated", "user": users[id]})
    return jsonify({"message": "User not found"}), 404

# DELETE
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id < len(users):
        users.pop(id)
        return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)