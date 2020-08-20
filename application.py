from flask import Flask, render_template, request
from flask_cors import CORS
from pathlib import Path
from blueprints.tasks_bp import tasks_bp
transpiled_ui_path = str(Path(__file__).parent / 'dist')

# EB looks for an 'application' callable by default.
application = Flask(__name__, static_folder=transpiled_ui_path, template_folder=transpiled_ui_path)
application.register_blueprint(tasks_bp)


@application.route('/')
def index():
    return render_template("index.html")


# run the app.
if __name__ == "__main__":
    # Enable CORS only when debugging
    # Allow POSTs via CORS
    application.config['CORS_HEADERS'] = 'Content-Type'
    CORS(application, resources={r"/*": {"origins": "*"}})

    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
