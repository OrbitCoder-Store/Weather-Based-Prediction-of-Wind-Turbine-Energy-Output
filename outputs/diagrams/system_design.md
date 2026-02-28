# System Design Diagram

```mermaid
graph TB
    subgraph "Client Layer"
        BROWSER["🌐 Web Browser"]
        HTML["📄 HTML Pages<br/>intro.html<br/>predict.html"]
        CSS["🎨 Stylesheets<br/>style.css"]
        JS["⚙️ JavaScript<br/>Event Handling"]
    end
    
    subgraph "Application Layer"
        APP["🚀 Flask Application<br/>app.py / windApp.py"]
        ROUTES["🛣️ Route Handlers<br/>@ / (intro)<br/>@/predict (predict)"]
        TEMPLATE["📝 Template Engine<br/>Jinja2"]
    end
    
    subgraph "Business Logic Layer"
        VALIDATE["✅ Input Validation<br/>Type Check<br/>Range Check"]
        PREPROCESS["🔄 Data Preprocessing<br/>Normalization<br/>Feature Engineering"]
        PREDICT["🎯 Prediction Engine<br/>Load Model<br/>Generate Output"]
    end
    
    subgraph "Integration Layer"
        APIHANDLER["🔌 API Handler<br/>OpenWeatherMap"]
        DATABUFFER["💾 Cache Layer<br/>Request Buffering"]
    end
    
    subgraph "Data & Model Layer"
        MODEL["🤖 ML Model<br/>Random Forest Regressor<br/>power_prediction.sav"]
        SCALER["📊 Feature Scaler<br/>StandardScaler"]
        JOBLIB["📦 Joblib Serialization"]
    end
    
    subgraph "Storage Layer"
        DATABASE["💾 Data Storage<br/>T1.csv<br/>Historical Data"]
        MODELSTORE["🗂️ Model Storage<br/>Serialized Models<br/>power_prediction.sav"]
    end
    
    subgraph "External Services"
        WEATHER["🌤️ OpenWeatherMap API<br/>Real-time Weather Data"]
    end
    
    BROWSER -->|HTTP Request| APP
    HTML -->|Rendered by| BROWSER
    CSS -->|Styled with| HTML
    JS -->|Interacts with| APP
    
    APP -->|Renders| TEMPLATE
    TEMPLATE -->|Uses| HTML
    APP -->|Routes to| ROUTES
    ROUTES -->|Calls| VALIDATE
    VALIDATE -->|Passes to| PREPROCESS
    PREPROCESS -->|Feeds to| PREDICT
    
    VALIDATE -->|Fetches Weather| APIHANDLER
    APIHANDLER -->|Caches| DATABUFFER
    DATABUFFER -->|Sends Result| VALIDATE
    
    PREDICT -->|Uses| MODEL
    MODEL -->|Scales Features| SCALER
    SCALER -->|Returns Output| PREDICT
    PREDICT -->|Sends Result| APP
    APP -->|Renders| BROWSER
    
    MODEL -->|Loaded from| JOBLIB
    JOBLIB -->|Reads| MODELSTORE
    DATABASE -->|Trains| MODEL
    
    APIHANDLER -->|Calls| WEATHER
    
    style BROWSER fill:#E1F5FF
    style HTML fill:#E1F5FF
    style CSS fill:#E1F5FF
    style JS fill:#E1F5FF
    style APP fill:#FFF9C4
    style ROUTES fill:#FFF9C4
    style TEMPLATE fill:#FFF9C4
    style VALIDATE fill:#F3E5F5
    style PREPROCESS fill:#F3E5F5
    style PREDICT fill:#F3E5F5
    style APIHANDLER fill:#FCE4EC
    style DATABUFFER fill:#FCE4EC
    style MODEL fill:#E8F5E9
    style SCALER fill:#E8F5E9
    style JOBLIB fill:#E8F5E9
    style DATABASE fill:#BBDEFB
    style MODELSTORE fill:#BBDEFB
    style WEATHER fill:#FFE0B2
```

## System Components Architecture

### Client Layer
| Component | Role |
|-----------|------|
| **Web Browser** | User interface rendering |
| **HTML Templates** | UI structure and forms |
| **CSS Stylesheets** | Visual styling and responsiveness |
| **JavaScript** | Dynamic interactions and validations |

### Application Layer
| Component | Role |
|-----------|------|
| **Flask App** | Request handling and routing |
| **Route Handlers** | URL routing logic |
| **Jinja2 Engine** | Dynamic template rendering |

### Business Logic Layer
| Component | Role |
|-----------|------|
| **Validation** | Input verification and sanitization |
| **Preprocessing** | Feature normalization and scaling |
| **Prediction Engine** | ML model inference |

### Data & Model Layer
| Component | Role |
|-----------|------|
| **ML Model** | Random Forest Regression engine |
| **Feature Scaler** | StandardScaler for normalization |
| **Joblib** | Model serialization/deserialization |

### Storage Layer
| Component | Role |
|-----------|------|
| **CSV Database** | Historical training data |
| **Model Store** | Serialized model files |
