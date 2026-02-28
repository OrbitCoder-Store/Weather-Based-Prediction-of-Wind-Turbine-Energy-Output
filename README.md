# 🌬️ Weather-Based Prediction of Wind Turbine Energy Output

<div align="center">

### ⚡ A Next-Generation Approach to Renewable Energy Management

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Harness the Power of Machine Learning to Predict Wind Turbine Energy Output**

*Using weather conditions to forecast renewable energy generation with high accuracy*

</div>

---

## 📌 Project Overview

This project focuses on **predicting the energy output of wind turbines based on weather conditions** using **Machine Learning and Flask**. Accurate energy prediction is crucial for renewable energy management, helping energy companies, wind farm operators, and grid operators make informed decisions.

By analyzing **historical wind and weather data**, a regression-based machine learning model is trained to predict turbine energy output under given weather conditions.

---

## 🎯 Problem Type

✔ **Regression Problem**
Because the output (energy in kWh) is a **continuous numerical value**, regression algorithms are used.

---

## ⚠️ Problem Statement

### The Challenge

Wind farms face significant operational challenges in predicting energy output and optimizing turbine performance. Traditional forecasting methods rely on historical averages and manual analysis, which lack precision and adaptability to dynamic weather conditions.

### 🔑 Key Highlights

#### 1. 🌍 **Importance of Renewable Energy**
- Renewable energy accounts for **25-30%** of global electricity generation
- Wind energy is the fastest-growing renewable source
- Accurate prediction reduces grid instability by **15-20%**
- Critical for achieving carbon neutrality goals (UN SDG 13)

#### 2. 🌪️ **Wind Energy's Dependency on Weather**
- Wind power output is **directly proportional** to wind speed (cubic relationship)
- Atmospheric pressure and temperature affect air density
- Humidity influences turbine efficiency by **5-8%**
- Weather-driven variability requires real-time prediction models

#### 3. 📊 **Need for Intelligent Prediction**
- Energy companies need **24-48 hour forecasts** for grid planning
- Maintenance scheduling requires **production predictions**
- Reduces energy wastage by **10-15%** through accurate planning
- Enables dynamic pricing based on predicted supply

### 📈 Problem Statement Diagram

```mermaid
graph TB
    A["❌ Current Problem"] -->|Traditional Methods| B["Manual Analysis<br/>Inaccurate<br/>Delayed Decisions"]
    A -->|Limitations| C["✕ No Real-time Adaptation<br/>✕ High Prediction Error<br/>✕ Inefficient Planning<br/>✕ Grid Imbalance Risk"]
    
    D["✅ Proposed Solution<br/>ML-Based Prediction"] -->|Modern Technology| E["Intelligent Algorithms<br/>Real-time Processing<br/>High Accuracy"]
    D -->|Benefits| F["✓ 90%+ Prediction Accuracy<br/>✓ Real-time Adaptation<br/>✓ Optimal Planning<br/>✓ Grid Stability"]
    
    C -->|Gap| F
    
    style A fill:#FFCDD2
    style B fill:#FFCDD2
    style C fill:#FFCDD2
    style D fill:#C8E6C9
    style E fill:#C8E6C9
    style F fill:#C8E6C9
```

---

## 🌍 Real-World Scenarios

### 🔹 Scenario 1: Energy Production Forecasting

Energy companies can forecast wind turbine energy production using weather forecasts, enabling:

* Efficient energy distribution
* Dynamic pricing decisions
* Reduced energy wastage

### 🔹 Scenario 2: Maintenance Planning

Wind farm operators can:

* Predict low-wind periods
* Schedule maintenance to minimize downtime
* Maximize turbine availability during high-wind periods

### 🔹 Scenario 3: Grid Integration

Grid operators can:

* Balance renewable and conventional energy sources
* Adjust grid load dynamically
* Ensure stable and efficient energy supply

---

## 🏗️ Technical Architecture

### System Architecture Overview

The system is designed with a multi-layered architecture for scalability and maintainability:

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

📄 **[Detailed Technical Architecture Diagram](outputs/diagrams/technical_architecture.md)**

### Use Case Diagram

