import streamlit as st
import requests
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

# Load env
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_KEY = os.getenv("WEATHER_API_KEY")
CURRENCY_KEY = os.getenv("CURRENCY_API_KEY")

st.set_page_config(page_title="TripGenie AI", layout="wide")
st.title("Plan Your Trip With AI")

# User Inputs
col1, col2, col3 = st.columns(3)

with col1:
    country = st.text_input("Country")

with col2:
    city = st.text_input("City / State")

with col3:
    days = st.number_input("Days", min_value=1, max_value=30)

budget_type = st.selectbox("Budget Type", ["Low", "Medium", "Luxury"])
currency = st.text_input("Convert Budget To (e.g., USD, INR, EUR)", value="USD")

# Initialize LLM
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
parser = StrOutputParser()

# ----------------------------
# 1️⃣ Weather API Tool
# ----------------------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"
    response = requests.get(url).json()
    if "main" in response:
        return f"{response['main']['temp']}°C, {response['weather'][0]['description']}"
    return "Weather data unavailable"

weather_tool = RunnableLambda(lambda x: get_weather(x["city"]))

# ----------------------------
# 2️⃣ Hotel Mock Tool
# ----------------------------
HOTELS = {
    "Goa": [
        {"name": "Beach Resort", "price": 8000, "rating": 4.5},
        {"name": "Budget Inn", "price": 2500, "rating": 4.0},
        {"name": "Luxury Palace", "price": 15000, "rating": 4.8},
    ]
}

def get_hotels(city, budget):
    hotels = HOTELS.get(city, [])
    if budget == "Low":
        return [h for h in hotels if h["price"] <= 3000]
    elif budget == "Medium":
        return [h for h in hotels if 3000 < h["price"] <= 10000]
    return hotels

hotel_tool = RunnableLambda(lambda x: get_hotels(x["city"], x["budget_type"]))

# ----------------------------
# 3️⃣ Currency Conversion Tool
# ----------------------------
def convert_currency(amount, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_KEY}/latest/INR"
    data = requests.get(url).json()
    if data["result"] == "success":
        rate = data["conversion_rates"].get(target_currency.upper())
        if rate:
            return round(amount * rate, 2)
    return "Conversion unavailable"

currency_tool = RunnableLambda(
    lambda x: convert_currency(x["estimated_budget"], x["currency"])
)

# ----------------------------
# 4️⃣ Google Maps Link Generator
# ----------------------------
def generate_maps_link(place):
    return f"https://www.google.com/maps/search/?api=1&query={place.replace(' ', '+')}"

# ----------------------------
# 5️⃣ LLM Itinerary Prompt
# ----------------------------
prompt = PromptTemplate.from_template("""
You are a professional travel planner.

Create a {days}-day itinerary for {city}, {country}.
Budget type: {budget_type}

Include:
- Day-wise plan
- Must visit places
- Travel tips
""")

llm_chain = prompt | model | parser

# ----------------------------
# 6️⃣ Parallel Execution
# ----------------------------
final_chain = RunnableParallel(
    itinerary=llm_chain,
    weather=weather_tool,
    hotels=hotel_tool
)

# ----------------------------
# RUN
# ----------------------------
if st.button("Generate Smart Trip Plan 🚀"):
    if city and country and days:
        with st.spinner("Planning your trip..."):

            result = final_chain.invoke({
                "city": city,
                "country": country,
                "days": days,
                "budget_type": budget_type
            })

            # Estimate base budget logic
            base_budget = days * (3000 if budget_type == "Low" else 7000 if budget_type == "Medium" else 15000)

            converted_budget = convert_currency(base_budget, currency)

        # UI Display
        tab1, tab2, tab3, tab4 = st.tabs(["📅 Itinerary", "🌦 Weather", "🏨 Hotels", "💰 Budget"])

        with tab1:
            st.write(result["itinerary"])

        with tab2:
            st.write(result["weather"])

        with tab3:
            st.write(result["hotels"])

        with tab4:
            st.write(f"Estimated Budget (INR): ₹{base_budget}")
            st.write(f"Converted Budget ({currency.upper()}): {converted_budget}")

            st.markdown(f"[View {city} on Google Maps]({generate_maps_link(city)})")

    else:
        st.warning("Please fill all fields.")