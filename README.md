# 🧠 Personality Type Predictor

A machine learning-powered web application that predicts your personality type (Introvert, Extrovert, or Ambivert) based on your behavioral traits and characteristics. Built with Streamlit for an interactive user experience and scikit-learn for robust predictions.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Personality Type Predictor** uses advanced machine learning techniques to analyze 26 behavioral attributes and accurately classify individuals into one of three personality types:

- **🌟 Extrovert**: Social, energetic, and outgoing individuals
- **🎧 Introvert**: Reflective, independent, and thoughtful individuals  
- **⚖️ Ambivert**: Balanced individuals with both introverted and extroverted traits

With **99.75% model accuracy**, this application provides reliable and insightful personality assessments.

---

## ✨ Features

✅ **Interactive Web Interface** - Built with Streamlit for seamless user interaction  
✅ **Real-time Predictions** - Instant personality classification  
✅ **26 Behavioral Attributes** - Comprehensive personality assessment  
✅ **Confidence Scoring** - Model confidence percentage for each prediction  
✅ **Personalized Insights** - Detailed explanations for each personality type  
✅ **Responsive Design** - Modern UI with smooth animations  
✅ **Pre-trained Model** - Ready-to-use ML model with high accuracy  
✅ **Data Scaling** - Normalized inputs for consistent predictions  

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE (STREAMLIT)                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Interactive Sliders for 26 Behavioral Attributes          │ │
│  │  - Social Energy, Talkativeness, Empathy, Leadership, etc. │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  DATA PREPROCESSING LAYER                       │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Feature Collection: [26 Behavioral Attributes]           │ │
│  │  Data Scaling: StandardScaler (scaler.pkl)                │ │
│  │  Input Normalization: [0-10] → Standardized Scale        │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                 MACHINE LEARNING MODEL LAYER                    │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Algorithm: Logistic Regression                           │ │
│  │  Model File: personality_model.pkl                        │ │
│  │  Training Data: personality_synthetic_dataset.csv         │ │
│  │  Features: 26 behavioral traits                           │ │
│  │  Classes: [Introvert, Extrovert, Ambivert]              │ │
│  │  Accuracy: 99.75%                                        │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PREDICTION & OUTPUT LAYER                     │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Personality Classification                               │ │
│  │  Confidence Score (probability)                           │ │
│  │  Personalized Insights & Recommendations                 │ │
│  │  Visual Display with Emojis & Animations                │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Interactive web application framework |
| **Scikit-learn** | Machine learning and model training |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Pickle** | Model serialization |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/BaljeetkumarPatel/Personality-Predictor.git
cd Personality-Predictor
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
streamlit --version
```

---

## 🚀 Usage

### Run the Application
```bash
streamlit run app.py
```

The application will start at `http://localhost:8501` in your default browser.

### How to Use

1. **Rate Your Attributes**: Use the interactive sliders (0-10) to rate yourself on 26 behavioral traits
2. **Click Predict**: Press the "🔮 Predict My Personality Type" button
3. **View Results**: Get your personality type with confidence score and insights
4. **Repeat**: Adjust values and predict again to explore different scenarios

### Example Workflow
```
Opening the app
    ↓
Adjust 26 sliders based on your traits
    ↓
Click "Predict" button
    ↓
Receive personality classification
    ↓
Read personalized insights
```

---

## 📁 Project Structure

```
Personality-Predictor/
│
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Python dependencies
├── personality_model.pkl               # Trained ML model (binary)
├── scaler.pkl                          # Data scaler for normalization
├── personality_synthetic_dataset.csv   # Training dataset (~10MB)
│
├── logistic_solutions.ipynb            # Model training & evaluation notebook
├── logistic Que.ipynb                  # Exploratory data analysis notebook
│
├── screenshot/                         # Application screenshots
│   ├── Screenshot 2026-04-26 233637.png
│   └── Screenshot 2026-04-26 233729.png
│
└── README.md                           # Documentation (this file)
```

---

## 🧠 Model Details

### Algorithm
- **Classifier**: Logistic Regression
- **Framework**: Scikit-learn
- **Training Approach**: Supervised Learning

### Performance Metrics
- **Accuracy**: 99.75%
- **Precision**: High across all classes
- **Training Samples**: Large synthetic dataset
- **Features**: 26 behavioral attributes

### Input Features (26 Total)

| Behavioral Attribute | Scale |
|---------------------|-------|
| Social Energy | 0-10 |
| Alone Time Preference | 0-10 |
| Talkativeness | 0-10 |
| Deep Reflection | 0-10 |
| Group Comfort | 0-10 |
| Party Liking | 0-10 |
| Listening Skill | 0-10 |
| Empathy | 0-10 |
| Organization | 0-10 |
| Leadership | 0-10 |
| Risk Taking | 0-10 |
| Public Speaking Comfort | 0-10 |
| Curiosity | 0-10 |
| Routine Preference | 0-10 |
| Excitement Seeking | 0-10 |
| Friendliness | 0-10 |
| Planning | 0-10 |
| Spontaneity | 0-10 |
| Adventurousness | 0-10 |
| Reading Habit | 0-10 |
| Sports Interest | 0-10 |
| Online Social Usage | 0-10 |
| Travel Desire | 0-10 |
| Gadget Usage | 0-10 |
| Work Style (Collaborative) | 0-10 |
| Decision Speed | 0-10 |

