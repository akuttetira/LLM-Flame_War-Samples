import shutil
from pathlib import Path
import json

input_folder = Path("content/Output_v4")
output_folder = Path("content/Output_fixed")
failure_output_folder = Path("content/Output_Failures_2")
failure_output_folder.mkdir(parents=True, exist_ok=True)

counter = 0

for file_path in input_folder.rglob("*.json"):
    if not file_path.is_file():
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        conversation_data = json.load(f)

    # Fix JSON wrapped inside a string
    if isinstance(conversation_data, str):
        cleaned = conversation_data.strip()

        # Remove wrapping quotes IF they wrap the whole string
        if cleaned.startswith('"') and cleaned.endswith('"'):
            cleaned = cleaned[1:-1]

        try:
            conversation_data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            print("\n--- BAD JSON STRING IN FILE ---")
            print("FILE:", file_path)
            print("--- SKIPPING FILE ---\n")
            counter += 1

            relative_path = file_path.relative_to(input_folder)
            output_path = (failure_output_folder / relative_path).with_suffix(".json")
            output_path.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy(file_path, output_path)

            continue



    judgement = conversation_data["judgement"]
    steering = conversation_data["steering"]

    data = {"judgement": judgement, "steering": steering}

    relative_path = file_path.relative_to(input_folder)
    output_path = (output_folder / relative_path).with_suffix(".json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as out_file:
        json.dump(data, out_file, indent=2, ensure_ascii=True)


print (counter)