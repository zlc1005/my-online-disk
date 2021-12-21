from PIL import ImageGrab
import cv2, mediapipe as mp, tkinter, pyautogui, time
win = tkinter.Tk()
win.withdraw()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
def get_screen(width,height,name):
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img.save(name)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
def process_frame(file):
    nosepos = None
    with mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5) as pose:
        for _ in [1]:
            image = cv2.imread(file)
            image_height, image_width, _ = image.shape
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if not results.pose_landmarks:
                continue
            print(
                f'Nose coordinates: ('
                f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
                f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
            )
            nosepos = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width,results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height)
            annotated_image = image.copy()
            mp_drawing.draw_landmarks(
                annotated_image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            cv2.imwrite('d:/aa.png', annotated_image)
            # mp_drawing.plot_landmarks(
            #     results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
    return nosepos
def press_space():
    pyautogui.press('space')

def main():
    while True:#for i in range(10):
        get_screen(width,height,'d:/a.png')
        nosepos = process_frame('d:/a.png')
        if nosepos != None:
            pyautogui.moveTo(nosepos[0],nosepos[1])
            press_space()
        time.sleep(2)

if __name__ == '__main__':
    main()































'''
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # results = pose.process(image)
    # Draw the pose annotation on the image.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # try:
    #     image_height, image_width, _ = image.shape
    #     nosepos=(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width,results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height)
    #     # Draw the pose keypoints onto the image.
    #     cv2.circle(image, (int(nosepos[0]), int(nosepos[1])), 20, (0, 0, 255), -1)
    #     print(nosepos)
    # except Exception as e:
    #     if e == "'NoneType' object has no attribute 'landmark'" or e == "'NoneType' object has no attribute 'landmark'":   # 如果没有检测到人脸，则不画红点
    #         print("No pose detected.")
    #     else:
    #         print(e)
    # finally:
    #     pass
    # print nose position
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0x0000FF == 27:
      break
cap.release()
'''