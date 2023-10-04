# Video Color Grading with Python

This Python script allows you to apply color grading effects to a video using the `moviepy` and `OpenCV` libraries. You can adjust the brightness, contrast, and saturation of the video to achieve the desired visual effect.

---

## Prerequisites

Before you can use this script, make sure you have the following libraries installed:

- `moviepy`: Install it using `pip install moviepy`.
- `OpenCV` (cv2): Install it using `pip install opencv-python`.
- `numpy`: Install it using `pip install numpy`.

## Usage

1. Clone this repository or download the script.
2. Place your input video file (e.g., `videoplayback.mp4`) in the same directory as the script.
3. Adjust the color grading factors (`brightness_factor`, `contrast_factor`, and `saturation_factor`) according to your preferences.

```python
brightness_factor = 1.5  # Adjust as needed
contrast_factor = 1.5    # Adjust as needed
saturation_factor = 1.5  # Adjust as needed
```

Run the script. It will process the video, apply the color grading effects, and save the graded video as output_video.mp4 in the same directory.

## Example
```bash
python color_grading.py
```

