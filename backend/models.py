from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Soba(db.Model):
    __tablename__ = 'sobe'
    
    id = db.Column(db.Integer, primary_key=True)
    broj_sobe = db.Column(db.String(10), unique=True, nullable=False)
    sprat = db.Column(db.Integer, nullable=False)
    kapacitet = db.Column(db.Integer, nullable=False)
    tip_kreveta = db.Column(db.String(50), nullable=False)
    kategorija = db.Column(db.String(30), nullable=False)  # 'Stara soba' ili 'Nova soba'
    napomena = db.Column(db.String(100), nullable=True)     # 'Bide', 'Rezervna'
    status = db.Column(db.String(30), default='Slobodna')   # 'Slobodna', 'Zauzeta', 'Čišćenje'

    def to_dict(self):
        return {
            'id': self.id,
            'broj_sobe': self.broj_sobe,
            'sprat': self.sprat,
            'kapacitet': self.kapacitet,
            'tip_kreveta': self.tip_kreveta,
            'kategorija': self.kategorija,
            'napomena': self.napomena,
            'status': self.status
        }

class Gost(db.Model):
    __tablename__ = 'gosti'
    
    id = db.Column(db.Integer, primary_key=True)
    ime_prezime = db.Column(db.String(100), nullable=False)
    kontakt_telefon = db.Column(db.String(30))
    email = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'ime_prezime': self.ime_prezime,
            'kontakt_telefon': self.kontakt_telefon,
            'email': self.email
        }

class Rezervacija(db.Model):
    __tablename__ = 'rezervacije'
    
    id = db.Column(db.Integer, primary_key=True)
    soba_id = db.Column(db.Integer, db.ForeignKey('sobe.id'), nullable=False)
    gost_id = db.Column(db.Integer, db.ForeignKey('gosti.id'), nullable=False)
    datum_dolaska = db.Column(db.Date, nullable=False)
    datum_odlaska = db.Column(db.Date, nullable=False)
    status_placanja = db.Column(db.String(30), default='Neplaćeno')
    status_rezervacije = db.Column(db.String(30), default='Aktivna')

    def to_dict(self):
        return {
            'id': self.id,
            'soba_id': self.soba_id,
            'gost_id': self.gost_id,
            'datum_dolaska': str(self.datum_dolaska),
            'datum_odlaska': str(self.datum_odlaska),
            'status_placanja': self.status_placanja,
            'status_rezervacije': self.status_rezervacije
        }