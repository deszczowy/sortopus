from .Style import STYLE
from .Theme import OTheme

class OStyler:

    def get(self, theme_name: str) -> str:

        theme = OTheme(theme_name)
        theme.load()

        if theme is None:
            raise ValueError("Theme cannot be None.")

        # Słownik mapujący placeholdery na wartości z OTheme
        replacements = {
            "{@color}": theme.Foreground,
            "{@back}": theme.Background,
            "{@text}": theme.Text,
        }

        result = STYLE
        for placeholder, value in replacements.items():
            result = result.replace(placeholder, value)

        return result
