def role_create(mysql, role):
    with mysql.connection.cursor() as cursor:
        sql = f"insert into role(name) value('{role['name']}')"
        cursor.execute(sql)
        mysql.connection.commit()


def get_role(mysql):
    with mysql.connection.cursor() as cursor:
        cursor.execute("select * from role")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            role = {
                "id": row[0],
                "name": row[1]
            }
            result.append(role)
    return result

def get_role_id(mysql, id):
    with mysql.connection.cursor() as cursor:
        sql = f"select * from role where id = {id}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) == 0:
            return None
        row = rows[0]
        role = {
            "id": row[0],
            "name": row[1]
        }
        return role

def delete_role_id(mysql, id):
    with mysql.connection.cursor() as cursor:
        cursor.execute(f"delete from role where id = {id}")
        mysql.connection.commit()

def update_role_id(mysql, role, id):
    with mysql.connection.cursor() as cursor:
        sql = f"update role set name = '{role['name']}' where id = {id}"
        cursor.execute(sql)
        mysql.connection.commit()