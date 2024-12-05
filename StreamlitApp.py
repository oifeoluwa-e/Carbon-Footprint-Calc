#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install streamlit pandas openai


# In[2]:


import streamlit as st
import openai

# Set OpenAI API Key
openai.api_key = "key"

# Emission Factors
EMISSION_FACTORS = {
    "transport": 0.21,  # kg CO₂ per km
    "electricity": 0.475,  # kg CO₂ per kWh
    "diet": {"Omnivore": 2.5, "Vegetarian": 1.7, "Vegan": 1.5},  # kg CO₂ per day
    "waste": 3.5  # kg CO₂ per kg
}

# Title and Description
st.title("🌍 Carbon Footprint Calculator")
st.write("Calculate your carbon footprint and get tips to reduce it.")

# Inputs from User
st.header("Enter Your Details:")
transportation = st.number_input("Daily travel distance (in km):", min_value=0)
electricity = st.number_input("Monthly electricity usage (in kWh):", min_value=0)
diet = st.selectbox("Your primary diet:", ["Omnivore", "Vegetarian", "Vegan"])
waste = st.number_input("Weekly waste produced (in kg):", min_value=0)

# Calculate Emissions
def calculate_emissions(transportation, electricity, diet, waste):
    transport_emission = transportation * EMISSION_FACTORS["transport"] * 30  # monthly
    electricity_emission = electricity * EMISSION_FACTORS["electricity"]
    diet_emission = EMISSION_FACTORS["diet"][diet] * 30  # monthly
    waste_emission = waste * EMISSION_FACTORS["waste"] * 4  # monthly
    total_emissions = transport_emission + electricity_emission + diet_emission + waste_emission
    return total_emissions

if st.button("Calculate Footprint"):
    total_emissions = calculate_emissions(transportation, electricity, diet, waste)
    st.success(f"🌱 Your total carbon footprint is approximately **{total_emissions:.2f} kg CO₂/month**")

    # Get Suggestions
    def get_suggestions(emissions):
        prompt = f"My carbon footprint is {emissions:.2f} kg CO₂ per month. How can I reduce it?"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    if st.button("Get Suggestions"):
        suggestions = get_suggestions(total_emissions)
        st.info(f"💡 Suggestions to reduce your footprint:\n\n{suggestions}")


# In[ ]:




