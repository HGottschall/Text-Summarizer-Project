import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Arquivo yaml {path_to_yaml} lido com sucesso")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError(
            f"Erro ao ler o arquivo yaml {path_to_yaml}. O arquivo está vazio ou não existe"
        )

    except Exception as e:
        logger.exception(f"Erro ao ler o arquivo yaml {path_to_yaml}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Diretório {path} criado com sucesso")


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
