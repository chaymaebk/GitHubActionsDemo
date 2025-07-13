#!/usr/bin/env python3
"""
Test suite for Weather App
"""

import pytest
import json
from weather_web_app_enhanced import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Weather App' in response.data

def test_api_weather_missing_city(client):
    """Test API endpoint without city parameter."""
    response = client.get('/api/weather')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_api_weather_demo_city(client):
    """Test API endpoint with demo city."""
    response = client.get('/api/weather?city=London')
    # Should return either 200 (if API key works) or 404 (demo mode)
    assert response.status_code in [200, 404]

def test_api_weather_with_country(client):
    """Test API endpoint with city and country."""
    response = client.get('/api/weather?city=London&country=GB')
    assert response.status_code in [200, 404]

def test_api_weather_invalid_city(client):
    """Test API endpoint with invalid city."""
    response = client.get('/api/weather?city=InvalidCityName123')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

def test_app_configuration():
    """Test that the app is configured correctly."""
    assert app.config['TESTING'] == True

if __name__ == '__main__':
    pytest.main([__file__]) 