from fastapi import FastAPI, Request
from pydantic import BaseModel
import random, re, os, requests
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class Problem(BaseModel):
    description: str

@app.post("/evolve")
async def evolve_code(problem: Problem):
    """
    Simulates a basic genetic algorithm evolution for Python code snippets.
    Uses random variations and simulated fitness scoring.
    """

    base_templates = [
        "def solve():\n    # TODO: write code for {desc}\n    pass",
        "def function():\n    # Handles {desc}\n    return None",
        "def main():\n    print('Solving {desc}')",
    ]

    # Step 1: Generate initial population
    population = [random.choice(base_templates).format(desc=problem.description) for _ in range(5)]

    # Step 2: Randomly mutate and evaluate
    evolved = []
    for code in population:
        mutation = re.sub(r"#.*", f"# mutation for {problem.description}", code)
        fitness = round(random.uniform(0.7, 1.0), 2)
        evolved.append({"code": mutation, "fitness": fitness})

    # Step 3: Pick best snippet
    best = max(evolved, key=lambda x: x["fitness"])

    # Optional: Simulate AI-assisted mutation via OpenRouter (not required)
    if OPENROUTER_API_KEY and random.random() > 0.6:
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "deepseek/deepseek-coder",
                    "messages": [
                        {"role": "system", "content": "You are an AI that improves Python code quality."},
                        {"role": "user", "content": f"Improve this code:\n{best['code']}"}
                    ],
                },
            )
            ai_data = response.json()
            ai_code = ai_data.get("choices", [{}])[0].get("message", {}).get("content", best["code"])
            best["code"] = ai_code.strip()
            best["fitness"] = round(best["fitness"] + 0.05, 2)
        except Exception:
            pass

    return {
        "best_snippet": best["code"],
        "fitness": best["fitness"],
        "generations": len(population),
        "description": problem.description
    }

@app.get("/")
def root():
    return {"message": "Welcome to Code Breeder AI 🧬 — use /evolve endpoint to generate code!"}
