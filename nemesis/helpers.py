import sqlite3
import os
from serverldap import LdapInstance

PATH = os.path.dirname(os.path.abspath(__file__))

def get_username(token):
    c = sqlite_connect()
    cur = c.cursor()
    result = cur.execute("SELECT username FROM auth WHERE token=?", (token,))
    return result.next()[0]


def handle_authentication(args,userid=None):
    if args.has_key("token"):
        token = args["token"]
        instance = LdapInstance(PATH + "/userman")
        teacher_username = get_username(token)
        teacher = instance.is_teacher(teacher_username)
        if userid is not None:
            return teacher and instance.is_teacher_of(teacher_username, userid)
        else:
            return teacher

    return False

def sqlite_connect():
    return sqlite3.connect(PATH + "/db/nemesis.sqlite")

def register_user(teacher_username, college_group, first_name, last_name, email, team):
    conn = sqlite_connect()
    cur = conn.cursor()
    prep_statement = "INSERT INTO registrations (teacher_username, college_group, first_name, last_name, email, team) VALUES (?,?,?,?,?,?)";
    cur.execute(prep_statement, (teacher_username, college_group, first_name, last_name, email, team))
    conn.commit()




