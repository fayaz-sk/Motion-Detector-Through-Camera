# Motion Detector Through Camera

## 📌 Project Overview

The **Motion Detector Through Camera** project is a real-time computer vision application developed using **Python**, **OpenCV**, and **MediaPipe Pose Estimation**. The system captures live video from a webcam, detects the human body pose, analyzes body landmarks, and identifies both **human posture** and **movement**.

This project demonstrates how Artificial Intelligence and Computer Vision techniques can be used to recognize basic human activities such as **Standing**, **Sitting**, **Walking**, and **Running** in real time without requiring any wearable sensors.

---

# 🎯 Aim

To develop a real-time motion detection system using a webcam that can identify human posture and movement through pose estimation.

---

# 📖 Introduction

Human motion detection has become an important application in many fields including healthcare, surveillance, fitness tracking, sports analytics, robotics, and smart homes.

Traditional motion detection techniques rely on image subtraction or optical flow, whereas modern AI-based techniques use body landmark estimation for more accurate results.

This project utilizes **MediaPipe Pose**, a machine learning framework developed by Google, to detect 33 body landmarks from live webcam footage. Based on these landmarks, the program determines whether the user is standing, sitting, walking, or running.

---

# 🎯 Objectives

- Detect a person's body using a webcam.
- Identify body posture.
- Detect movement in real time.
- Display the detected activity on the screen.
- Learn the fundamentals of Computer Vision using Python.

---

# ✨ Features

- ✅ Real-time webcam processing
- ✅ Human pose estimation
- ✅ Standing detection
- ✅ Sitting detection
- ✅ Walking detection
- ✅ Running detection
- ✅ Live body landmark visualization
- ✅ Lightweight and easy to run
- ✅ No external sensors required

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Human pose estimation |
| NumPy | Mathematical calculations |

---

# 📂 Project Structure

```
Motion-Detector-Through-Camera/
│
├── motion_detector.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── images/
│   ├── output1.png
│   ├── output2.png
│   └── output3.png
└── output/
```

---

# ⚙ Requirements

- Python 3.10 or above
- Webcam
- Windows/Linux/macOS

---

# 📦 Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/fayaz-sk/Motion-Detector-Through-Camera.git
```

## Step 2

Move into the project folder

```bash
cd Motion-Detector-Through-Camera
```

## Step 3

Install required libraries

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Execute the following command:

```bash
python motion_detector.py
```

The webcam will automatically open.

Press **ESC** to close the application.

---

# 🔍 Working Principle

1. OpenCV captures frames from the webcam.
2. Each frame is converted from BGR to RGB.
3. MediaPipe Pose detects body landmarks.
4. Hip and knee positions are analyzed to detect posture.
5. Ankle movement between consecutive frames is calculated.
6. Based on displacement:
   - Standing
   - Sitting
   - Walking
   - Running
7. The detected activity is displayed on the webcam screen.

---

# 🧠 Algorithm

1. Start webcam.
2. Read video frame.
3. Detect body landmarks.
4. Calculate hip and knee positions.
5. Determine posture.
6. Compare ankle positions with previous frame.
7. Detect movement.
8. Display motion and posture.
9. Repeat until ESC key is pressed.

---

# 📸 Output

The application displays:

- 🧍 Standing
- 🪑 Sitting
- 🚶 Walking
- 🏃 Running

along with the detected body skeleton in real time.

---

# 💡 Applications

- Smart Surveillance Systems
- Healthcare Monitoring
- Fitness Tracking
- Human Activity Recognition
- Sports Analytics
- Smart Homes
- Elderly Care
- Robotics
- Gesture Recognition
- Security Systems

---

# 🚀 Future Scope

This project can be extended by adding:

- Fall Detection
- Exercise Recognition
- Yoga Pose Detection
- Dance Movement Recognition
- Multiple Person Tracking
- AI-based Action Recognition
- Attendance Monitoring
- Gesture Control
- Face Recognition Integration
- CCTV Surveillance

---

# ✅ Advantages

- Real-time processing
- Easy to use
- Fast detection
- Accurate pose estimation
- Open-source technologies
- Lightweight implementation
- Cross-platform compatibility

---

# ⚠ Limitations

- Requires good lighting.
- Accuracy decreases with heavy occlusion.
- Supports only basic motion classification.
- Performance depends on webcam quality.

---

# 📚 Libraries Used

```
opencv-python
mediapipe
numpy
```

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Shaik Fayaz**

B.Tech – Computer Science and Engineering

VIT-AP University

---

# ⭐ If you like this project
