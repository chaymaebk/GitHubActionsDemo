# 🌤️ Weather App - Docker Image

A modern, responsive weather application with unlimited cities support and real-time weather data.

## 🚀 Quick Start

Pull and run the latest image:

```bash
docker pull chaymae01/weather-app:latest
docker run -p 5000:5000 -e OPENWEATHER_API_KEY=your_api_key chaymae01/weather-app:latest
```

## 🌍 Features

- ✅ **Real-time Weather Data** - Live data from OpenWeatherMap API
- ✅ **Unlimited Cities** - Search weather for any city worldwide  
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile
- ✅ **Modern UI** - Clean interface with smooth animations
- ✅ **Health Monitoring** - Built-in health checks
- ✅ **Security** - Runs as non-root user

## 🔧 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENWEATHER_API_KEY` | Your OpenWeatherMap API key | Yes |
| `FLASK_ENV` | Environment (development/production) | No |

## 📖 Usage Examples

### Basic Usage
```bash
docker run -p 5000:5000 \
  -e OPENWEATHER_API_KEY=your_api_key \
  chaymae01/weather-app:latest
```

### With Docker Compose
```yaml
version: '3.8'
services:
  weather-app:
    image: chaymae01/weather-app:latest
    ports:
      - "5000:5000"
    environment:
      - OPENWEATHER_API_KEY=your_api_key
```

### Production Deployment
```bash
docker run -d \
  --name weather-app \
  -p 80:5000 \
  -e OPENWEATHER_API_KEY=your_api_key \
  --restart unless-stopped \
  chaymae01/weather-app:latest
```

## 🏥 Health Check

The container includes health monitoring:
```bash
curl http://localhost:5000/health
```

## 🔗 Links

- **Source Code**: [GitHub Repository](https://github.com/yourusername/weather-app)
- **Demo**: Access at `http://localhost:5000` after running
- **API**: Get free API key at [OpenWeatherMap](https://openweathermap.org/api)

## 📊 Image Info

- **Base Image**: Python 3.11 Slim
- **Size**: Optimized for production
- **Security**: Non-root user, minimal dependencies
- **Platforms**: linux/amd64, linux/arm64

## 🤝 Support

For issues and questions:
- GitHub Issues: [Report here](https://github.com/yourusername/weather-app/issues)
- Docker Hub: [chaymae01/weather-app](https://hub.docker.com/r/chaymae01/weather-app)

---
⭐ **Star this repository if you find it useful!** 