import pi_servo_hat
import numpy as np

_MIN_CHANNEL = 0
_MAX_CHANNEL = 15
_MIN_DEG = 0
_MAX_DEG = 180
_PAN_HOME = 0.0
_TILT_HOME = 45.0
_SINGLE_MOVE_DEGS = 1.0

class PanTilt:
    def __init__(self, p_channel, t_channel):
        self.sensor = pi_servo_hat.PiServoHat()
        self.pan_deg = _PAN_HOME
        self.tilt_deg = _TILT_HOME

        self._p_channel = p_channel
        self._t_channel = t_channel

        if self._p_channel not in range(_MIN_CHANNEL, _MAX_CHANNEL):
            self._p_channel = 0 # default pan channel
        if self._t_channel not in range(_MIN_CHANNEL, _MAX_CHANNEL):
            self._t_channel = 1 # default tilt channel
        self.sensor.restart()
        self.home_positions()

    
    def get_pan_degrees(self):
        return self.pan_deg
    

    def get_tilt_degrees(self):
        return self.tilt_deg

    
    def home_positions(self):
        self.sensor.move_servo_position(self._p_channel, _PAN_HOME)
        self.sensor.move_servo_position(self._t_channel, _TILT_HOME)
        self._pan_deg = _PAN_HOME
        self._tilt_deg = _TILT_HOME

    
    def pan_single_step(self, direction):
        if direction > 0: 
            self.pan_deg += _SINGLE_MOVE_DEGS
        else:
            self.pan_deg -= _SINGLE_MOVE_DEGS
        
        self.pan_deg = np.clip(_MIN_DEG, self.pan_deg, _MAX_DEG)
        self.sensor.move_servo_position(self._p_channel, self.pan_deg)


    def tilt_single_step(self, direction):
        if direction > 0: 
            self.tilt_deg += _SINGLE_MOVE_DEGS / 2.0
        else:
            self.tilt_deg -= _SINGLE_MOVE_DEGS / 2.0
            
        self.tilt_deg = np.clip(_MIN_DEG, self.tilt_deg, _MAX_DEG)
        self.sensor.move_servo_position(self._t_channel, self.tilt_deg)
