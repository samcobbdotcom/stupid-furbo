from src import camera
import pygame
import threading

_PAN_UP = 0
_PAN_DOWN = 1
_TILT_UP = 1
_TILT_DOWN = 0

_JS_LEFT_RIGHT = 0
_JS_UP_DOWN = 1
_JS_THRESH = 0.01

class Controller:
    def __init__(self, camera: camera):
        pygame.init()
        self._joystick = pygame.joystick.Joystick(0)
        self._joystick.init()
        print(pygame.joystick.get_count())
        self._clock = pygame.time.Clock()
        self._should_run = False
        self._camera = camera
        self._thread = None

    
    def start(self):
        self._should_run = True
        if self._thread == None:
            self._thread = threading.Thread(target=self.poll)
            self._thread.start()
        else:
            self._thread.start()

    
    def stop(self):
        self._should_run = False
        if self._thread != None:
            self._thread.join()


    def pan(self, direction):
        self._camera.pan_camera(direction)


    def tilt(self, direction):
        self._camera.tilt_camera(direction)


    def poll(self):
        running = True
        while(self._should_run & running):
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    lat = self._joystick.get_axis(_JS_LEFT_RIGHT)
                    vert = self._joystick.get_axis(_JS_UP_DOWN)

                    while (lat < 0 or lat > _JS_THRESH):
                        self.pan(-lat)
                        pygame.event.get()
                        lat = self._joystick.get_axis(_JS_LEFT_RIGHT)
                    
                    while (vert < 0 or vert > _JS_THRESH):
                        self.tilt(-vert)
                        pygame.event.get()
                        vert = self._joystick.get_axis(_JS_UP_DOWN)

                elif event.type == pygame.JOYBUTTONDOWN:
                    self._camera.reset_position()



