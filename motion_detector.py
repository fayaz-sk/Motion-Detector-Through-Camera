import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# Open Webcam
cap = cv2.VideoCapture(0)

previous_landmarks = None


# Function to detect posture
def detect_posture(landmarks, image_height):
    left_hip = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
    left_knee = landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
    right_knee = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]

    left_hip_y = left_hip.y * image_height
    right_hip_y = right_hip.y * image_height
    left_knee_y = left_knee.y * image_height
    right_knee_y = right_knee.y * image_height

    hip_avg_y = (left_hip_y + right_hip_y) / 2
    knee_avg_y = (left_knee_y + right_knee_y) / 2

    hip_knee_diff = hip_avg_y - knee_avg_y

    if hip_knee_diff < 30:
        return "Standing"
    elif hip_avg_y > image_height * 0.6:
        return "Sitting"
    else:
        return "Unknown"


# Function to detect motion
def detect_motion(current_landmarks, previous_landmarks, image_height):
    if previous_landmarks is None:
        return "Standing"

    left_ankle_current = current_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
    right_ankle_current = current_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]

    left_ankle_prev = previous_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
    right_ankle_prev = previous_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]

    displacement = (
        abs(left_ankle_current.y - left_ankle_prev.y) +
        abs(right_ankle_current.y - right_ankle_prev.y)
    ) * image_height

    if displacement > 50:
        return "Running"
    elif displacement > 10:
        return "Walking"
    else:
        return "Standing"


# Pose Detection
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.7
) as pose:

    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            print("Failed to read frame.")
            break

        frame.flags.writeable = False
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        frame.flags.writeable = True
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            image_height, image_width, _ = frame.shape

            posture = detect_posture(results.pose_landmarks, image_height)
            motion = detect_motion(
                results.pose_landmarks,
                previous_landmarks,
                image_height
            )

            previous_landmarks = results.pose_landmarks

            text = f"{motion} - {posture}"

            cv2.putText(
                frame,
                text,
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )

        cv2.imshow("Pose Detection", cv2.flip(frame, 1))

        if cv2.waitKey(5) & 0xFF == 27:  # Press ESC to exit
            break

cap.release()
cv2.destroyAllWindows()
