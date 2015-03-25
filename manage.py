#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from proof_companion import create_app
from proof_companion.core import db
from proof_companion.models import Contact

app = create_app(os.getenv('PROOF_COMP_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, Contact=Contact)

manager.add_command('shell', Shell(make_context=make_shell_context))

@manager.command
def listroutes():
    """
    List routes for app
    """
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint,
                                                        methods,
                                                        rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()
