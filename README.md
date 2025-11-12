# 🧬 Code Breeder AI

> An experimental AI-powered **genetic algorithm engine** that automatically evolves and improves Python code snippets to solve given programming tasks — showcasing AI-assisted code generation with real-world value.

---

## 🚀 Overview

**Code Breeder AI** uses principles of **evolutionary algorithms** and **LLM-assisted mutation** to generate, test, and evolve small Python programs.  
Given a problem description, the system:
1. Generates an initial population of code snippets.
2. Tests them using predefined fitness metrics.
3. Evolves them through crossover + mutation.
4. Returns the best-performing snippet.

This helps developers **automate repetitive code generation** or explore **AI-driven problem solving**.

---

## 🧠 Core Features

- ⚙️ **FastAPI Backend** — handles task creation and genetic evolution.
- 🧬 **Genetic Algorithm Engine** — iteratively improves Python code snippets.
- 🧩 **LLM Integration** — uses OpenRouter or any compatible API.
- 🧑‍💻 **Simple Frontend Playground** — test code evolution in real time.
- 📈 **Memory-Based Learning (Optional)** — stores fitness histories for adaptive evolution.

---

## 🧩 Architecture Diagram

```text
           ┌────────────────────────────┐
           │         Frontend            │
           │ (HTML + JS Playground UI)   │
           └─────────────┬───────────────┘
                         │  (HTTP POST)
                         ▼
           ┌────────────────────────────┐
           │         FastAPI Server      │
           │ - Handles tasks             │
           │ - Runs Genetic Algorithm    │
           │ - Calls AI API (LLM)        │
           └─────────────┬───────────────┘
                         │
                         ▼
           ┌────────────────────────────┐
           │      AI Model / OpenRouter  │
           │ "ENTER YOUR API KEY HERE"   │
           └────────────────────────────┘
