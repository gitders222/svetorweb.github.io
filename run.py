# run.py

from app import create_app, db
from app.models import User

# Create the Flask application instance
app = create_app()

# Optional: Create a command-line interface for the Flask app
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)