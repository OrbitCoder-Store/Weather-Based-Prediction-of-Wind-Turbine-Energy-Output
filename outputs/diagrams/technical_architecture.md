# Technical Architecture Diagram

```mermaid
graph TB
    subgraph "User Interface Layer"
        UI["🌐 Web UI<br/>HTML5 + CSS3"]
    end
    
    subgraph "Flask Backend"
        ROUTE["📍 Route Handler<br/>app.py"]
        API["🔌 API Integration<br/>OpenWeatherMap"]
        PROCESSING["⚙️ Data Processing<br/>NumPy + Pandas"]
    end
    
    subgraph "Machine Learning"
        MODEL["🤖 ML Model<br/>Random Forest Regression<br/>power_prediction.sav"]
        FEATURES["📊 Feature Engineering<br/>Wind Speed, Temperature<br/>Humidity, Pressure"]
    end
    
    subgraph "Data Layer"
        CSV["💾 Historical Data<br/>T1.csv"]
        JOBLIB["📦 Model Storage<br/>Joblib Format"]
    end
    
    subgraph "External Services"
        WEATHER["🌤️ Weather API<br/>Real-time Data"]
    end
    
    UI -->|User Input| ROUTE
    ROUTE -->|Fetch Weather| API
    API -->|Weather Data| WEATHER
    WEATHER -->|Returns Data| PROCESSING
    PROCESSING -->|Feature Vector| MODEL
    FEATURES -->|Training Data| MODEL
    CSV -->|Historical Data| FEATURES
    MODEL -->|Predictions| ROUTE
    ROUTE -->|Result| UI
    ROUTE -->|Load Model| JOBLIB
    
    style UI fill:#E1F5FF
    style ROUTE fill:#FFF9C4
    style API fill:#FFF9C4
    style PROCESSING fill:#FFF9C4
    style MODEL fill:#F3E5F5
    style FEATURES fill:#F3E5F5
    style CSV fill:#E8F5E9
    style JOBLIB fill:#E8F5E9
    style WEATHER fill:#FCE4EC
```

## Architecture Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | HTML5, CSS3, JavaScript | User interface for data input & result display |
| **Backend** | Flask, Python | Route handling, API integration, data processing |
| **ML Engine** | Scikit-learn, Joblib | Model training, prediction, serialization |
| **Data Processing** | NumPy, Pandas, SciPy | Feature engineering, normalization |
| **External APIs** | OpenWeatherMap | Real-time weather data retrieval |
| **Data Storage** | CSV, Joblib | Historical data & trained model persistence |
