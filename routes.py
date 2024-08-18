from app import create_app, db
from flask import jsonify, request, redirect
from models import URL

app = create_app()


@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json['url']
    url = URL(original_url=original_url)
    db.session.add(url)
    db.session.commit()
    return jsonify({'short_url': url.short_url}), 201

# Ruta para redirigir a la URL original


@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    print(url.original_url)
    return redirect(url.original_url)


@app.route('/api/update/<short_url>', methods=['POST'])
def update_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    new_url = request.json['url']
    url.assign_new_url(new_url)
    db.session.commit()
    return jsonify({'short_url': url.short_url})
