#!/usr/bin/env python
# manage.py


from flask_script import Server, Manager

from project import app


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=3300))


if __name__ == '__main__':
    manager.run()
