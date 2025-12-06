from flask import Flask, request, jsonify

app = Flask(__name__)

users = []   # simple list

# CREATE
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    users.append(data)      # directly add
    return {"message": "User created"}


# READ ALL
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# READ SINGLE (using list index as id)
@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    if id < len(users):
        return jsonify(users[id])
    return {"message": "User not found"}, 404

# UPDATE
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    if id < len(users):
        users[id] = request.json
        return {"message": "User updated"}
    return {"message": "User not found"}, 404


# DELETE
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id < len(users):
        users.pop(id)
        return {"message": "User deleted"}
    return {"message": "User not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)