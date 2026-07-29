from pathlib import Path

folder = Path("data")
file_path = folder / "notes.txt"

if file_path.exists():
    print(file_path.read_text())
