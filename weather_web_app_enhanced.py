#!/usr/bin/env python3
"""
Enhanced Weather Web App
Option 1: More demo cities
Option 2: Real API integration
"""

from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import requests
import os

app = Flask(__name__)

# OpenWeatherMap API key (replace with your own)
API_KEY = '7ec7dd35b9c60e4a1768a3d26ae779ee'  # Your actual API key
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Enhanced demo data with more popular cities
DEMO_DATA = {
    # Europe
    "london,gb": {"name": "London", "country": "United Kingdom", "weather": [{"main": "Clouds", "description": "broken clouds", "icon": "04d"}], "main": {"temp": 15, "feels_like": 13, "humidity": 72, "pressure": 1013}, "wind": {"speed": 5.2}, "visibility": 10000},
    "paris,fr": {"name": "Paris", "country": "France", "weather": [{"main": "Clouds", "description": "partly cloudy", "icon": "02d"}], "main": {"temp": 20, "feels_like": 22, "humidity": 68, "pressure": 1018}, "wind": {"speed": 3.5}, "visibility": 15000},
    "rome,it": {"name": "Rome", "country": "Italy", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 25, "feels_like": 27, "humidity": 60, "pressure": 1020}, "wind": {"speed": 2.8}, "visibility": 16000},
    "madrid,es": {"name": "Madrid", "country": "Spain", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 26, "feels_like": 28, "humidity": 55, "pressure": 1019}, "wind": {"speed": 3.2}, "visibility": 18000},
    "berlin,de": {"name": "Berlin", "country": "Germany", "weather": [{"main": "Clouds", "description": "overcast clouds", "icon": "04d"}], "main": {"temp": 18, "feels_like": 19, "humidity": 75, "pressure": 1015}, "wind": {"speed": 4.1}, "visibility": 12000},
    "amsterdam,nl": {"name": "Amsterdam", "country": "Netherlands", "weather": [{"main": "Rain", "description": "light rain", "icon": "10d"}], "main": {"temp": 16, "feels_like": 15, "humidity": 85, "pressure": 1010}, "wind": {"speed": 5.5}, "visibility": 8000},
    
    # North America
    "new york,us": {"name": "New York", "country": "United States", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 22, "feels_like": 24, "humidity": 55, "pressure": 1020}, "wind": {"speed": 3.8}, "visibility": 16000},
    "los angeles,us": {"name": "Los Angeles", "country": "United States", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 28, "feels_like": 30, "humidity": 45, "pressure": 1022}, "wind": {"speed": 2.5}, "visibility": 20000},
    "chicago,us": {"name": "Chicago", "country": "United States", "weather": [{"main": "Snow", "description": "light snow", "icon": "13d"}], "main": {"temp": 2, "feels_like": -2, "humidity": 80, "pressure": 1008}, "wind": {"speed": 6.2}, "visibility": 5000},
    "toronto,ca": {"name": "Toronto", "country": "Canada", "weather": [{"main": "Clouds", "description": "few clouds", "icon": "02d"}], "main": {"temp": 10, "feels_like": 8, "humidity": 70, "pressure": 1016}, "wind": {"speed": 4.5}, "visibility": 14000},
    "mexico city,mx": {"name": "Mexico City", "country": "Mexico", "weather": [{"main": "Clouds", "description": "scattered clouds", "icon": "03d"}], "main": {"temp": 24, "feels_like": 26, "humidity": 62, "pressure": 1012}, "wind": {"speed": 3.0}, "visibility": 13000},
    
    # Asia
    "tokyo,jp": {"name": "Tokyo", "country": "Japan", "weather": [{"main": "Rain", "description": "light rain", "icon": "10d"}], "main": {"temp": 18, "feels_like": 19, "humidity": 85, "pressure": 1008}, "wind": {"speed": 2.5}, "visibility": 8000},
    "beijing,cn": {"name": "Beijing", "country": "China", "weather": [{"main": "Haze", "description": "haze", "icon": "50d"}], "main": {"temp": 12, "feels_like": 10, "humidity": 65, "pressure": 1018}, "wind": {"speed": 1.8}, "visibility": 6000},
    "mumbai,in": {"name": "Mumbai", "country": "India", "weather": [{"main": "Clouds", "description": "broken clouds", "icon": "04d"}], "main": {"temp": 32, "feels_like": 38, "humidity": 78, "pressure": 1005}, "wind": {"speed": 4.2}, "visibility": 9000},
    "seoul,kr": {"name": "Seoul", "country": "South Korea", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 15, "feels_like": 16, "humidity": 58, "pressure": 1020}, "wind": {"speed": 2.9}, "visibility": 15000},
    "bangkok,th": {"name": "Bangkok", "country": "Thailand", "weather": [{"main": "Thunderstorm", "description": "thunderstorm", "icon": "11d"}], "main": {"temp": 35, "feels_like": 42, "humidity": 88, "pressure": 1002}, "wind": {"speed": 1.5}, "visibility": 7000},
    
    # Africa
    "rabat,ma": {"name": "Rabat", "country": "Morocco", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 28, "feels_like": 30, "humidity": 65, "pressure": 1015}, "wind": {"speed": 4.1}, "visibility": 12000},
    "cairo,eg": {"name": "Cairo", "country": "Egypt", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 35, "feels_like": 38, "humidity": 35, "pressure": 1018}, "wind": {"speed": 3.5}, "visibility": 18000},
    "lagos,ng": {"name": "Lagos", "country": "Nigeria", "weather": [{"main": "Rain", "description": "heavy rain", "icon": "09d"}], "main": {"temp": 28, "feels_like": 33, "humidity": 92, "pressure": 1008}, "wind": {"speed": 2.8}, "visibility": 4000},
    "cape town,za": {"name": "Cape Town", "country": "South Africa", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 22, "feels_like": 24, "humidity": 55, "pressure": 1020}, "wind": {"speed": 5.2}, "visibility": 16000},
    
    # South America
    "sao paulo,br": {"name": "São Paulo", "country": "Brazil", "weather": [{"main": "Rain", "description": "moderate rain", "icon": "10d"}], "main": {"temp": 25, "feels_like": 28, "humidity": 85, "pressure": 1010}, "wind": {"speed": 3.2}, "visibility": 8000},
    "buenos aires,ar": {"name": "Buenos Aires", "country": "Argentina", "weather": [{"main": "Clouds", "description": "few clouds", "icon": "02d"}], "main": {"temp": 20, "feels_like": 21, "humidity": 68, "pressure": 1016}, "wind": {"speed": 4.0}, "visibility": 14000},
    "lima,pe": {"name": "Lima", "country": "Peru", "weather": [{"main": "Mist", "description": "mist", "icon": "50d"}], "main": {"temp": 19, "feels_like": 20, "humidity": 82, "pressure": 1014}, "wind": {"speed": 2.1}, "visibility": 10000},
    
    # Oceania
    "sydney,au": {"name": "Sydney", "country": "Australia", "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}], "main": {"temp": 26, "feels_like": 28, "humidity": 60, "pressure": 1018}, "wind": {"speed": 3.8}, "visibility": 17000},
    "auckland,nz": {"name": "Auckland", "country": "New Zealand", "weather": [{"main": "Rain", "description": "light rain", "icon": "10d"}], "main": {"temp": 16, "feels_like": 17, "humidity": 80, "pressure": 1012}, "wind": {"speed": 4.5}, "visibility": 11000},
}

