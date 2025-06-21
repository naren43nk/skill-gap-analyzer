import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="UK Job Skill Gap Analyzer", layout="wide")
st.title("📊 UK Job Skill Gap Analyzer")
st.markdown("Explore skill demand across data roles and cities using real job market data.")

# Load Data
@st.cache_data
def load_data():
    skill_role = pd.read_csv("data/skill_by_role.csv")
    skill_city = pd.read_csv("data/skill_by_city.csv")
    skill_trend = pd.read_csv("data/skill_trend.csv")
    return skill_role, skill_city, skill_trend

skill_role_df, skill_city_df, skill_trend_df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
roles = skill_role_df.columns[1:]  # skip 'skills' column
cities = skill_city_df.columns[1:]
dates = skill_trend_df.columns[1:]

selected_role = st.sidebar.selectbox("Select Job Role", roles)
selected_city = st.sidebar.selectbox("Select City", cities)

# Top Skills by Role
st.markdown(f"### 🔧 Top Skills for **{selected_role.title()}**")
role_data = skill_role_df[["skills", selected_role]].rename(columns={"skills": "skill"})
role_data = role_data.sort_values(by=selected_role, ascending=False).head(20)
st.bar_chart(role_data.set_index("skill"))

# Top Skills by City
st.markdown(f"### 📍 Top Skills in **{selected_city.title()}**")
city_data = skill_city_df[["skills", selected_city]].rename(columns={"skills": "skill"})
city_data = city_data.sort_values(by=selected_city, ascending=False).head(20)
st.bar_chart(city_data.set_index("skill"))

# Skill Trends Over Time
st.markdown("### 📈 Skill Trends Over Time")
available_skills = skill_trend_df["skills"].tolist()
selected_skills = st.multiselect(
    "Choose up to 5 skills to compare trends",
    available_skills,
    default=["python", "sql", "power bi"]
)

if selected_skills:
    trend_data = skill_trend_df[skill_trend_df["skills"].isin(selected_skills)].set_index("skills").T
    st.line_chart(trend_data)

# Footer
st.markdown("---")
st.markdown("Built by **Narendran Mohan** | Powered by **Adzuna + Streamlit**")
