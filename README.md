# Llamma Chef
LLamachef provides a quick-ollama deployment using docker and shell-script provisioning. It uses the [Structured Output](https://ollama.com/blog/structured-outputs) feature of [ollama](https://github.com/ollama/ollama).
The objective is to generate *Chefs* personas and their *Recipes* according to *La Main à la Pâte (LMP)*  data model in order to seed the database. It follows the evolution of LMP accross its milestones and the evolution of the data mode. LMP data model is detailed in the [Overview Document](https://github.com/Lucccyo/lmp_main/blob/main/design_documents/0_Overview.md). 

Jupyter notebooks and helper functions are made available to ease the process, save the progress in prompt engineering and format the outputs for facilitating the seeding.



## Images and Models
Available images:
+ genuine (CPU/GPU, ~2go?): https://hub.docker.com/r/ollama/ollama
+ alpine (CPU, ~70mo): https://hub.docker.com/r/alpine/ollama

Start with `deploy-<image>_<model>.sh up`
Stop  with `deploy-<image>_<model>.sh down`
Current best `deploy_genuine_llama32.sh`

## Prompt Engineering
*Prompt* engineering is a non-linear process, requiring iterating, branching and exploring. Given that we aim for a structured output, each process start with a schema then branches and is versioned.
*Prompts* are saved in Markdown, with a YAML frontmatter that contain the `schema_name` and may be completed with an optional `description` and `comment`

### I/O Formatting
+ *JSON Schemas* are formatted `<schema_name>.json`
+ *Prompts* are formatted `<schema_name>_<branch_version>.md`
+ *Outputs* are formatted `<timestamp>-<prompt_reference>-<llm_model>.md`

<!--
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

-->

