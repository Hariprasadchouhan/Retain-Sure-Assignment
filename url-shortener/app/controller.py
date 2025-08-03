from flask import Blueprint, request, jsonify, redirect, abort, url_for
from .service import (
    shorten_url_service,
    redirect_short_url_service,
    stats_service,
    health_service
)

bp = Blueprint('routes', __name__)

@bp.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json(force=True)
    return shorten_url_service(data)

@bp.route('/<short_code>', methods=['GET'])
def redirect_short_url(short_code):
    return redirect_short_url_service(short_code)

@bp.route('/api/stats/<short_code>', methods=['GET'])
def stats(short_code):
    return stats_service(short_code)

@bp.route('/api/health', methods=['GET'])
def health():
    from .service import health_service
    return health_service()
