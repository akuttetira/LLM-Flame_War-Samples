import json
from datetime import date, datetime
from pathlib import Path

input_folder = Path("Dataset_v2")
output_folder = Path("Flattened_v2")

def flatten_thread (node: dict) -> list[dict]:
    msgs = [{"author": node["From"], "text": node["Reply_Text"].strip()}]
    for child in node.get("Replies", []):
        msgs.extend(flatten_thread(child))
    return msgs
    

for file_path in input_folder.rglob("*.json"):
    if file_path.is_file():
        # Load JSON
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Flatten all threads
        flattened = []
        post = [{"title": data.get("Post_Title"), "text": data.get("post_text")}]
        flattened.extend(post)
        for thread in data.get("Threads", []):
            flattened.extend(flatten_thread(thread))

        # Build output path (mirror folder structure)
        relative_path = file_path.relative_to(input_folder)
        output_path = output_folder / relative_path

        # Create parent directories
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save flattened output
        with open(output_path, "w", encoding="utf-8") as out_file:
            json.dump(flattened, out_file, indent=2, ensure_ascii=False)

        print(f"Flattened: {file_path} → {output_path}")

        





