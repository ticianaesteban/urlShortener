from app import db
import string  # to generate random short URL
import random


class URL(db.Model):
    """
    Database URL model. Stores destination URL and short URL
    id: primary key
    destination_url: destination URL
    short_url: short URL
    enabled: flag to indicate if the URL is enabled
    """
    id = db.Column(db.Integer, primary_key=True)
    destination_url = db.Column(db.String(512), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        # Check if the short URL exists in database
        while URL.query.filter_by(short_url=short_url).first():
            short_url = ''.join(random.choice(characters) for _ in range(6))

        return short_url
