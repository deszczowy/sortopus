from pathlib import Path
from typing import List

class Files:

    SUPPORTED_EXTS = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png')  # dozwolone rozszerzenia

    def find_images_recursively(self, root: Path) -> List[Path]:
        results = []
        for p in root.rglob('*'):
            if p.suffix.lower() in self.SUPPORTED_EXTS and p.is_file():
                results.append(p)
        results.sort()
        return results
