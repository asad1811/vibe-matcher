import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import timeit
from openai import OpenAI


from products_data import load_products_df
import config




# Keys
api_key = config.OPENAI_API_KEY
client = OpenAI(api_key=api_key)

# Load Dataset 
df = load_products_df()
print(f"Loaded dataset with {len(df)} products.")
print(df.head())


# Generate Embeddings 
def get_embedding(text: str) -> list:
    """Generate text embedding using OpenAI text-embedding-ada-002."""
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding


print(" Generating embeddings for product descriptions...")
df["embedding"] = df["desc"].apply(get_embedding)
print(" Embeddings generated successfully!")


# Define Vibe Matcher 
def vibe_matcher(query: str, df: pd.DataFrame, top_k: int = 3):
    """
    Given a vibe query, embed it and return top_k most similar products.
    """
    query_emb = get_embedding(query)
    df["similarity"] = df["embedding"].apply(
        lambda e: cosine_similarity([e], [query_emb])[0][0]
    )
    return df.sort_values("similarity", ascending=False).head(top_k)[
        ["name", "desc", "tags", "similarity"]
    ]


# Run Sample Query 
sample_query = "energetic urban chic"
print(f"\n🔍 Query: '{sample_query}'\n")

matches = vibe_matcher(sample_query, df)

if matches["similarity"].max() < 0.4:
    print("⚠️ No strong vibe match found. Try rephrasing your query.")
else:
    print("✨ Top vibe matches:\n")
    print(matches.to_string(index=False))


# Evaluation: Multiple Queries 
queries = [
    "energetic urban chic"
]

results = []

for q in queries:
    start = timeit.default_timer()
    m = vibe_matcher(q, df)
    latency = timeit.default_timer() - start
    avg_sim = m["similarity"].mean()
    results.append({"query": q, "avg_sim": avg_sim, "latency": latency})

metrics = pd.DataFrame(results)
metrics["good_match"] = metrics["avg_sim"] > 0.7
print(metrics)


# Visualization: Latency Plot 
plt.figure(figsize=(8,4))
plt.bar(metrics["query"], metrics["latency"], color="skyblue", edgecolor="black")
plt.title(" Query Latency per Vibe")
plt.ylabel("Seconds")
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# Summary 
print("\n Evaluation Summary")
print(f"Total Queries Tested: {len(metrics)}")
print(f"Good Matches (>0.7 avg sim): {metrics['good_match'].sum()}")
print(f"Average Latency: {metrics['latency'].mean():.2f} sec")