```mermaid
graph TB
    subgraph "Wind Turbine Energy Prediction System"
        UC1["⚡ Predict Energy Output"]
        UC2["🌍 Fetch Weather Data"]
        UC3["📊 Manual Input"]
        UC4["🎯 View Prediction Result"]
        UC5["📈 View Historical Data"]
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
    
    SYSTEM -->|Performs| UC6["🔄 Train Model"]
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
    style OPERATOR fill:#FFF9C4
    style GRID fill:#FFF9C4
    style ENERGY fill:#FFF9C4
    style SYSTEM fill:#FFF9C4
```

📄 **[Complete Use Case Diagram](outputs/diagrams/use_case_diagram.md)**

### Activity Flow Diagram

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

📄 **[Complete Activity Diagram](outputs/diagrams/activity_diagram.md)**

### System Design Diagram

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

📄 **[Complete System Design Diagram](outputs/diagrams/system_design.md)**

---

## 🎯 Project Objectives

By completing this project, you will be able to:

* Identify whether a problem is **regression or classification**
* Perform **data preprocessing and cleaning**
* Visualize and analyze datasets for insights
* Apply suitable **machine learning algorithms**
* Train, test, and evaluate ML models
* Build a **Flask-based web application**
* Integrate ML models with a real-time UI

---

## 🔄 Project Flow

1. User interacts with the Web UI
2. Weather data is fetched (API integration)
3. Input is passed to the ML model
4. Model predicts wind turbine energy output
5. Prediction is displayed to the user

---

## 🧪 Project Phases

### 1️⃣ Data Collection

* Dataset collected from wind turbine historical records
* Stored in CSV format

### 2️⃣ Data Preprocessing

* Importing libraries
* Handling missing values
* Data cleaning and normalization
* Feature selection
* Train-test split

### 3️⃣ Data Visualization

* Wind speed vs power analysis
* Accuracy and performance graphs

### 4️⃣ Model Building

Regression algorithms used:

* **Random Forest Regression** (final model)

### 5️⃣ Model Evaluation

* Accuracy comparison
* Performance analysis on test data

### 6️⃣ Application Building

* HTML + CSS frontend
* Flask backend
* Model integration using `joblib`

---

## 🛠️ Technologies Used

### 🧠 Machine Learning

* Python
* Scikit-learn
* NumPy
* Pandas
* Matplotlib

### 🌐 Web Development

* Flask
* HTML
* CSS
* JavaScript

---

## 📦 Prerequisites

### Software Requirements

* Anaconda Navigator
* Python 3.x
* Jupyter Notebook / Spyder
* Web Browser

### Required Python Packages

Install from requirements.txt:

```bash
pip install -r requirements.txt
```

**Package List:**

* numpy==1.24.4
* pandas==2.0.3
* scipy==1.10.1
* scikit-learn==1.2.2
* joblib==1.3.2
* flask
* requests

---

## 📂 Project Structure

