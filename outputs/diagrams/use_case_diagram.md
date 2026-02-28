# Use Case Diagram

```mermaid
graph TB
    subgraph "Wind Turbine Energy Prediction System"
        UC1["⚡ Predict Energy Output"]
        UC2["🌍 Fetch Weather Data"]
        UC3["📊 Manual Input"]
        UC4["🎯 View Prediction Result"]
        UC5["📈 View Historical Data"]
        UC6["🔄 Train Model"]
    end
    
    subgraph "Actors"
        OPERATOR["👷 Wind Farm Operator"]
        GRID["🏢 Grid Operator"]
        ENERGY["⚡ Energy Manager"]
        SYSTEM["💻 System Admin"]
    end
    
    OPERATOR -->|Uses| UC1
    OPERATOR -->|Uses| UC2
    OPERATOR -->|Uses| UC3
    OPERATOR -->|Views| UC4
    
    GRID -->|Uses| UC1
    GRID -->|Uses| UC4
    GRID -->|Uses| UC5
    
    ENERGY -->|Uses| UC1
    ENERGY -->|Uses| UC3
    ENERGY -->|Views| UC4
    
    SYSTEM -->|Performs| UC6
    SYSTEM -->|Maintains| UC1
    
    UC2 -->|Fetches from| API["🌐 Weather API"]
    UC3 -->|Input from| User["👤 Manual Input"]
    UC1 -->|Uses| ML["🤖 ML Model"]
    UC5 -->|Accesses| DB["💾 Historical Data"]
    
    style UC1 fill:#E3F2FD
    style UC2 fill:#E3F2FD
    style UC3 fill:#E3F2FD
    style UC4 fill:#E3F2FD
    style UC5 fill:#E3F2FD
    style UC6 fill:#FCE4EC
    style OPERATOR fill:#FFF9C4
    style GRID fill:#FFF9C4
    style ENERGY fill:#FFF9C4
    style SYSTEM fill:#FFF9C4
```

## Use Case Scenarios

### 1. **Wind Farm Operator**
- Predict daily energy output for turbine maintenance planning
- Fetch real-time weather data automatically
- Manually input weather parameters for offline predictions
- View prediction results for scheduling purposes

### 2. **Grid Operator**
- Predict aggregate wind energy production
- Balance renewable and conventional energy sources
- Monitor historical production patterns
- Plan grid load distribution

### 3. **Energy Manager**
- Forecast energy availability for pricing decisions
- Input specific weather scenarios
- Compare predictions with actual output
- Optimize energy distribution strategy

### 4. **System Administrator**
- Train and retrain ML models with new data
- Maintain API integration
- Monitor system performance
- Manage database and backups
