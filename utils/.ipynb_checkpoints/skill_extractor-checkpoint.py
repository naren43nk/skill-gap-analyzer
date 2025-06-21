import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd
import os
from tqdm import tqdm

# List of relevant data skills to match (can expand later)
SKILL_LIST = [
    "python", "r", "sql", "java", "c++", "excel", "tableau", "power bi", "spark",
    "hadoop", "aws", "azure", "gcp", "pandas", "numpy", "keras", "tensorflow",
    "scikit-learn", "matplotlib", "seaborn", "data visualization", "etl", "bash",
    "docker", "airflow", "git", "linux", "agile", "jira", "nlp", "deep learning"
]

def extract_skills(description, matcher, nlp):
    doc = nlp(description)
    matches = matcher(doc)
    found = set([doc[start:end].text.lower() for match_id, start, end in matches])
    return list(found)

def process_file(input_path, output_path):
    print(f"📄 Reading: {input_path}")
    df = pd.read_csv(input_path)

    # Load spaCy + build matcher
    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp(skill) for skill in SKILL_LIST]
    matcher.add("SKILLS", patterns)

    # Apply skill extraction
    tqdm.pandas(desc="🔎 Extracting skills")
    df['skills'] = df['description'].fillna("").progress_apply(lambda text: extract_skills(text, matcher, nlp))

    df.to_csv(output_path, index=False)
    print(f"✅ Skills saved to {output_path}")

if __name__ == "__main__":
    input_path = "data/all_jobs.csv"
    output_path = "data/all_skills.csv"
    process_file(input_path, output_path)
