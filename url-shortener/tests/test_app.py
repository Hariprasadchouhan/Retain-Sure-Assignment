import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_health(client):
    resp = client.get('/api/health')
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_shorten_and_redirect(client):
    url = "https://www.example.com/test"
    resp = client.post('/api/shorten', json={"url": url})
    assert resp.status_code == 201
    data = resp.get_json()
    short_code = data["short_code"]
    short_url = data["short_url"]

    # Redirect
    resp2 = client.get(f"/{short_code}", follow_redirects=False)
    assert resp2.status_code == 302
    assert resp2.headers["Location"] == url

def test_invalid_url(client):
    resp = client.post('/api/shorten', json={"url": "not-a-url"})
    assert resp.status_code == 400

def test_stats(client):
    url = "https://www.example.com/analytics"
    resp = client.post('/api/shorten', json={"url": url})
    short_code = resp.get_json()["short_code"]

    # Click once
    client.get(f"/{short_code}")
    stats = client.get(f"/api/stats/{short_code}")
    data = stats.get_json()
    assert data["url"] == url
    assert data["clicks"] == 1
    assert "created_at" in data

def test_404(client):
    resp = client.get("/api/stats/doesnotexist")
    assert resp.status_code == 404
    resp2 = client.get("/doesnotexist")
    assert resp2.status_code == 404
