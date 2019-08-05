import jester, db_postgres

let db = open("localhost", "rocio", "password", "database")

routes:
  get "/":
    resp $db.getAllRows(sql"select now();")

db.close()