import os

class OTheme:
    def __init__(self, theme_name: str):
        self.Name = theme_name

        self.Foreground = "#FFFFFF"
        self.Background = "#000000"
        self.Text = "#AAAAAA"

    def load(self):
        filename = f"./themes/{self.Name}.theme"
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"File not found: {filename}")

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip().lower()
                value = value.strip()

                if key == "foreground":
                    self.Foreground = value
                elif key == "background":
                    self.Background = value
                elif key == "text":
                    self.Text = value
                else:
                    pass
