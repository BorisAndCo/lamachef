# Llamma Chef

Objectif: Générer des personas de chefs et leurs recettes pour remplir la base de données de *La Main à la Pâte* (LaMaPa) au fil des milestones.
Nous utilisons la sortie structurée du modèle ``llama3` interfacée par l'environnement [ollama](https://github.com/ollama/ollama).
Le prompt engineering se fait sur des notebooks python


## Images and Models
Available images:
+ genuine (CPU/GPU, ~4go): https://hub.docker.com/r/ollama/ollama
+ alpine (CPU, ~70mo): https://hub.docker.com/r/alpine/ollama

Start with `deply-<image>_<model>.sh up`
Stop  with `deply-<image>_<model>.sh down`

## Prompt Engineering
The *prompts* are structured as branches ($b_1,$b_2,$b_{2.2},\ldots,b_n$)

+ UserChef
    + b1 *Unique UserChef* (~1min)
    + b2 *groupUserChef* (~1min for 5 chiefs): too few diversity, redundancy in fusion cooking
        + b201 *groupUserChef* with long bio (>50 words) and types (~12min for 6 chiefs)
        + b202 *groupUserChef* with shortened bio (>30 words) and French Cuisine (~xxxmin for 5 chiefs)
+ Recipes
    + b1 *Recipe* (~2min)



```py
UserChef(
    familyName='Ramos',
    givenName='Felipe',
    alternateName='Chef Felipe',
    nationality='Portuguese',
    birthDate='January 15, 1975',
    gender='Male',
    description=(
        'A charismatic and passionate chef with a love for bold flavors and vibrant presentations. Born in Lisbon, Por'
        'tugal, Felipe was trained in the classical traditions of Portuguese cuisine before venturing out to explore i'
        'nternational flavors. His culinary journey took him to Japan, where he immersed himself in the art of sushi-m'
        'aking, and later to Spain, where he discovered the magic of tapas culture.'
    ),
    prefCuisine=[
        'Portuguese',
        'Japanese',
        'Spanish',
    ],
)
```


## Ressources
+ Structuring Outputs from Ollama: https://ollama.com/blog/structured-outputs
+ OpenWebUI, An UI for LLMs: https://docs.openwebui.com/

## Roadmap
+ `ollama` en local