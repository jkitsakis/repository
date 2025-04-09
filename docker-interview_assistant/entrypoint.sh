
#!/bin/sh
ollama serve &

# Wait for Ollama to be ready
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama to start..."
  sleep 1
done

echo "Ollama is up. Pulling llama3..."
ollama pull llama3

tail -f /dev/null
