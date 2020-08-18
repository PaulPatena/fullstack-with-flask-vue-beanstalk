from flask import Flask, render_template
from pathlib import Path

transpiled_ui_path = str(Path(__file__).parent / 'dist')

# EB looks for an 'application' callable by default.
application = Flask(__name__, static_folder=transpiled_ui_path, template_folder=transpiled_ui_path)

@application.route('/')
def index():
    return render_template("index.html")

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()