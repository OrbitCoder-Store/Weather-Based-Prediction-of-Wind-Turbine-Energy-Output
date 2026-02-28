# Activity Diagram - Wind Energy Prediction Flow

```mermaid
graph TD
    START([🟢 Start]) --> A["User Navigates to<br/>Prediction Page"]
    
    A --> B{"Select Input<br/>Method"}
    
    B -->|API Method| C["User Enters City Name"]
    B -->|Manual Method| D["User Enters Parameters"]
    
    C --> E["Fetch Weather Data<br/>from OpenWeatherMap API"]
    E --> F{"API Request<br/>Successful?"}
    F -->|Yes| G["Extract Weather Parameters<br/>Temp, Humidity,<br/>Pressure, Wind Speed"]
    F -->|No| H["Display Error Message"]
    H --> A
    
    D --> G
    
    G --> I["Validate Input Data<br/>Check Range & Format"]
    I --> J{"Data Valid?"}
    J -->|No| K["Show Validation Error"]
    K --> A
    J -->|Yes| L["Normalize Features<br/>Scaling & Encoding"]
    
    L --> M["Load Trained Model<br/>power_prediction.sav"]
    M --> N["Generate Feature Vector<br/>from Input Parameters"]
    
    N --> O["Random Forest Model<br/>Prediction"]
    O --> P["Generate Energy Output<br/>in kWh"]
    
    P --> Q["Format Results<br/>Display Prediction"]
    Q --> R["Show Results on UI<br/>with Visualization"]
    
    R --> S{"User Wants<br/>Another<br/>Prediction?"}
    S -->|Yes| A
    S -->|No| END([🛑 End])
    
    style START fill:#4CAF50,color:#fff
    style END fill:#F44336,color:#fff
    style O fill:#2196F3,color:#fff
    style A fill:#FFF9C4
    style B fill:#FFE0B2
    style C fill:#E1BEE7
    style D fill:#E1BEE7
    style E fill:#BBDEFB
    style G fill:#C8E6C9
    style I fill:#C8E6C9
    style L fill:#B3E5FC
    style M fill:#F8BBD0
    style N fill:#F8BBD0
    style P fill:#D1C4E9
    style Q fill:#FFCCBC
    style R fill:#FFCCBC
```

## Prediction Flow Stages

| Stage | Activity | Status |
|-------|----------|--------|
| **Input** | User selects prediction method and provides data | 🔵 Initial |
| **Validation** | System validates input parameters and format | 🟡 Processing |
| **Preparation** | Features are normalized and scaled for ML model | 🟡 Processing |
| **Prediction** | Random Forest model generates energy output | 🔵 Critical |
| **Output** | Results formatted and displayed to user | 🟢 Final |
