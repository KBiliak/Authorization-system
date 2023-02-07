from server import app, mysql
from flask import request
from server.db import role_repository


@app.post("/role")
def create_role():
    role = request.get_json()
    print("Create a role:", role)
    role_repository.role_create(mysql, role)
    return role, 201


@app.get("/role")
def get_all_roles():
    role = role_repository.get_role(mysql)
    return role


@app.get("/role/<int:id>")
def get_role_by_id(id):
    print("get role by id", id)
    role = role_repository.get_role_id(mysql, id)
    if role is None:
        return "Not found", 404
    return role


@app.delete("/role/<int:id>")
def delete_role(id):
    print("delete role by id", id)
    role_repository.delete_role_id(mysql, id)
    return {}


@app.put("/role/<int:id>")
def update_role(id):
    role = request.get_json()
    role_repository.update_role_id(mysql, role, id)
    print("Update role by id", id)
    return role, 201
