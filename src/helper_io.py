from typing import Any
from pathlib import Path
from pydantic import BaseModel, Field, create_model
from typing import Any, Dict, List, Optional, Type, Union
from datetime import datetime
import json

import uuid

import logging
logger = logging.getLogger(__name__)

def record_structured_prompt(directory_prompts: str|Path, schema_model: str) -> bool:
    pass

def record_ollama_output(directory_out: str|Path, llm_model: str) -> bool:
    pass

# def record_pydantic_model(directory_models: str|Path, model: BaseModel) -> None:
#     """Records a pydantic model as a JSON Schema
#        nb: Pydantics models are used to format the Ollama output

#     Args:
#         directory_models (str | Path): target directory
#         model (BaseModel): Pydantic model to register
#     """
#     filename = f"{datetime.now().strftime(format='%Y%m%d')[2:]}-{model.__name__}.json"
#     filepath = Path(directory_models, filename) 
#     print(filepath)
#     with open(filepath, 'w') as f:
#         json.dump(model.model_json_schema(), f, indent=2)



# Prompts I/O
def save_prompt(directory_prompt: str|Path, prompt:str, prompt_name: str, description: str = "", comment: str = "") -> None:
    # from textwrap import dedent
    filename = f"{prompt_name}.md"
    
    txt = f"""---
title: {prompt_name},
date.created: {datetime.now().strftime("%Y-%m-%dT%H:%M:%S")},
description: {description},
comment: {comment},
---
{prompt}
"""

    filepath = Path(directory_prompt, filename)
    logger.info(f"Saving prompt {prompt_name} to {filepath}")

    if filepath.exists():
        raise FileExistsError(f"The prompt named {prompt_name} is already registered in your target directory {filepath}")

    with open(filepath, 'w') as f:
        f.writelines(txt)

def load_prompt(directory_prompt: str|Path, schema_model: BaseModel) -> str:
    pass

# Structured Output
def save_structured_output(output: dict, directory_outputs: str|Path, prompt_name: str, llm_model: str) -> None:
    filename = f"{datetime.now().strftime(format='%Y%m%d_%H%M%S')[2:]}_{str(uuid.uuid4())[:3]}-{prompt_name}-{llm_model}.json"
    filepath = Path(directory_outputs, filename)
    logger.info(f"Saving output {filepath}")

    with open(filepath, 'w') as f:
        json.dump(output, f, indent=2)


# JSON Schema (Pydantic Models) I/O
## For load, code from https://github.com/pydantic/pydantic/issues/643#issuecomment-513240271
def save_pydantic_model_as_jsonschema(directory_schema: str|Path, schema_pydmodel: BaseModel) -> None:
    """_summary_

    Args:
        directory_schema (str | Path): home directory for the saved schemas
        schema_pydmodel (BaseModel): Pydantic model to register as JSON Schema
    """
    # filename = f"{datetime.now().strftime(format='%Y%m%d')[2:]}-{schema_pydmodel.__name__}.json"
    filename = f"{schema_pydmodel.__name__}.json"
    filepath = Path(directory_schema, filename)
    logger.info(f"Saving schema {schema_pydmodel.__name__} to {filepath}")

    if filepath.exists():
        raise FileExistsError(f"The schema named {schema_pydmodel.__name__} is already registered in your target directory {filepath}")

    with open(filepath, 'w') as f:
        json.dump(schema_pydmodel.model_json_schema(), f, indent=2)

def load_jsonschema_to_pydantic_model(json_schema: Dict[str, Any]) -> Type[BaseModel]:
    """
    Converts a JSON schema to a Pydantic BaseModel class.

    Args:
        json_schema: The JSON schema to convert.

    Returns:
        A Pydantic BaseModel class.
    """

    # Extract the model name from the schema title.
    model_name = json_schema.get('title')

    # Extract the field definitions from the schema properties.
    field_definitions = {
        name: json_schema_to_pydantic_field(name, prop, json_schema.get('required', []) )
        for name, prop in json_schema.get('properties', {}).items()
    }

    logger.info(f"Retrieving Pydantic model '{model_name}' from JSON")

    # Create the BaseModel class using create_model().
    return create_model(model_name, **field_definitions)

def json_schema_to_pydantic_field(name: str, json_schema: Dict[str, Any], required: List[str]) -> Any:
    """
    Converts a JSON schema property to a Pydantic field definition.

    Args:
        name: The field name.
        json_schema: The JSON schema property.

    Returns:
        A Pydantic field definition.
    """

    # Get the field type.
    type_ = json_schema_to_pydantic_type(json_schema)

    # Get the field description.
    description = json_schema.get('description')

    # Get the field examples.
    examples = json_schema.get('examples')

    # Create a Field object with the type, description, and examples.
    # The 'required' flag will be set later when creating the model.
    return (type_, Field(description=description, examples=examples, default=... if name in required else None))

def json_schema_to_pydantic_type(json_schema: Dict[str, Any]) -> Any:
    """
    Converts a JSON schema type to a Pydantic type.

    Args:
        json_schema: The JSON schema to convert.

    Returns:
        A Pydantic type.
    """

    type_ = json_schema.get('type')

    if type_ == 'string':
        return str
    elif type_ == 'integer':
        return int
    elif type_ == 'number':
        return float
    elif type_ == 'boolean':
        return bool
    elif type_ == 'array':
        items_schema = json_schema.get('items')
        if items_schema:
            item_type = json_schema_to_pydantic_type(items_schema)
            return List[item_type]
        else:
            return List
    elif type_ == 'object':
        # Handle nested models.
        properties = json_schema.get('properties')
        if properties:
            nested_model = json_schema_to_model(json_schema)
            return nested_model
        else:
            return Dict
    elif type_ == 'null':
        return Optional[Any]  # Use Optional[Any] for nullable fields
    else:
        raise ValueError(f'Unsupported JSON schema type: {type_}')


