import json
from pathlib import Path
from typing import Dict, List, NamedTuple

class DeferAction(NamedTuple):
    dir: str
    label: str

class Config:
    
    def load_config(self, config_path: Path) -> Dict:
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with config_path.open('r', encoding='utf-8') as f:
            cfg = json.load(f)

        # Wymagane pola bazowe
        required_base = ['main_dir', 'deleted_dir', 'actions']
        for k in required_base:
            if k not in cfg:
                raise KeyError(f"Required key not found in config file: {k}")

        # Walidacja i konwersja 'actions'
        if not isinstance(cfg['actions'], list):
            raise ValueError("'actions' must be a list")
        
        actions: List[DeferAction] = []
        for i, item in enumerate(cfg['actions'], start=1):
            if not isinstance(item, dict):
                raise ValueError(f"Action {i} must be a dictionary")
            if 'dir' not in item or 'label' not in item:
                raise ValueError(f"Action {i} must contain 'dir' and 'label'")
            actions.append(DeferAction(dir=str(item['dir']), label=str(item['label'])))

        # Zwracamy tylko potrzebne dane
        return {
            'main_dir': str(cfg['main_dir']),
            'deleted_dir': str(cfg['deleted_dir']),
            'actions': actions
        }