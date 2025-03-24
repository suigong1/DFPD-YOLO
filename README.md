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
   git clone https://github.com/suigong1/DFPD-YOLO.git
   cd DFPD-YOLO
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. The categorized kitti dataset is in the kitti-yolov5 folder, which contains the categorized train, val, and test folders.

## Usage
Modify `train.py` to set the training parameters before running:

```python
# Inside train.py
model = YOLO('ultralytics/cfg/models/v8/DFPD.yaml')
model.train(data=r'DFPD-YOLO\kitti.yaml',
EPOCHS = 200
BATCH_SIZE = 16
IMG_SIZE = 640
```)

Then execute:

```bash
python train.py
```


### Inference
Modify `test.py` to set evaluation parameters before running:

```python
# Inside test.py
model = YOLO('runs/name/weights/best.pt')
model.val(source='kitti-yolov5/test/images',
 imgsz=640,
project='runs/detect',
name='v8',
save=True,
```)

Then execute:

```bash
python val.py
```
### Evaluation

Modify `val.py` to set evaluation parameters before running:

```python
# Inside val.py
model = YOLO('runs/name/weights/best.pt')
model.predict(data=r'kitti-yolov5/val/images',
split='test',
imgsz=640,
batch=16,
```)

Then execute:

```bash
python val.py
```
## Key Code Files

The key components of DFPD-YOLO, including the Dynamic Task-aligned Detection Head (DTDH), FocusFeature, feature diffusion mechanism, and task decomposition, are implemented in the following files:

- **DTDH.py**: Contains the implementation of the Dynamic Task-aligned Detection Head.
- **FocusFeature.py**: Implements the FocusFeature and feature diffusion mechanism in the Neck section, improving multi-scale feature context-awareness.
- **TaskDecomposition.py**: Implements task decomposition for better separation and alignment of the classification and localization tasks, enhancing the overall model performance.

These files contain the core functionality of the model and can be modified for further improvements or experiments.

## Experimental Results
Our experiments on the KITTI dataset show that **DFPD-YOLO significantly improves detection accuracy**, especially for **small and occluded objects**. The proposed enhancements lead to better feature representation, faster convergence, and improved localization precision.
![fig11](https://github.com/user-attachments/assets/272c5f55-5a38-42b2-905a-714af745b365)




## Contact
For any inquiries, please contact **lzf18874212199@gmail.com**.

