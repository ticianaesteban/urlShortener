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


@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url, enabled=True).first_or_404()
    return redirect(url.original_url)


@app.route('/api/update/<short_url>', methods=['POST'])
def update_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    print(url)
    new_url = request.json['url']
    url.original_url = new_url
    db.session.commit()
    return jsonify({'short_url': url.short_url, 'original_url': url.original_url})


@app.route('/api/disable/<short_url>', methods=['POST'])
def disable_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    url.enbaled = False
    db.session.commit()
    return jsonify({'short_url': url.short_url, 'original_url': url.original_url})


@app.route('/api/enable/<short_url>', methods=['POST'])
def enable_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    url.enabled = True
    db.session.commit()
    return jsonify({'short_url': url.short_url, 'original_url': url.original_url})
