# Llamma Chef

Objectif: Générer des personas de chefs et leurs recettes pour remplir la base de données de *La Main à la Pâte* (LaMaPa) au fil des milestones.
Nous utilisons la sortie structurée du modèle ``llama3` interfacée par l'environnement [ollama](https://github.com/ollama/ollama).
Le prompt engineering se fait sur des notebooks python


## Images and Models
+ official (CPU/GPU, ~4go): https://hub.docker.com/r/ollama/ollama
+ alpine (CPU, ~70mo): https://hub.docker.com/r/alpine/ollama

Start with `docker-compose `


## Ressources
+ Structuring Outputs from Ollama: https://ollama.com/blog/structured-outputs
+ OpenWebUI, An UI for LLMs: https://docs.openwebui.com/


## Roadmap
+ `ollama` en local