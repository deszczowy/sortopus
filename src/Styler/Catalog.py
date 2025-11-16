import os

from .Theme import OTheme

class OCatalog:
    BASE_PATH = "./themes"

    def __init__(self):
        if not os.path.isdir(self.BASE_PATH):
            raise NotADirectoryError(self.BASE_PATH)

        self._themes = self._scan()

    def _scan(self):
        themes = []
        for filename in os.listdir(self.BASE_PATH):
            if filename.lower().endswith(".theme"):
                name = os.path.splitext(filename)[0]
                themes.append(name)
        return themes

    @property
    def names(self):
        return list(self._themes)

    def get(self, theme_name: str):
        if theme_name not in self._themes:
            raise ValueError(f"Nie znaleziono tematu: {theme_name}")

        full_path = os.path.join(self.BASE_PATH, f"{theme_name}.theme")

        theme = OTheme(theme_name)

        cwd = os.getcwd()
        try:
            os.chdir(self.BASE_PATH)
            theme.load()
        finally:
            os.chdir(cwd)

        return theme
