
# ✨ **TripGenie AI – Intelligent Travel Planning System**


# 🌍 TripGenie AI

### Your Intelligent AI Travel Companion

TripGenie AI is an industry-level travel planning system powered by Generative AI.
It creates personalized multi-day itineraries by combining Large Language Models (LLMs) with real-time APIs and smart business logic.

Unlike simple AI chatbots, TripGenie AI integrates:

* 🌦 Live weather data
* 💱 Currency conversion
* 🏨 Budget-based hotel recommendations
* 🗺 Location intelligence (Google Maps links)
* ⚡ Parallel AI execution using LangChain

---

## 🚀 Features

* 🧠 AI-generated day-wise travel itinerary
* 🌦 Real-time weather integration
* 💱 Live currency conversion support
* 🏨 Budget-filtered hotel suggestions (mock API logic)
* 🗺 Auto-generated Google Maps search links
* ⚡ RunnableParallel execution for optimized performance
* 💰 Hybrid cost estimation engine
* 🎯 Structured modular architecture

---

## 🏗 System Architecture

```text
User Input (Streamlit UI)
        ↓
LangChain Orchestration
        ↓
RunnableParallel
   ├── LLM Itinerary Generator
   ├── Weather API Tool
   ├── Hotel Logic Engine
   └── Currency Converter
        ↓
Structured Output
        ↓
Interactive Streamlit UI
```

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **OpenAI (gpt-4o-mini)**
* **Weather API (OpenWeather / Open-Meteo)**
* **Frankfurter / ExchangeRate API**
* **RunnableLambda & RunnableParallel**

---

## 🔐 Environment Setup

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key
CURRENCY_API_KEY=your_currency_api_key
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/bhupender5/tripgenie-ai.git
cd tripgenie-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🎯 Why TripGenie AI Is Industry-Level

✔ Modular architecture
✔ Hybrid AI + rule-based logic
✔ Parallel execution
✔ Multi-API integration
✔ Scalable design principles
✔ Cost-aware LLM usage

This mirrors how modern travel platforms like
MakeMyTrip and
Airbnb integrate AI-driven personalization with backend intelligence.

---

## 📈 Future Enhancements

* Redis caching
* User login & trip history
* Streaming AI responses
* PDF export
* Docker deployment
* Cloud hosting
* Database integration

---

## 👨‍💻 Author

**Bhupender Singh**
B.Tech | AI & Data Enthusiast
Passionate about GenAI, DevOps & Intelligent Systems

GitHub: [https://github.com/bhupender5](https://github.com/bhupender5)
LinkedIn: [https://www.linkedin.com/in/bhupinder-singh-bba271187](https://www.linkedin.com/in/bhupinder-singh-bba271187)

---


