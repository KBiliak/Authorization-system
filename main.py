from flask import Flask, request
from flask_mysqldb import MySQL
import user_repository
import role_repository

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'author_db'

mysql = MySQL(app)


@app.post("/user")
def create_user():
    user = request.get_json()
    print("Create a user:", user)
    user_repository.user_create(mysql, user)
    return user, 201


@app.post("/role")
def create_role():
    role = request.get_json()
    print("Create a role:", role)
    user_repository.role_create(mysql, role)
    return role, 201


@app.get("/user")
def get_all_users():
    user = user_repository.read_user(mysql)
    return user


@app.get("/role")
def get_all_roles():
    role = role_repository.get_role(mysql)
    return role


@app.get("/user/<int:id>")
def get_user_by_id(id):
    print("get user by id", id)
    user = user_repository.read_user_by_id(mysql, id)
    if user is None:
        return "Not found", 404
    return user


@app.get("/role/<int:id>")
def get_role_by_id(id):
    print("get role by id", id)
    role = role_repository.get_role_id(mysql, id)
    if role is None:
        return "Not found", 404
    return role


@app.delete("/user/<int:id>")
def delete_user(id):
    print("delete user by id", id)
    user_repository.delete_user_by_id(mysql, id)
    return {}


@app.delete("/role/<int:id>")
def delete_role(id):
    print("delete role by id", id)
    role_repository.delete_role_id(mysql, id)
    return {}


@app.put("/user/<int:id>")
def update_user(id):
    user = request.get_json()
    user_repository.update_user_by_id(mysql, user, id)
    print("Update a user by id", id)
    return user, 201


@app.put("/role/<int:id>")
def update_role(id):
    role = request.get_json()
    role_repository.update_role_id(mysql, role, id)
    print("Update role by id", id)
    return role, 201
