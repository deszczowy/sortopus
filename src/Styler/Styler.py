from .Style import STYLE
from .Theme import OTheme

class OStyler:

    Theme = None

    def get(self, theme_name: str) -> str:

        self.Theme = OTheme(theme_name)
        self.Theme.load()

        if self.Theme is None:
            raise ValueError("Theme cannot be None.")

        # Słownik mapujący placeholdery na wartości z OTheme
        replacements = {
            "{@color}": self.Theme.Foreground,
            "{@back}": self.Theme.Background,
            "{@text}": self.Theme.Text,
        }

        result = STYLE
        for placeholder, value in replacements.items():
            result = result.replace(placeholder, value)

        return result
    
    @property
    def Foreground(self) -> str:
        return self.Theme.Foreground