```text
Weather-Based-Prediction-of-Wind-Turbine-Energy-Output/
│
├── README.md
├── Procfile
├── runtime.txt
│
├── Document/
│   └── README.md
│
├── Project-Files/
│   ├── data/
│   │   └── T1.csv
│   │
│   ├── Flask-Wind-Mill-Power-Prediction/
│   │   ├── static/
│   │   │   ├── style.css
│   │   │   └── images/
│   │   │
│   │   ├── templates/
│   │   │   ├── intro.html
│   │   │   └── predict.html
│   │   │
│   │   ├── app.py
│   │   ├── windApp.py
│   │   └── power_prediction.sav
│   │
│   ├── power_prediction.sav
│   ├── Wind_mill_model.ipynb
│   ├── wind_turbine_energy_prediction.py
│   ├── test_model.py
│   └── requirements.txt
│
├── outputs/
│   ├── images/
│   │   └── [Generated Output Images]
│   │
│   └── diagrams/
│       ├── technical_architecture.md
│       ├── use_case_diagram.md
│       ├── activity_diagram.md
│       └── system_design.md
│
└── Video-Demo/
    └── README.md
```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Weather-Based-Prediction-of-Wind-Turbine-Energy-Output/Project-Files/Flask-Wind-Mill-Power-Prediction
```

### Step 2: Install Dependencies

```bash
pip install -r ../requirements.txt
```

Or install individually:

```bash
pip install numpy==1.24.4
pip install pandas==2.0.3
pip install scipy==1.10.1
pip install scikit-learn==1.2.2
pip install joblib==1.3.2
pip install flask
pip install requests
```

### Step 3: Run the Flask Application

```bash
python app.py
```

### Step 4: Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 💡 How to Use the Application

### Method 1: Using Weather API

1. Navigate to the prediction page
2. Enter a city name (e.g., "London", "New York")
3. Click "Fetch Weather Data"
4. The system will automatically retrieve weather parameters
5. Click "Predict Energy Output"
6. View the predicted energy output in kW

### Method 2: Manual Input

1. Navigate to the prediction page
2. Manually enter the following parameters:
   * Temperature (°C)
   * Humidity (%)
   * Pressure (mmHG)
   * Wind Speed (m/s)
3. Click "Predict Energy Output"
4. View the predicted energy output in kW

---

## 🎨 Features

* 🌤 Weather-based energy prediction
* 🔌 Weather API integration (OpenWeatherMap)
* ⏳ Loading animation
* 📊 Real-time prediction visualization
* ⚡ Live energy output prediction
* 📱 Responsive UI design
* 🎯 Manual input or API-based weather data

---

## 📸 Application Screenshots

### Landing Page
![Landing Page](Project-Files/Flask-Wind-Mill-Power-Prediction/static/images/output1.jpeg)

### Prediction Interface
![Prediction Page](Project-Files/Flask-Wind-Mill-Power-Prediction/static/images/output2.jpeg)

### Prediction Results
![Results](Project-Files/Flask-Wind-Mill-Power-Prediction/static/images/output3.jpeg)

---

## 📋 File Descriptions

### Main Files

* **app.py** - Main Flask application with routes and API integration
* **windApp.py** - Alternative Flask application implementation
* **Wind_mill_model.ipynb** - Jupyter notebook for model training and analysis
* **wind_turbine_energy_prediction.py** - Python script for model development
* **test_model.py** - Model testing and evaluation script
* **power_prediction.sav** - Trained machine learning model (joblib format)

### Data Files

* **data/T1.csv** - Wind turbine historical data for training

### Templates

* **intro.html** - Landing page template
* **predict.html** - Prediction page with input forms and results display

### Static Files

* **style.css** - Styling for the web application
* **images/** - Contains UI images and application screenshots

---

## 🔧 Model Details

The project uses **Random Forest Regression** as the final model for predicting wind turbine energy output. The model is trained on historical weather data including:

* Wind Speed (m/s)
* Temperature (°C)
* Humidity (%)
* Atmospheric Pressure (mmHG)

The trained model is saved using **joblib** and integrated with the Flask application for real-time predictions.

---

## 🌐 API Integration

The application integrates with **OpenWeatherMap API** to fetch real-time weather data for any city. Users can either:

1. Enter weather parameters manually
2. Fetch weather data automatically by entering a city name

**API Key**: The application uses OpenWeatherMap API (included in app.py)

---

## ✅ Conclusion

This project demonstrates how **machine learning and web technologies** can be combined to solve real-world renewable energy challenges. Predicting wind turbine energy output improves efficiency, planning, and grid stability, contributing to a more sustainable energy future.

---

## 👨‍💻 Developed By

**APSCHE AIML Project – Renewable Energy & Machine Learning**

### 👑 Team Lead
- **Aditya Indana** - Project Lead & Technical Architect

### 🏆 Development Team

| Role | Member | GitHub |
|------|--------|--------|
| **Team Lead** | Aditya Indana | [22MH1A42G1](https://github.com/22MH1A42G1) |
| **Developer** | KAMPARAPU SRI RAM | [22MH1A42G5](https://github.com/22MH1A42G5) |
| **Developer** | Vinay Charu Kirthan Rohit Kotha | [RohitKotha](https://github.com/RohitKotha) |
| **Developer** | Likhitha Hasini Chebolu | [22mh1a42h0](https://github.com/22mh1a42h0) |
| **Developer** | Mary Shakeena Meka | [maryshakeena](https://github.com/maryshakeena) |

### 📈 Project Contributions
- **Project Vision & Architecture** — Team Lead
- **Machine Learning Model Development** — Development Team
- **Web Application Development** — Development Team
- **Documentation & Testing** — Full Team

---

## 📞 Contact & Support

For questions, suggestions, or contributions, feel free to reach out:
- Create an issue in the repository
- Submit a pull request with improvements
- Contact the team lead for collaboration opportunities

---

*This project represents the collaborative effort of the APSCHE AIML team, demonstrating excellence in renewable energy technology and machine learning applications.*
