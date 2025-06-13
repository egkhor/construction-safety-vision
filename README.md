# Construction Safety Vision AI

This open-source project uses computer vision and CoreML to detect construction site safety hazards (e.g., missing helmets, unsafe scaffolding) from images or video. It includes synthetic metadata for training, ready for iOS/macOS apps to assist supervisors.

## Features
- **Synthetic Metadata**: 500 samples with image IDs, hazard types, bounding boxes, and worker details.
- **CoreML Ready**: Designed for CreateML vision classifiers.
- **Community-Driven**: Contribute images, models, or Swift code.

## Project Structure
```
construction-safety-vision/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── src/
│   └── generate_synthetic_images.py
└── data/
    └── safety_images/
        └── safety_image_metadata.csv
```

## Getting Started
### Prerequisites
- Python 3.8+
- Xcode 13+ with CreateML
- macOS
- (Optional) Blender/Unity for synthetic image generation

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/egkhor/construction-safety-vision.git
   cd construction-safety-vision
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate metadata:
   ```bash
   python src/generate_synthetic_images.py
   ```
   This creates `data/safety_image_metadata.csv` and `data/safety_images/`.

### Using with CoreML
1. Add images to `data/safety_images/` matching `safety_image_metadata.csv`.
2. Open Xcode > CreateML > Vision Classifier.
3. Import images with metadata (use CreateML’s image annotation format).
4. Train and export as a `.mlmodel` for iOS/macOS apps.

## Notes
- **Synthetic Data**: Metadata is provided; generate images with Blender or contribute real images.
- **Scalability**: Increase `N_SAMPLES` in `generate_synthetic_images.py`.
- **Future Work**: Add video support, IoT integration, or multilingual alerts.

## Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details on submitting images, models, or code.

## License
MIT License. See [LICENSE](LICENSE).

## Contact
Connect via GitHub Issues or LinkedIn: [Your LinkedIn Profile URL]
