import pandas as pd
import ast
from collections import Counter

def explode_skills_column(df):
    df = df.copy()
    df["skills"] = df["skills"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
    return df.explode("skills")

def analyze_by_role(df):
    grouped = df.groupby(["role", "skills"]).size().reset_index(name="count")
    pivot = grouped.pivot(index="skills", columns="role", values="count").fillna(0).astype(int)
    return pivot.reset_index()

def analyze_by_city(df):
    grouped = df.groupby(["city", "skills"]).size().reset_index(name="count")
    pivot = grouped.pivot(index="skills", columns="city", values="count").fillna(0).astype(int)
    return pivot.reset_index()

def analyze_trend(df):
    grouped = df.groupby(["scraped_at", "skills"]).size().reset_index(name="count")
    pivot = grouped.pivot(index="skills", columns="scraped_at", values="count").fillna(0).astype(int)
    return pivot.reset_index()

def run_analysis(input_path="data/all_skills.csv"):
    df = pd.read_csv(input_path)
    df = explode_skills_column(df)

    skill_by_role = analyze_by_role(df)
    skill_by_city = analyze_by_city(df)
    skill_trend = analyze_trend(df)

    skill_by_role.to_csv("data/skill_by_role.csv", index=False)
    skill_by_city.to_csv("data/skill_by_city.csv", index=False)
    skill_trend.to_csv("data/skill_trend.csv", index=False)

    print("✅ Saved analysis to:")
    print("  • data/skill_by_role.csv")
    print("  • data/skill_by_city.csv")
    print("  • data/skill_trend.csv")

if __name__ == "__main__":
    run_analysis()
