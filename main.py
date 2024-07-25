from flask import Flask
from flask_cors import CORS
from controllers.facts_controller import fact_bp
from controllers.user_controller import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(fact_bp)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")