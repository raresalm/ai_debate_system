# 🏛️ Local AI Debate System

A turn-based, multi-agent debate system that runs entirely on your local machine using **Docker** and **Ollama**. No APIs, no costs, 100% privacy.

## 🚀 Features
- **Turn-Based Logic:** Opening arguments -> Rebuttals -> Final Verdict.
- **Local LLMs:** Powered by Llama 3 (Pro), Mistral (Con), and Phi-3 (Judge).
- **Zero Cost:** Uses your computer's hardware via Ollama.
- **Dockerized:** Easy deployment on Windows.

## 🛠️ Prerequisites
1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. [Ollama for Windows](https://ollama.com/)
3. Download the models (run in terminal):
   ```bash
   ollama pull llama3
   ollama pull mistral
   ollama pull phi3
