import os
import xml.etree.ElementTree as ET

entries = []
input_dir = "src/gfx/buttons"
output_file="src/Buttons/Icons.py"
enum_file="src/Buttons/IconEnum.py"

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".svg"):
        full_path = os.path.join(input_dir, filename)

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            tree = ET.parse(full_path)
            root = tree.getroot()

            svg_id = root.attrib.get("id")
            if not svg_id:
                continue

        except Exception as e:
            continue

        entries.append((filename, svg_id, content))

entries.sort(key=lambda x: x[0])

with open(output_file, "w", encoding="utf-8") as out:
    for filename, svg_id, content in entries:
        out.write(f'{svg_id} = """{content}"""\n\n')

with open(enum_file, "w", encoding="utf-8") as enum:
    enum.write("from enum import IntEnum\n\n")
    enum.write("class IconEnum(IntEnum):\n")
    for index, (_, svg_id, _) in enumerate(entries, start=1):
        enum.write(f"    {svg_id} = {index}\n")

print(f"Stored {len(entries)} elements")
