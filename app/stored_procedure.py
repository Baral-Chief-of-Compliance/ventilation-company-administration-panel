from app import mysql


def call_stored_procedure(name_of_procedure, *args, commit, fetchall):

    cur = mysql.connection.cursor()

    cur.callproc(name_of_procedure, *args)

    if commit:
        cur.close()

        mysql.connection.commit()

        result_of_procedure = None
    else:

        if fetchall:
            result_of_procedure = cur.fetchall()
            cur.close()
        else:
            result_of_procedure = cur.fetchone()
            cur.close()

    return result_of_procedure
