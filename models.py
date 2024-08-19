from app import db
import string
import random


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))

        # Asegurarse de que la URL acortada sea únicawhile URL.query.filter_by(short_url=short_url).first():
        short_url = ''.join(random.choice(characters) for _ in range(6))

        return short_url
