from flask import Blueprint, request, jsonify, redirect, abort, url_for
from .models import store
from .utils import generate_short_code, is_valid_url

bp = Blueprint('routes', __name__)

@bp.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json(force=True)
    url = data.get('url')
    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    existing_code = store.find_by_url(url)
    if existing_code:
        short_url = url_for('routes.redirect_short_url', short_code=existing_code, _external=True)
        return jsonify({"short_code": existing_code, "short_url": short_url}), 200


    for _ in range(10):
        short_code = generate_short_code()
        if not store.exists(short_code):
            break
    else:
        return jsonify({"error": "Could not generate unique short code"}), 500

    store.add(short_code, url)
    short_url = url_for('routes.redirect_short_url', short_code=short_code, _external=True)
    return jsonify({"short_code": short_code, "short_url": short_url}), 201



@bp.route('/<short_code>', methods=['GET'])
def redirect_short_url(short_code):
    entry = store.get(short_code)
    if not entry:
        abort(404)
    store.increment_click(short_code)
    return redirect(entry["url"])


@bp.route('/api/stats/<short_code>', methods=['GET'])
def stats(short_code):
    entry = store.get(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404
    return jsonify({
        "url": entry["url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"]
    }), 200



@bp.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200
