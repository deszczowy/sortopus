import json

from pathlib import Path
from typing import List, Dict, Optional

from . import Files

LIST_FILENAME = "list.txt"

class Sortopus:

    def __init__(self, config: Dict):
        self.config = config
        self.main_dir = Path(config['main_dir'])
        self.deleted_dir = Path(config['deleted_dir'])
        self.defer1_dir = Path(config['defer1_dir'])
        self.defer1_label = config.get('defer1_label', 'Move 1')
        self.defer2_dir = Path(config['defer2_dir'])
        self.defer2_label = config.get('defer2_label', 'Move 2')
        self.defer3_dir = Path(config['defer3_dir'])
        self.defer3_label = config.get('defer3_label', 'Move 3')

        # ensure directories exist
        for d in (self.main_dir, self.deleted_dir, self.defer1_dir, self.defer2_dir):
            try:
                d.mkdir(parents=True, exist_ok=True)
            except Exception:
                pass

        self.list_file = self.main_dir / LIST_FILENAME
        self.items: List[Dict] = []  # Elements {'path': str, 'status': int}
        self.current_index: Optional[int] = None

        self.load_or_create_list()

    def load_or_create_list(self):
        if self.list_file.exists():
            try:
                with self.list_file.open('r', encoding='utf-8') as f:
                    data = json.load(f)
                # podstawowa walidacja
                if isinstance(data, list):
                    self.items = data
                else:
                    raise ValueError('list.txt nie zawiera listy JSON')
            except Exception as e:
                raise RuntimeError(f'List cannot be read {self.list_file}: {e}')
        else:
            # skanuj katalog główny
            images = Files.Files().find_images_recursively(self.main_dir)
            self.items = []
            for p in images:
                self.items.append({'path': str(p), 'status': 0})
            self.save_list()

        # znajdź pierwszy indeks ze statusem 0
        self.current_index = self.find_next_status_index(-1, 0)
        if self.current_index is None and len(self.items) > 0:
            # jeśli brak 0, ustaw na 0
            self.current_index = 0

    def save_list(self):
        try:
            with self.list_file.open('w', encoding='utf-8') as f:
                json.dump(self.items, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print('Write error list.txt:', e)

    def find_next_status_index(self, start_idx: int, status: int) -> Optional[int]:
        # znajdź index > start_idx z danym status
        for i in range(start_idx + 1, len(self.items)):
            if self.items[i].get('status') == status:
                return i
        return None

    def clamp_index(self, idx: int) -> int:
        if idx < 0:
            return 0
        if idx >= len(self.items):
            return len(self.items) - 1
        return idx

    def get_current_item(self) -> Optional[Dict]:
        if self.current_index is None:
            return None
        if 0 <= self.current_index < len(self.items):
            return self.items[self.current_index]
        return None

    def set_status(self, index: int, status: int):
        if 0 <= index < len(self.items):
            self.items[index]['status'] = status
            self.save_list()

    def move_file_and_update(self, index: int, target_dir: Path, new_status: int):
        item = self.items[index]
        src = Path(item['path'])
        if src.exists():
            target_dir.mkdir(parents=True, exist_ok=True)
            dest = target_dir / src.name
            # unikaj nadpisania: dodaj sufiks gdy potrzeba
            counter = 1
            base = dest.stem
            suffix = dest.suffix
            while dest.exists():
                dest = target_dir / f"{base}_{counter}{suffix}"
                counter += 1
            try:
                shutil.move(str(src), str(dest))
                item['path'] = str(dest)
            except Exception as e:
                print('Exception during file move:', e)
        else:
            # plik nie istnieje — nadal ustaw status i zostaw ścieżkę jak była
            print('File does not exists:', src)
        item['status'] = new_status
        self.save_list()

    def go_to_next(self):
        if self.current_index is None:
            return
        if self.current_index < len(self.items) - 1:
            self.current_index += 1
        # jeśli na końcu — zostajemy

    def go_to_prev(self):
        if self.current_index is None:
            return
        if self.current_index > 0:
            self.current_index -= 1
