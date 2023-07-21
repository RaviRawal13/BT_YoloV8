from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
# Images config
IMAGES_DIR = ROOT /'dataset'/'test'/ 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'y701_jpg.rf.81a4472f77fdc1f31537342ceca340c9.jpg'
DEFAULT_DETECT_IMAGE = ROOT / 'runs' / 'segment' / 'predict' / 'y701_jpg.rf.81a4472f77fdc1f31537342ceca340c9.jpg'

# ML Model config
MODEL_DIR = ROOT / 'runs' / 'segment' / 'train' / 'weights'
SEGMENTATION_MODEL = MODEL_DIR / 'best.pt'


