import json
from pathlib import Path
from typing import Dict

class Config:

    def load_config(self, config_path: Path) -> Dict:
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        with config_path.open('r', encoding='utf-8') as f:
            cfg = json.load(f)

        required = ['main_dir', 'deleted_dir', 'defer1_dir', 'defer1_label', 'defer2_dir', 'defer2_label']
        for k in required:
            if k not in cfg:
                raise KeyError(f"Required key not found in config file: {k}")
        return cfg