# 🎞️ Video to JPG Frame Extractor

This module allows you to **convert a video into a sequence of JPG images**, frame by frame, with optional rotation. Ideal for preprocessing video data for machine learning, computer vision, or archival purposes.

---

## 📦 Description

The script uses **OpenCV** and **imutils** to:
- Read a video from a specified path
- Rotate each frame by -90° (optional preprocessing)
- Save each frame as a `.jpg` image
- Store all frames in a structured output directory

---

## 📁 Input & Output

### 🎥 Input
A video file, e.g., `vid-wheels.mp4`.

### 🖼️ Output
A folder named after the video (e.g., `vid-wheels/`) containing:
