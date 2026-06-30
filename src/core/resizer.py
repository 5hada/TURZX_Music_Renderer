from pathlib import Path
from PIL import Image

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

SIZE = 200  # 원하는 크기 (예: 128, 256, 512)


class Resizer:
    def __init__(self):
        self.size: int = SIZE
        self.input_dir: str = INPUT_DIR
        self.output_dir: str = OUTPUT_DIR
        self.prev_rgb
        self.cur_rgb

    def resize(self, fileName: str) -> bool :
        input_path: str = self.input_dir + fileName

        if input_path.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            return False
        with Image.open(input_path) as img:
            img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
            out_path = self.output_dir / fileName
            img.save(out_path)
            return True


