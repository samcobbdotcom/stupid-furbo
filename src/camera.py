import cv2
from src import objdetection
from src import utils
from src import pantilt
import threading
import time
import os

_lock = threading.Lock()

class Camera:
    def __init__(self, camID, model_path="models/efficientdet_lite0_edgetpu.tflite"):
        self._camera = cv2.VideoCapture(camID)
        self._camID = camID
        self._model_path = model_path
        self.object_detector = objdetection.ObjectDetection(True, self._model_path, num_threads=3)
        self.output_frame = None
        self._pan_tilt_ctrl = pantilt.PanTilt(0,1)

        self._row_size = 20  # pixels
        self._left_margin = 24  # pixels
        self._text_color = (0, 0, 255)  # red
        self._font_size = 1
        self._font_thickness = 1
        self._fps_avg_frame_count = 10

        self._counter = 0
        self._fps = 0
        self._start_time = time.time()
        time.sleep(2)


    def get_camera_indices(self):
        arr = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.read()[0]:
                if i != 2:
                    self._camera = cap
                    print("Found camera at {}".format(i))
                    return


    def get_frame(self):
        with _lock:
            return self.output_frame
    

    def ingest_frames(self):
        while True:
            if self._camera is None:
                continue
            self._counter += 1
            ret, frame = self._camera.read()
            if ret == False:
                continue
            detection_result = self.object_detector.detectObject(frame)
            frame = utils.visualize(frame, detection_result)
             # Calculate the FPS
            if self._counter % self._fps_avg_frame_count == 0:
                self._end_time = time.time()
                self._fps = self._fps_avg_frame_count / (self._end_time - self._start_time)
                self._start_time = time.time()

            # Show the FPS
            fps_text = 'FPS = {:.1f}'.format(self._fps)
            text_location = (self._left_margin, self._row_size)
            cv2.putText(frame, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    self._font_size, self._text_color, self._font_thickness)

            with _lock:
                self.output_frame = frame.copy()

    
    def pan_camera(self, direction):
        self._pan_tilt_ctrl.pan_single_step(direction)

    
    def tilt_camera(self, direction):
        self._pan_tilt_ctrl.tilt_single_step(direction)

    
    def reset_position(self):
        self._pan_tilt_ctrl.home_positions()
