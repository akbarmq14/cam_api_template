import os
import logging
import json


# Need to add logger for camera api template

class CameraApiTemplate:
    """
    This is a boilerplate code for any camera api.
    """
    PixelFormats = ["mono", "rgb", "bgr", "hsv"]

    @staticmethod
    def detect_connected_devices():
        devices = None
        """
        Detect the appropriate connected devices/cameras
        :return: list with camera names
        """
        try:
            '''
            Add your code here
            '''
            return devices
        except Exception as error:
            '''
            Add your code here
            '''
            return devices

    def __init__(self, name="camera"):
        """
        Initialise the camera
        :param name: Input a name for the camera object, or leave it as default name
        :type name: str
        """
        assert (type(name) == str), "[ERROR] Input name is not a string"

        self._name = name
        self._acquisition_mode = None
        self._acquisition_method = None
        self._exposure = None
        self._frame_rate_limit = None
        self._frame_timeout = None
        self._buffer_size = None
        self._gain = None
        self._gamma = None
        self._pixel_format = None
        self._logger = None
        self._resolution_width = None
        self._resolution_height = None
        self._ROI_x0 = None
        self._ROI_y0 = None
        self._ROI_x1 = None
        self._ROI_y1 = None
        self._auto_exposure_flag = False
        self._auto_gain_flag = False
        '''
        Any additional initializations?
        '''

    @property
    def name(self):
        """
        Retrieve the name of the camera
        :return: str
        """
        return self._name

    def set_name(self, name):
        """
        Change the name of the camera
        :param name: Input a name for the camera object
        :return: True if successful, else false
        """
        try:
            assert (type(name) == str), "[ERROR] Input name is not a string"
            self._name = name
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def acquisition_mode(self):
        """
        Retrieve the acquisition mode of the camera - Single, Multiple and Continous mode
        :return: str
        """
        return self._acquisition_mode

    def set_acquisition_mode(self, mode):
        """
        Change the acquisition mode of the camera
        :param mode: Input the camera acquisition mode - Single, Multiple or Continous mode
        :return: True if successful, else false
        """
        try:
            assert (type(mode) == str), "[ERROR] Input mode is not a string"
            self._acquisition_mode = mode
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def acquisition_method(self):
        """
        Retrieve the acquisition method - Software, Hardware and No trigger
        :return: str
        """
        return self._acquisition_method

    def set_acquisition_method(self, method):
        """
        Change the acquisition method of the camera
        :param mode: Input the camera acquisition method - Software, Hardware or No trigger
        :return: True if successful, else false
        """
        try:
            assert (type(method) == str), "[ERROR] Input method is not a string"
            self._acquisition_method = method
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def exposure(self):
        """
        Retrieve the exposure of camera
        :return: float
        """
        return self._exposure

    def set_exposure(self, exposure):
        """
        Change the exposure of the camera
        :param exposure: Input exposure of the camera in float value
        :return: True if successful, else false
        """
        try:
            assert (type(exposure) == float), "[ERROR] Input exposure is not float"
            self._exposure = exposure
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def frame_rate_limit(self):
        """
        Retrieve the frame rate limit of the camera
        :return: float
        """
        return self._frame_rate_limit

    def set_frame_rate_limit(self, limit):
        """
        Provide a limit for camera frame rate, if applicable
        :param limit: Input framerate limit of the camera in float value
        :return: True if successful, else false
        """
        try:
            assert (type(limit) == float), "[ERROR] Input frame rate limit is not float"
            self._frame_rate_limit = limit
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def buffer_count(self):
        """
        Retrieve the buffer count of the camera
        :return: int
        """
        return self._buffer_size

    def set_buffer_count(self, count):
        """
        Provide a buffer count for camera, if applicable
        :param size: Input buffer count of the camera in int value
        :return: True if successful, else false
        """
        try:
            assert (type(count) == int), "[ERROR] Input count is not int"
            self._buffer_count = count
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def frame_timeout(self):
        """
        Retrieve the frame timeout of the camera
        :return: float
        """
        return self._frame_timeout

    def set_frame_timeout(self, timeout):
        """
        Provide a timeout for frame capture
        :param timeout: Input frame timeout in seconds
        :return: True if successful, else false
        """
        try:
            assert (type(timeout) == float), "[ERROR] Input frame rate timeout is not float"
            self._frame_timeout = timeout
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def gain(self):
        """
        Retrieve the gain of the camera
        :return: float
        """
        return self._gain

    def set_gain(self, gain):
        """
        Provide gain value for the camera
        :param gain: Input gain in float
        :return: True if successful, else false
        """
        try:
            assert (type(gain) == float), "[ERROR] Input gain is not float"
            self._gain = gain
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def pixel_format(self):
        """
        Retrieve the pixel format of the camera
        :return: str
        """
        return self._pixel_format

    def get_supported_pixel_formats(self):
        pixel_formats = None
        """
        Retrieve supported pixel formats from the camera
        :return: list of pixel formats
        """
        '''
        Add your code here
        '''
        return pixel_formats

    def set_pixel_format(self, pixel_format):
        """
        Provide a pixel format for the camera
        :param format: Input pixel format in string - mono, rgb, bgr or hsv
        :return: True if successful, else False
        """
        try:
            assert (type(pixel_format) == str), "[ERROR] Input format is not string"
            self._pixel_format = pixel_format
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def resolution(self):
        """
        Retrieve the resolution of the camera
        :return: list of two int's (width, height)
        """
        return self._resolution_width, self._resolution_height

    def set_resolution(self, width, height):
        """
        Provide frame resolution for the camera
        :param width: Input camera width resolution
        :param height: Input camera height resolution
        :return: True if successful, else False
        """
        try:
            assert (type(width) == int and type(height) == int), "[ERROR] Input resolution is not integer"
            self._resolution_width = width
            self._resolution_height = height
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def ROI(self):
        """
        Retrieve the region of interest of the camera
        :return: list of four int's (x0, x1, y0, y1)
        """
        return self._ROI_x0, self._ROI_x1, self._ROI_y0, self._ROI_y1

    def set_ROI(self, x0, y0, x1, y1):
        """
        Provide a region of interest for the camera
        :param x0: Input x-axis start point
        :param y0: Input y-axis start point
        :param x1: Input x-axis end point
        :param y1: Input y-axis end point
        :return: True if successful, else False
        """
        try:
            assert (type(x0) == int and type(y0) == int and type(x1) == int and type(
                y1) == int), "[ERROR] Input ROI is not integer"
            self._ROI_x0 = x0
            self._ROI_x1 = x1
            self._ROI_y0 = y0
            self._ROI_y1 = y1
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def auto_gain(self):
        """
        Retrieve the flag for auto gain
        :return: bool
        """
        return self._auto_gain_flag

    def set_auto_gain(self, flag):
        """
        Enable or disable auto gain of the camera
        :param flag: Input True to enable or False to disable
        :return: True if successful, else False
        """
        try:
            assert (type(flag) == bool), "[ERROR] Input flag is not boolean"
            self._auto_gain_flag = flag
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    @property
    def auto_exposure(self):
        """
        Retrieve the flag for auto exposure
        :return: bool
        """
        return self._auto_gain_flag

    def set_auto_exposure(self, flag):
        """
        Enable or disable auto exposure of the camera
        :param flag: Input True to enable or False to disable
        :return: True if successful, else False
        """
        try:
            assert (type(flag) == bool), "[ERROR] Input flag is not boolean"
            self._auto_exposure_flag = flag
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    def initiate_logger(self, logger):
        '''
        Add your code here
        '''
        pass

    def set_logger_level(self, logger_level):
        """
        Set the logger level of this camera
        :param logger_level: input logger level
        :return: True if successful, else False
        """
        try:
            assert (type(logger_level) == int), "[ERROR] Input logger level is not valid"
            '''
            Add your code here
            '''
            return True

        except AssertionError as error:
            '''
            Add your code here
            '''
            return False

    def connect(self):
        """
        Establish connection to the camera
        :return: True if successful, else False
        """
        try:
            '''
            Add your code here
            '''
            return True

        except Exception as error:
            '''
            Add your code here
            '''
            return False

    def disconnect(self):
        """
        Disconnect from the camera
        :return: True if successful, else False
        """
        try:
            '''
            Add your code here
            '''
            return True

        except Exception as error:
            '''
            Add your code here
            '''
            return False

    def capture_raw(self):
        """
        Retrieve a raw / unaltered frame from the camera
        :return: this is camera specific
        """
        frame_raw = None
        try:
            '''
            Add your code here
            '''
            return frame_raw

        except Exception as error:
            '''
            Add your code here
            '''
            return frame_raw

    def capture_numpy(self):
        """
        Retrieve a numpy frame from the camera
        :return: this is camera specific
        """
        frame = None
        try:
            '''
            Add your code here
            '''
            return frame

        except Exception as error:
            '''
            Add your code here
            '''
            return frame

    def load_parameters_from_json(self, file_path):
        """
        Load camera parameters from a json file
        Sample JSON Schema for camera settings
        {
            "version": 0.1,
            "name": "Basler",
            "acquisition_mode": "single",
            "acquisition_method": "software",
            "exposure": 8000.0,
            "frame_rate": 25.0,
            "frame_timeout": 0.1,
            "buffer_count": 5,
            "pixel_format": "mono",
            "gain": 1.0,
            "gamma": 0.634,
            "auto_exposure": false,
            "auto_gain": false,
            "resolution": {
                            "width": 1920,
                            "height": 1080
                           },
            "ROI": {
                     "x0": 0,
                     "y0": 0,
                     "x1": 1920,
                     "y1": 1080
                    }
        }
        :param file_path: Input the path of the json file in string
        :return: True if successful, else False
        """
        try:
            with open(file_path) as json_file:
                parameters = json.load(json_file)
                status = self.validate_json(parameters)
                if status:
                    '''
                    Add your code here
                    '''
                else:
                    raise Exception
            return True

        except Exception as error:
            '''
            Add your code here
            '''
            return False

    def validate_json(self, parameters):
        """
        Validate the schema of the json file
        :param parameters: path of the json file
        :return: True if successful, else False
        """
        try:
            '''
            Add your code here
            '''
            return True

        except Exception as error:
            '''
            Add your code here
            '''
            return False

    def save_parameters_to_json(self, json_file):
        """
        Store all the camera settings to a json file
        :param json_file: path to the json file
        :return: True if successful, else False
        """
        try:
            '''
            Add your code here
            '''
            return True

        except Exception as error:
            '''
            Add your code here
            '''
            return False

    def initialize_camera(self):
        """
        Initialise the camera
        :return: True if successful, else False
        """
        try:
            '''
            Add your code here
            '''
            return True

        except Exception as error:
            '''
            Add your code here
            '''
            return False

