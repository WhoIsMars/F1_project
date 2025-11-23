# 🏎️ F1 Live Stats

A modern, real-time Formula 1 statistics visualization web application built with Vue.js 3 and FastAPI.

![F1 Live Stats](https://img.shields.io/badge/F1-Live%20Stats-E10600?style=for-the-badge&logo=formula1&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-3-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)

## ✨ Features

- **Real-time Race Data**: Live position tracking, lap times, and gaps between drivers
- **Interactive UI**: Responsive design with elegant glassmorphism effects
- **Race Visualization**: Animated track map showing driver positions in real-time
- **Comprehensive Stats**: Weather conditions, track temperature, race status
- **Driver Information**: Team colors, tyre compounds, pit stop data
- **Sector Times**: Detailed sector-by-sector performance analysis
- **Dual View**: Separate interfaces for Qualifying and Race sessions
- **WebSocket Streaming**: Real-time data updates without page refresh

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+**
- **Node.js 18+**
- **npm** or **yarn**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/WhoIsMars/F1_project.git
   cd F1_project
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

1. **Start Backend** (Terminal 1)
   ```bash
   cd backend
   source venv/bin/activate
   uvicorn main:app --reload
   ```
   Backend will run on `http://127.0.0.1:8000`

2. **Start Frontend** (Terminal 2)
   ```bash
   cd frontend
   npm run dev
   ```
   Frontend will run on `http://localhost:5173`

3. **Open in Browser**
   Navigate to `http://localhost:5173`

## 📁 Project Structure

```
F1_project/
├── backend/
│   ├── main.py              # FastAPI application & WebSocket server
│   ├── collector.py         # Data collection from OpenF1 API
│   ├── processor.py         # Data processing & simulation
│   ├── requirements.txt     # Python dependencies
│   └── tests/              # Backend unit tests
│       ├── test_collector.py
│       └── test_processor.py
│
├── frontend/
│   ├── src/
│   │   ├── components/     # Vue components
│   │   │   ├── DriverList.vue
│   │   │   ├── RaceMap.vue
│   │   │   └── SectorGrid.vue
│   │   ├── views/          # Page views
│   │   │   ├── Race.vue
│   │   │   └── Qualifying.vue
│   │   ├── stores/         # Pinia state management
│   │   │   └── race.ts
│   │   ├── router/         # Vue Router
│   │   └── style.css       # Tailwind CSS config
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```

## 🔌 Data Sources

The application uses a **cascade fallback system** for data reliability:

1. **OpenF1 API** (Primary)
   - Real historical race data
   - Driver positions, lap times, intervals
   - Session information
   - [OpenF1 Documentation](https://openf1.org)

2. **Simulation Fallback** (Secondary)
   - Realistic standings based on recent races
   - Simulated telemetry and race progression
   - Ensures app functionality when live data unavailable

## 🎨 Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **TypeScript** - Type safety
- **Tailwind CSS v4** - Utility-first CSS framework
- **Pinia** - State management
- **Vue Router** - Client-side routing
- **Vite** - Build tool and dev server
- **Vitest** - Unit testing

### Backend
- **FastAPI** - Modern Python web framework
- **WebSockets** - Real-time bidirectional communication
- **httpx** - Async HTTP client
- **pytest** - Testing framework

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🎯 Key Features Explained

### Real-time Updates
Data is streamed via WebSockets and updates every 5 seconds, providing near-real-time race information.

### Viewport-Optimized Layout
The UI is designed to fit perfectly within the viewport (no page scrolling), with internal scrolling for the driver list to accommodate all 20 drivers.

### Team-Based Styling
Driver entries are color-coded based on their team, making it easy to track team performance at a glance.

### Responsive Design
Fully responsive layout that adapts to different screen sizes while maintaining functionality.

## 🔧 Configuration

Create `backend/config.py` to customize data sources (optional):
```python
# OpenF1 - Free for historical data
OPENF1_ENABLED = True

# Fallback simulation
SIMULATION_ENABLED = True
```

## 📊 API Endpoints

### WebSocket
- `ws://127.0.0.1:8000/ws` - Real-time race data stream

### HTTP
- `GET /` - Health check
- Returns: `{"status": "ok"}`

## 🎨 UI Screenshots

The application features:
- **Dark theme** with F1 red accents
- **Glassmorphism** effects for modern aesthetics
- **Compact driver list** with internal scrolling
- **Interactive race map** with live driver positions
- **Real-time stats** (Weather, Track Temp, Status)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **OpenF1** for providing free F1 data API
- **Formula 1** for the amazing sport
- **Vue.js** and **FastAPI** communities for excellent documentation

## 📧 Contact

Project Link: [https://github.com/WhoIsMars/F1_project](https://github.com/WhoIsMars/F1_project)

---

**Built with ❤️ for F1 fans by F1 fans** 🏁
