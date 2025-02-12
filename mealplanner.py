
import google.generativeai as genai
import streamlit as st

# Configure Gemini AI
genai.configure(api_key="AIzaSyC66AKH068dNmD1iFiUaG9LLmZJ_UG2XEE")  # Replace with your Gemini API key
model = genai.GenerativeModel('gemini-pro')

def get_meal_plan(diet_type, calorie_goal):
    """
    Generate a meal plan using Gemini AI.
    :param diet_type: Type of diet (e.g., vegetarian, keto, vegan)
    :param calorie_goal: Daily calorie goal (e.g., 2000)
    :return: Generated meal plan
    """
    prompt = f"""
    Create a {diet_type} meal plan for a day with a total of {calorie_goal} calories.
    Include breakfast, lunch, dinner, and two snacks.
    Provide detailed recipes and calorie counts for each meal.
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("Welcome to the Meal Planner!")
st.write("Please enter your diet preferences and calorie goal below.")

# Diet type input
diet_type = st.selectbox(
    "Select your diet type",
    ["Vegetarian", "Keto", "Vegan", "Paleo", "Gluten-Free"]
)

# Calorie goal input
calorie_goal = st.number_input(
    "Enter your daily calorie goal", min_value=100, max_value=5000, value=2000
)

# Button to generate the meal plan
if st.button("Generate Meal Plan"):
    if calorie_goal:
        meal_plan = get_meal_plan(diet_type, calorie_goal)
        st.subheader("Here's your personalized meal plan:")
        st.write(meal_plan)
    else:
        st.error("Please enter a valid calorie goal.")
