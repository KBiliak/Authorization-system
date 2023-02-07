def user_create(mysql, user):
    with mysql.connection.cursor() as cursor:
        sql = f"insert into user(first_name, last_name, position, role)" \
              f" value('{user['first_name']}'," \
              f" '{user['last_name']}', " \
              f"'{user['position']}'," \
              f" '{user['role']}')"
        cursor.execute(sql)
        mysql.connection.commit()


def role_create(mysql, role):
    with mysql.connection.cursor() as cursor:
        sql = f"insert into role(name) value('{role['name']}')"
        cursor.execute(sql)
        mysql.connection.commit()


def read_user(mysql):
    with mysql.connection.cursor() as cursor:
        cursor.execute(f"select * from user")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            user = {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "position": row[3],
                "role": row[4]
            }
            result.append(user)
    return result


def read_user_by_id(mysql, id):
    with mysql.connection.cursor() as cursor:
        cursor.execute(f"select * from user where id = {id}")
        rows = cursor.fetchall()
        if len(rows) == 0:
            return None
        row = rows[0]
        user = {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "position": row[3],
            "role": row[4]
        }
        return user


def delete_user_by_id(mysql, id):
    with mysql.connection.cursor() as cursor:
        sql = f"delete  from user where id = {id}"
        cursor.execute(sql)
        mysql.connection.commit()


def update_user_by_id(mysql, user, id):
    with mysql.connection.cursor() as cursor:
        sql = f"update user set first_name = '{user['first_name']}', " \
              f"last_name = '{user['last_name']}', " \
              f"position = '{user['position']}', " \
              f"role = '{user['role']}' where id = {id}"
        cursor.execute(sql)
        mysql.connection.commit()
