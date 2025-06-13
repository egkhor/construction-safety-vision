import pandas as pd
import numpy as np
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
N_SAMPLES = 500
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "safety_image_metadata.csv")
IMAGE_DIR = os.path.join(OUTPUT_DIR, "safety_images")

# Hazard types and attributes
HAZARD_TYPES = ['no_helmet', 'unsafe_scaffold', 'missing_guardrail', 'none']
WORKER_POSITIONS = ['left', 'center', 'right']

def generate_image_metadata(has_hazard: bool) -> dict:
    """Generate synthetic metadata for construction site images."""
    image_id = f"IMG_{random.randint(1000, 9999)}"
    hazard_type = random.choice(HAZARD_TYPES) if has_hazard else 'none'
    worker_count = random.randint(1, 10) if has_hazard else random.randint(1, 5)
    worker_position = random.choice(WORKER_POSITIONS)
    bbox_x = random.uniform(0, 0.5) if has_hazard else 0
    bbox_y = random.uniform(0, 0.5) if has_hazard else 0
    bbox_width = random.uniform(0.1, 0.3) if has_hazard else 0
    bbox_height = random.uniform(0.1, 0.3) if has_hazard else 0
    lighting = random.choice(['bright', 'dim', 'shadow'])

    return {
        'image_id': image_id,
        'hazard_type': hazard_type,
        'worker_count': worker_count,
        'worker_position': worker_position,
        'bbox_x': bbox_x,
        'bbox_y': bbox_y,
        'bbox_width': bbox_width,
        'bbox_height': bbox_height,
        'lighting': lighting,
        'has_hazard': int(has_hazard)
    }

def main():
    """Generate synthetic image metadata and create image directory."""
    os.makedirs(IMAGE_DIR, exist_ok=True)

    data = {
        'image_id': [],
        'hazard_type': [],
        'worker_count': [],
        'worker_position': [],
        'bbox_x': [],
        'bbox_y': [],
        'bbox_width': [],
        'bbox_height': [],
        'lighting': [],
        'has_hazard': []
    }

    for _ in range(N_SAMPLES):
        has_hazard = random.choice([True, False])
        metadata = generate_image_metadata(has_hazard)
        for key in metadata:
            data[key].append(metadata[key])

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Metadata generated and saved to {OUTPUT_FILE}")
    print(f"Image directory created at {IMAGE_DIR}")
    print(df.head())

if __name__ == "__main__":
    main()