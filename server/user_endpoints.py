from server import app, mysql
from flask import request
import user_repository


@app.post("/user")
def create_user():
    user = request.get_json()
    print("Create a user:", user)
    user_repository.user_create(mysql, user)
    return user, 201


@app.get("/user")
def get_all_users():
    user = user_repository.read_user(mysql)
    return user


@app.get("/user/<int:id>")
def get_user_by_id(id):
    print("get user by id", id)
    user = user_repository.read_user_by_id(mysql, id)
    if user is None:
        return "Not found", 404
    return user


@app.delete("/user/<int:id>")
def delete_user(id):
    print("delete user by id", id)
    user_repository.delete_user_by_id(mysql, id)
    return {}


@app.put("/user/<int:id>")
def update_user(id):
    user = request.get_json()
    user_repository.update_user_by_id(mysql, user, id)
    print("Update a user by id", id)
    return user, 201
