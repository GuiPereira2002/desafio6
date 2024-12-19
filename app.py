from flask import Flask
from routes.pessoa_fisica_routes import pessoa_fisica_bp
from routes.pessoa_juridica_routes import pessoa_juridica_bp

app = Flask(__name__)

# Registrando rotas
app.register_blueprint(pessoa_fisica_bp, url_prefix="/pessoa-fisica")
app.register_blueprint(pessoa_juridica_bp, url_prefix="/pessoa-juridica")

if __name__ == "__main__":
    app.run(debug=True)
