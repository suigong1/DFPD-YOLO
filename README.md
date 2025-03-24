# DFPD-YOLO: Diffusion-Focused Pyramid Dynamic Task-aligned Detection Head YOLO

## Introduction
Object detection in road scenes presents significant challenges due to multi-scale variations and complex backgrounds. Many existing methods struggle with detecting small objects that have blurred features and low contrast with their surroundings. Additionally, traditional detection heads separate classification and localization tasks, neglecting their potential correlation and limiting overall performance.

To address these issues, we propose **DFPD-YOLO (Diffusion-Focused Pyramid Dynamic Task-aligned Detection Head YOLO)**. Our model introduces improvements in **feature extraction** and **task alignment**, enhancing detection accuracy and robustness. The key contributions are as follows:

- **FocusFeature and Feature Diffusion Mechanism in the Neck**: These components improve the context-awareness of multi-scale features, helping detect small objects more accurately.
- **Dynamic Task-aligned Detection Head (DTDH)**: This structure strengthens the interaction between classification and localization tasks, improving detection performance.
- **WIoU as the Bounding Box Regression Loss**: This loss function reduces the impact of low-quality samples on anchor box regression, speeds up network convergence, and enhances localization precision.
- **Extensive Experiments on KITTI Dataset**: The results show significant improvements, especially for small and occluded road objects.

## Network Architecture
The DFPD-YOLO network consists of the following major components:

- **Backbone**: Extracts deep hierarchical features from input images.
- **Neck (FocusFeature & Feature Diffusion Mechanism)**: Enhances feature representation to improve small object detection.
- **Detection Head (DTDH)**: Aligns classification and localization tasks dynamically, improving detection robustness.
- **Loss Function (WIoU)**: Optimizes bounding box regression for better localization accuracy.

## Installation
To set up the environment and run DFPD-YOLO, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/DFPD-YOLO.git
   cd DFPD-YOLO
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the KITTI dataset and place it in the appropriate directory.

## Usage
### Training
To train DFPD-YOLO on the KITTI dataset, run:
```bash
python train.py --data kitti.yaml --epochs 100 --batch-size 16 --img-size 640
```

### Inference
To test the trained model on an image:
```bash
python detect.py --weights best.pt --source test_image.jpg
```

### Evaluation
To evaluate performance on KITTI:
```bash
python val.py --data kitti.yaml --weights best.pt
```

## Experimental Results
Our experiments on the KITTI dataset show that **DFPD-YOLO significantly improves detection accuracy**, especially for **small and occluded objects**. The proposed enhancements lead to better feature representation, faster convergence, and improved localization precision.

## Citation
If you find this work useful, please consider citing our paper:
```
@article{your_paper,
  author    = {Your Name},
  title     = {DFPD-YOLO: Diffusion-Focused Pyramid Dynamic Task-aligned Detection Head YOLO},
  journal   = {Your Journal/Conference},
  year      = {2025},
}
```

## Contact
For any inquiries, please contact **your_email@example.com**.

