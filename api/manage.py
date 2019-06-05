#!/usr/bin/env python
# manage.py


from flask_script import Server, Manager

from project import app, db


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=3300))

@manager.command
def recreate_db():
    """Recreates a database"""
    # db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
