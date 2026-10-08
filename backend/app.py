from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Soba, Gost, Rezervacija

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recepcija.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# API RUTA: Dohvati sve sobe
@app.route('/api/sobe', methods=['GET'])
def get_sobe():
    sobe = Soba.query.all()
    return jsonify([soba.to_dict() for soba in sobe])

# API RUTA: Promijeni status sobe (Slobodna / Zauzeta / Čišćenje)
@app.route('/api/sobe/<int:id>/status', methods=['PATCH'])
def update_status_sobe(id):
    data = request.json
    soba = Soba.query.get_or_404(id)
    soba.status = data.get('status', soba.status)
    db.session.commit()
    return jsonify(soba.to_dict())

if __name__ == '__main__':
    app.run(debug=True, port=5000)