### Output Classes
- **0**: Ambivert (⚖️)
- **1**: Extrovert (🌟)
- **2**: Introvert (🎧)

---

## 📸 Screenshots

### Application Interface - Input Section
![Personality Predictor UI - Input](screenshot/Screenshot%202026-04-26%20233637.png)

*The main interface showing interactive sliders for rating behavioral attributes*

### Application Interface - Results Section
![Personality Predictor UI - Results](screenshot/Screenshot%202026-04-26%20233729.png)

*The results display showing personality classification and confidence score*

---

## 💡 How It Works

### Step-by-Step Process

1. **User Input Collection**
   - User rates 26 behavioral attributes on a 0-10 scale
   - Values collected through interactive Streamlit sliders

2. **Data Preprocessing**
   - Input array created from collected values
   - StandardScaler normalizes the data
   - Ensures consistency with model training

3. **Model Inference**
   - Scaled input passed to trained Logistic Regression model
   - Model computes probability for each class

4. **Prediction Generation**
   - Highest probability class selected
   - Class mapping applied (0→Ambivert, 1→Extrovert, 2→Introvert)
   - Confidence score calculated

5. **Result Display**
   - Personality type shown with emoji
   - Confidence percentage displayed
   - Personalized insight text provided
   - Smooth animations enhance UX

### Personality Type Definitions

**🌟 Extrovert**
- Draws energy from social interactions
- Enjoys large group activities
- Comfortable with public speaking
- Highly sociable and outgoing
- Prefers collaborative work environments

**🎧 Introvert**
- Recharges through solitude
- Prefers one-on-one conversations
- Deep thinkers and listeners
- Comfortable with independent work
- Selective about social activities

**⚖️ Ambivert**
- Balanced personality traits
- Adaptable to different social situations
- Can be social or introspective as needed
- Versatile in various environments
- Bridges between introverts and extroverts

---

## 📊 Data Pipeline

```
Raw User Input (0-10 scale)
    ↓
Feature Vector Creation [26 features]
    ↓
Data Scaling (StandardScaler)
    ↓
Model Prediction
    ↓
Probability Calculation
    ↓
Class Mapping
    ↓
Output Formatting
    ↓
User Display
```

---

## 🔧 Configuration

### Customization Options

You can modify the following in `app.py`:

- **Color Scheme**: Adjust CSS gradients in the markdown styling
- **Button Labels**: Change emoji and text in the predict button
- **Feature Names**: Modify the `features` list
- **Confidence Display**: Toggle between model probability and fixed accuracy

---

## 📈 Model Training Notes

The model was trained on `personality_synthetic_dataset.csv` containing:
- **Size**: ~10 MB
- **Records**: Thousands of synthetic personality profiles
- **Features**: 26 behavioral attributes
- **Target**: Personality type classification (3 classes)

Training notebook available in `logistic_solutions.ipynb` for model evaluation and analysis.

---

## 🐛 Troubleshooting

### Issue: "Model files not found"
**Solution**: Ensure `personality_model.pkl` and `scaler.pkl` are in the same directory as `app.py`

### Issue: Application not loading
**Solution**: Run `pip install -r requirements.txt` again to ensure all dependencies are installed

### Issue: Streamlit port already in use
**Solution**: Run with a different port: `streamlit run app.py --server.port=8502`

### Issue: Predictions seem off
**Solution**: Ensure all sliders are adjusted to reflect your actual traits for accurate results

---

## 📝 Files Description

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application with UI and prediction logic |
| `requirements.txt` | All Python package dependencies |
| `personality_model.pkl` | Serialized trained ML model |
| `scaler.pkl` | Serialized data scaler for preprocessing |
| `personality_synthetic_dataset.csv` | Training dataset for model |
| `logistic_solutions.ipynb` | Model training and evaluation notebook |
| `logistic Que.ipynb` | Exploratory data analysis notebook |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Improvement
- Add more personality frameworks (Myers-Briggs, Big Five, etc.)
- Implement user data persistence
- Add visualization charts for trait analysis
- Create mobile-responsive design
- Add multilingual support

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Baljeet Kumar Patel**  
GitHub: [@BaljeetkumarPatel](https://github.com/BaljeetkumarPatel)

---

## 🙏 Acknowledgments

- Streamlit team for the amazing web framework
- Scikit-learn community for ML tools
- All contributors and users

---

## 📧 Contact & Support

For questions, suggestions, or issues, please:
- Open an issue on GitHub
- Check existing documentation
- Review the Jupyter notebooks for technical details

---

## 🚀 Future Enhancements

- [ ] API endpoint for programmatic access
- [ ] User profile saving and history tracking
- [ ] Advanced visualization dashboards
- [ ] Comparison with other personality frameworks
- [ ] Real-time model updates with user feedback
- [ ] Mobile application
- [ ] Export results as PDF report

---

**Last Updated**: April 26, 2026  
**Version**: 1.0.0  
**Status**: Active Development

---

*Discover your personality. Understand yourself better. 🌟*
