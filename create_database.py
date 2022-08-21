from auction import db, create_app

app =create_app()
context = app.app_context()
context.push()

db.create_all()
