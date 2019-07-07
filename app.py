import os

from app import blueprint
from app.main import create_app
from flask_script import Manager


app = create_app(os.getenv('TOUR_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(host='0.0.0.0')
    

if __name__ == '__main__':
    manager.run()