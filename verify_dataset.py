from pathlib import Path

IMAGES = Path("train/images")
LABELS = Path("train/labels")

missing = [
    img.name
    for img in IMAGES.iterdir()
    if img.suffix.lower() in {".jpg", ".jpeg", ".png"}
    and not (LABELS / (img.stem + ".txt")).exists()
]

print(f"Images without a label file: {len(missing)}")

for name in missing:
    print(" -", name)