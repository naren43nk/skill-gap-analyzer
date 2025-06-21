import pandas as pd
from collections import Counter
import ast

def flatten_skill_list(skill_column):
    flat_skills = []
    for entry in skill_column:
        if isinstance(entry, str):
            try:
                skills = ast.literal_eval(entry)
                flat_skills.extend(skills)
            except Exception as e:
                print("Parsing error:", e)
    return flat_skills

def get_skill_frequencies(input_path, output_path, top_n=20):
    df = pd.read_csv(input_path)
    all_skills = flatten_skill_list(df['skills'])
    
    counter = Counter(all_skills)
    top_skills = counter.most_common(top_n)
    result_df = pd.DataFrame(top_skills, columns=["skill", "count"])
    
    result_df.to_csv(output_path, index=False)
    print(f"✅ Top {top_n} skill frequencies saved to {output_path}")
