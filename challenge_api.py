from pathlib import Path
import os
DATASET_DIR = Path(".")


def load_large():
    return (DATASET_DIR/'large.bmp')

def iter_frames():
    z = DATASET_DIR/'zoomed'
    for p in sorted(z.iterdir()):
        if p.is_file() and p.suffix.lower() in {'.png','.jpg','.jpeg','.bmp','.tif','.tiff'}:
            yield p.stem, p