def get_weather_icon(icon_code):
    """Return emoji icon based on weather code"""
    icon_map = {
        '01d': '☀️', '01n': '🌙', '02d': '⛅', '02n': '⛅',
        '03d': '☁️', '03n': '☁️', '04d': '☁️', '04n': '☁️',
        '09d': '🌧️', '09n': '🌧️', '10d': '🌦️', '10n': '🌦️',
        '11d': '⛈️', '11n': '⛈️', '13d': '❄️', '13n': '❄️',
        '50d': '🌫️', '50n': '🌫️'
    }
    return icon_map.get(icon_code, '🌤️')

def fetch_real_weather(city, country=''):
    """Fetch weather from real OpenWeatherMap API"""
    if API_KEY == 'demo_key':
        return None
    
    try:
        query = f"{city},{country}" if country else city
        params = {
            'q': query,
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(API_URL, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

def get_popular_cities():
    """Get list of popular cities for demo buttons"""
    popular = [
        ('London', 'GB'), ('Paris', 'FR'), ('New York', 'US'), ('Tokyo', 'JP'),
        ('Rome', 'IT'), ('Madrid', 'ES'), ('Berlin', 'DE'), ('Mumbai', 'IN'),
        ('Sydney', 'AU'), ('Toronto', 'CA'), ('Bangkok', 'TH'), ('Cairo', 'EG'),
        ('São Paulo', 'BR'), ('Mexico City', 'MX'), ('Seoul', 'KR'), ('Rabat', 'MA')
    ]
    return popular

@app.route('/')
def index():
    """Main page with enhanced interface"""
    popular_cities = get_popular_cities()
    api_status = "Real API" if API_KEY != 'demo_key' else "Demo Mode"
    
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌤️ Global Weather App</title>
    <style>
        * {
            margin: 0; padding: 0; box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; color: #333; padding: 20px;
        }
        
        .container { max-width: 800px; margin: 0 auto; }
        
        .header {
            text-align: center; margin-bottom: 30px;
        }
        
        .header h1 {
            color: white; font-size: 2.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin-bottom: 10px;
        }
        
        .api-status {
            background: rgba(255,255,255,0.2); color: white; padding: 8px 16px;
            border-radius: 20px; font-size: 0.9rem; margin-bottom: 20px;
        }
        
        .search-section {
            background: white; padding: 30px; border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin-bottom: 30px;
        }
        
        .form-row {
            display: flex; gap: 15px; margin-bottom: 20px;
        }
        
        .form-group {
            flex: 1;
        }
        
        label {
            display: block; margin-bottom: 8px; font-weight: bold; color: #333;
        }
        
        input[type="text"] {
            width: 100%; padding: 12px; border: 2px solid #e0e0e0;
            border-radius: 8px; font-size: 16px; transition: border-color 0.3s;
        }
        
        input[type="text"]:focus {
            outline: none; border-color: #667eea;
        }
        
        .search-btn {
            width: 100%; padding: 15px; background: #667eea; color: white;
            border: none; border-radius: 8px; font-size: 16px; font-weight: bold;
            cursor: pointer; transition: background 0.3s;
        }
        
        .search-btn:hover { background: #5a67d8; }
        
        .popular-cities {
            margin-top: 20px;
        }
        
        .popular-cities h3 {
            margin-bottom: 15px; color: #333; text-align: center;
        }
        
        .cities-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 10px; max-height: 200px; overflow-y: auto;
        }
        
        .city-btn {
            background: #f8f9fa; border: 1px solid #ddd; padding: 8px 12px;
            border-radius: 6px; cursor: pointer; font-size: 12px;
            transition: all 0.3s; text-align: center;
        }
        
        .city-btn:hover {
            background: #e9ecef; transform: translateY(-2px);
        }
        
        .weather-container {
            background: white; border-radius: 15px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.2); overflow: hidden;
            min-height: 300px; display: flex; align-items: center; justify-content: center;
        }
        
        .loading {
            text-align: center; color: #666; font-size: 18px;
        }
        
        .weather-info {
            padding: 30px; width: 100%; display: none;
        }
        
        .weather-info.active { display: block; }
        
        .location {
            text-align: center; margin-bottom: 25px;
        }
        
        .location h2 {
            font-size: 2rem; color: #333; margin-bottom: 5px;
        }
        
        .location p {
            color: #666; font-size: 1.1rem;
        }
        
        .current-weather {
            text-align: center; margin-bottom: 30px; padding: 20px;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px;
        }
        
        .weather-icon { font-size: 4rem; margin-bottom: 10px; }
        .temperature { font-size: 3rem; font-weight: bold; color: #667eea; margin-bottom: 10px; }
        .description { font-size: 1.3rem; font-weight: bold; color: #333; text-transform: capitalize; margin-bottom: 5px; }
        .feels-like { color: #666; font-size: 1rem; }
        
        .weather-stats {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px;
        }
        
        .stat {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef); padding: 15px;
            border-radius: 10px; text-align: center; transition: transform 0.3s ease;
        }
        
        .stat:hover { transform: translateY(-5px); }
        .stat-icon { font-size: 1.5rem; margin-bottom: 5px; }
        .stat-label { font-size: 0.9rem; color: #666; margin-bottom: 5px; }
        .stat-value { font-weight: bold; color: #333; }
        
        .error-message {
            text-align: center; color: #e74c3c; display: none; padding: 30px;
        }
        
        .error-message.active { display: block; }
        
        .timestamp {
            text-align: center; color: #999; font-size: 0.9rem; margin-top: 20px;
        }
        
        .info-box {
            background: rgba(255,255,255,0.1); color: white; padding: 15px;
            border-radius: 10px; margin-bottom: 20px; text-align: center;
        }
        
        @media (max-width: 768px) {
            .form-row { flex-direction: column; }
            .cities-grid { grid-template-columns: repeat(3, 1fr); }
            .weather-stats { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌤️ Global Weather App</h1>
            <div class="api-status">Status: {{ api_status }}</div>
        </div>
        
        {% if api_status == "Demo Mode" %}
        <div class="info-box">
            <strong>Demo Mode:</strong> Showing {{ demo_cities_count }} popular cities. 
            <br>For unlimited cities, add your OpenWeatherMap API key!
        </div>
        {% endif %}
        
        <div class="search-section">
            <form id="weatherForm">
                <div class="form-row">
                    <div class="form-group">
                        <label for="city">City:</label>
                        <input type="text" id="city" name="city" placeholder="Enter city name..." required>
                    </div>
                    <div class="form-group">
                        <label for="country">Country (optional):</label>
                        <input type="text" id="country" name="country" placeholder="Country code (e.g., US, FR, MA)">
                    </div>
                </div>
                <button type="submit" class="search-btn">🔍 Get Weather</button>
            </form>
            
            <div class="popular-cities">
                <h3>Popular Cities ({{ demo_cities_count }} available):</h3>
                <div class="cities-grid">
                    {% for city, country in popular_cities %}
                    <button class="city-btn" onclick="searchDemo('{{ city }}', '{{ country }}')">
                        {{ city }}, {{ country }}
                    </button>
                    {% endfor %}
                </div>
            </div>
        </div>
        
        <div class="weather-container" id="weatherContainer">
            <div class="loading" id="loading">
                <div>🌍</div>
                <div>Enter a city to see weather data</div>
            </div>
            
            <div class="weather-info" id="weatherInfo">
                <div class="location">
                    <h2 id="cityName"></h2>
                    <p id="countryName"></p>
                </div>
                
                <div class="current-weather">
                    <div class="weather-icon" id="weatherIcon"></div>
                    <div class="temperature" id="temperature"></div>
                    <div class="description" id="description"></div>
                    <div class="feels-like" id="feelsLike"></div>
                </div>
                
                <div class="weather-stats">
                    <div class="stat">
                        <div class="stat-icon">💧</div>
                        <div class="stat-label">Humidity</div>
                        <div class="stat-value" id="humidity"></div>
                    </div>
                    <div class="stat">
                        <div class="stat-icon">🌪️</div>
                        <div class="stat-label">Wind</div>
                        <div class="stat-value" id="windSpeed"></div>
                    </div>
                    <div class="stat">
                        <div class="stat-icon">🔽</div>
                        <div class="stat-label">Pressure</div>
                        <div class="stat-value" id="pressure"></div>
                    </div>
                    <div class="stat">
                        <div class="stat-icon">👁️</div>
                        <div class="stat-label">Visibility</div>
                        <div class="stat-value" id="visibility"></div>
                    </div>
                </div>
                
                <div class="timestamp" id="timestamp"></div>
            </div>
            
            <div class="error-message" id="errorMessage">
                <div>❌</div>
                <div>City not found. Try one of the popular cities above.</div>
            </div>
        </div>
    </div>

    <script>
        // DOM elements
        const form = document.getElementById('weatherForm');
        const cityInput = document.getElementById('city');
        const countryInput = document.getElementById('country');
        const loading = document.getElementById('loading');
        const weatherInfo = document.getElementById('weatherInfo');
        const errorMessage = document.getElementById('errorMessage');

        // Form handler
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const city = cityInput.value.trim();
            const country = countryInput.value.trim();
            
            if (!city) {
                alert('Please enter a city name');
                return;
            }
            
            await searchWeather(city, country);
        });

        // Search weather function
        async function searchWeather(city, country = '') {
            showLoading();
            
            try {
                const params = new URLSearchParams({ city, country });
                const response = await fetch(`/api/weather?${params}`);
                const data = await response.json();
                
                if (response.ok) {
                    displayWeather(data);
                } else {
                    showError(data.error);
                }
            } catch (error) {
                showError('Connection error');
            }
        }

        // Demo city search
        function searchDemo(city, country) {
            cityInput.value = city;
            countryInput.value = country;
            searchWeather(city, country);
        }

        // Display weather data
        function displayWeather(data) {
            document.getElementById('cityName').textContent = data.city;
            document.getElementById('countryName').textContent = data.country;
            document.getElementById('weatherIcon').textContent = data.icon;
            document.getElementById('temperature').textContent = `${data.temperature}°C`;
            document.getElementById('description').textContent = data.description;
            document.getElementById('feelsLike').textContent = `Feels like: ${data.feels_like}°C`;
            document.getElementById('humidity').textContent = `${data.humidity}%`;
            document.getElementById('windSpeed').textContent = `${data.wind_speed} m/s`;
            document.getElementById('pressure').textContent = `${data.pressure} hPa`;
            document.getElementById('visibility').textContent = `${data.visibility} km`;
            document.getElementById('timestamp').textContent = `Updated: ${data.timestamp}`;
            
            showWeatherInfo();
        }

        // Show loading
        function showLoading() {
            loading.style.display = 'block';
            weatherInfo.classList.remove('active');
            errorMessage.classList.remove('active');
        }

        // Show weather info
        function showWeatherInfo() {
            loading.style.display = 'none';
            weatherInfo.classList.add('active');
            errorMessage.classList.remove('active');
        }

        // Show error
        function showError(message) {
            loading.style.display = 'none';
            weatherInfo.classList.remove('active');
            errorMessage.classList.add('active');
            errorMessage.querySelector('div:last-child').textContent = message;
        }

        // Load default city
        window.addEventListener('load', () => {
            searchDemo('London', 'GB');
        });
    </script>
</body>
</html>
    ''', popular_cities=popular_cities, api_status=api_status, demo_cities_count=len(DEMO_DATA))

@app.route('/api/weather')
def get_weather():
    """API endpoint for weather data"""
    city = request.args.get('city', '').strip()
    country = request.args.get('country', '').strip()
    
    if not city:
        return jsonify({'error': 'City required'}), 400
    
    # Try real API first if available
    if API_KEY != 'demo_key':
        real_data = fetch_real_weather(city, country)
        if real_data:
            weather_data = {
                'city': real_data['name'],
                'country': real_data['sys']['country'],
                'temperature': round(real_data['main']['temp']),
                'feels_like': round(real_data['main']['feels_like']),
                'description': real_data['weather'][0]['description'],
                'icon': get_weather_icon(real_data['weather'][0]['icon']),
                'humidity': real_data['main']['humidity'],
                'wind_speed': real_data['wind']['speed'],
                'pressure': real_data['main']['pressure'],
                'visibility': round(real_data['visibility'] / 1000, 1),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return jsonify(weather_data)
    
    # Fall back to demo data
    search_key = f"{city.lower()},{country.lower()}" if country else city.lower()
    
    data = None
    for key, value in DEMO_DATA.items():
        if search_key in key or city.lower() in key:
            data = value
            break
    
    if not data:
        return jsonify({'error': f'City "{city}" not found in demo data'}), 404
    
    weather_data = {
        'city': data['name'],
        'country': data['country'],
        'temperature': round(data['main']['temp']),
        'feels_like': round(data['main']['feels_like']),
        'description': data['weather'][0]['description'],
        'icon': get_weather_icon(data['weather'][0]['icon']),
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'pressure': data['main']['pressure'],
        'visibility': round(data['visibility'] / 1000, 1),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return jsonify(weather_data)

if __name__ == '__main__':
    print("🌤️ Starting Enhanced Weather App...")
    print(f"📱 Open your browser at: http://localhost:5000")
    print(f"🗄️ Demo cities available: {len(DEMO_DATA)}")
    if API_KEY != 'demo_key':
        print("🌍 Real API enabled - unlimited cities!")
    else:
        print("🎭 Demo mode - to enable real API:")
        print("   1. Get free API key from https://openweathermap.org/api")
        print("   2. Set environment variable: OPENWEATHER_API_KEY=your_key")
        print("   3. Or edit API_KEY in the code")
    print("⏹️ Press Ctrl+C to stop")
    app.run(debug=True, host='0.0.0.0', port=5000) 