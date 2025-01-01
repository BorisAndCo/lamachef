from typing import Any
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime
import json

def record_structured_prompt(directory_prompts: str|Path, schema_model: str) -> bool:
    pass

def record_ollama_output(directory_out: str|Path, llm_model: str) -> bool:
    pass

def record_pydantic_model(directory_models: str|Path, model: BaseModel) -> None:
    """Records a pydantic model as a JSON Schema
       nb: Pydantics models are used to format the Ollama output

    Args:
        directory_models (str | Path): target directory
        model (BaseModel): Pydantic model to register
    """
    filename = f"{datetime.now().strftime(format='%Y%m%d')[2:]}-{model.__name__}.json"
    filepath = Path(directory_models, filename) 
    print(filepath)
    with open(filepath, 'w') as f:
        json.dump(model.model_json_schema(), f, indent=2)