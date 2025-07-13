# 🌤️ Weather App

[![CI/CD](https://github.com/yourusername/weather-app/actions/workflows/weather-app.yml/badge.svg)](https://github.com/yourusername/weather-app/actions/workflows/weather-app.yml)
[![Code Quality](https://github.com/yourusername/weather-app/actions/workflows/code-quality.yml/badge.svg)](https://github.com/yourusername/weather-app/actions/workflows/code-quality.yml)
[![Docker](https://github.com/yourusername/weather-app/actions/workflows/docker.yml/badge.svg)](https://github.com/yourusername/weather-app/actions/workflows/docker.yml)

A modern, responsive weather application with unlimited cities support and real-time weather data.

## 🚀 Features

- 🌍 **Unlimited Cities** - Search weather for any city worldwide
- 🔄 **Real-time Data** - Live weather information from OpenWeatherMap
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 🎨 **Modern UI** - Clean, intuitive interface with smooth animations
- ⚡ **Fast Loading** - Optimized for quick weather data retrieval
- 🛡️ **Secure** - Environment-based API key management

## 🎯 Live Demo

- **Live App**: [https://your-app.onrender.com](https://your-app.onrender.com)
- **Documentation**: [https://yourusername.github.io/weather-app](https://yourusername.github.io/weather-app)

## 🏃‍♂️ Quick Start

### Prerequisites

- Python 3.8+
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   ```bash
   # Create config.py
   echo "OPENWEATHER_API_KEY = 'your_api_key_here'" > config.py
   ```

4. **Run the application**
   ```bash
   python weather_web_app_enhanced.py
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENWEATHER_API_KEY` | Your OpenWeatherMap API key | Yes |
| `PORT` | Port to run the application (default: 5000) | No |

### API Key Setup

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Set it in one of these ways:

   **Option 1: config.py file**
   ```python
   OPENWEATHER_API_KEY = 'your_api_key_here'
   ```

   **Option 2: Environment variable**
   ```bash
   export OPENWEATHER_API_KEY=your_api_key_here
   ```

## 🐳 Docker

### Run with Docker

```bash
# Build the image
docker build -t weather-app .

# Run the container
docker run -p 5000:5000 -e OPENWEATHER_API_KEY=your_api_key weather-app
```

### Docker Compose

```yaml
version: '3.8'
services:
  weather-app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - OPENWEATHER_API_KEY=your_api_key_here
```

## 📁 Project Structure

```
weather-app/
├── .github/workflows/          # GitHub Actions workflows
│   ├── weather-app.yml         # Main CI/CD pipeline
│   ├── code-quality.yml        # Code quality checks
│   ├── performance-test.yml    # Performance testing
│   └── docker.yml              # Docker build & push
├── weather_web_app_enhanced.py # Main Flask application
├── config.py                   # Configuration file
├── requirements.txt            # Python dependencies
├── test_api.py                 # API testing script
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## 🧪 Testing

### Run Tests Locally

```bash
# Install test dependencies
pip install pytest pytest-flask

# Run API test
python test_api.py

# Run Flask tests
python -m pytest
```

### Performance Testing

```bash
# Install Locust
pip install locust

# Run load test
locust -f .github/workflows/locustfile.py --host http://localhost:5000
```

## 🚀 Deployment

### Deploy to Render

1. Fork this repository
2. Connect your GitHub account to [Render](https://render.com)
3. Create a new Web Service
4. Set environment variable: `OPENWEATHER_API_KEY`
5. Deploy!

### Deploy to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create your-weather-app

# Set environment variable
heroku config:set OPENWEATHER_API_KEY=your_api_key

# Deploy
git push heroku main
```

### Deploy with GitHub Actions

The repository includes automated deployment workflows:

- **Render**: Set `RENDER_DEPLOY_HOOK_URL` secret
- **Heroku**: Set `HEROKU_API_KEY`, `HEROKU_APP_NAME`, and `HEROKU_EMAIL` secrets
- **Docker**: Automatically builds and pushes to GitHub Container Registry

## 🔒 Security

- API keys are never committed to the repository
- All secrets are managed through environment variables
- Regular security scans with Bandit and Snyk
- Docker images scanned with Trivy
- Dependency vulnerability checks

## 🛠️ Development

### Code Quality

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **Bandit**: Security scanning

Run all quality checks:
```bash
black --check .
isort --check-only .
flake8 .
bandit -r .
```

### GitHub Actions Workflows

- **CI/CD**: Testing, building, and deployment
- **Code Quality**: Linting, formatting, security checks
- **Performance**: Load testing and response time monitoring
- **Docker**: Multi-platform image building and security scanning

## 📊 Performance

- Homepage response time: < 2 seconds
- API response time: < 5 seconds
- Load tested with 10 concurrent users
- 99.9% uptime SLA

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/weather-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/weather-app/discussions)
- **Email**: your.email@example.com

## 🌟 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org)
- Icons from [Font Awesome](https://fontawesome.com)
- Deployed on [Render](https://render.com) and [Heroku](https://heroku.com)
