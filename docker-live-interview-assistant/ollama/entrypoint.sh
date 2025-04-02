#!/bin/sh

echo "🧠 Starting Ollama and loading models..."

# Start Ollama in the background
ollama serve &

# Give Ollama some time to initialize
sleep 3

# Pull models
ollama pull codellama
ollama pull mistral
ollama pull llama2
ollama pull gemma

# Wait to keep the container running
wait
