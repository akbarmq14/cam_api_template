import unittest
import Camera_Api as cam_api 


class Test(unittest.TestCase):
	print("***camera_api_TEST***")
	api_class = cam_api.CameraApiTemplate('Basler')


	def test_name(self):
		print("property name and set name \n")
		print("Default name :", self.api_class.name)
		self.api_class.set_name("Web-cam")		
		print("New camera name: ", self.api_class.name)
		print("\n")

	def test_set_acquisition_mode(self):
		print("property set_acquisition_mode \n")
		# self.api_class.initialize_camera()
		print("Default acquisition mode :", self.api_class.acquisition_mode)
		self.api_class.set_acquisition_mode("SingleFrame")		
		print("New acquisition mode: ", self.api_class.acquisition_mode)
		print("\n")

	def test_acquisition_method(self):
		print("property set_acquisition_method \n")
		# self.api_class.initialize_camera()
		print("Default acquisition method :", self.api_class.acquisition_method)
		self.api_class.set_acquisition_method("Software")		
		print("New acquisition method: ", self.api_class.acquisition_method)
		print("\n")


	def test_exposure(self):
		print("property of Exposure \n")
		# self.api_class.initialize_camera()
		print("Default Exposure :", self.api_class.exposure)
		self.api_class.set_exposure(0.5)		
		print("New Exposure: ", self.api_class.exposure)
		print("\n")

	def test_frame_rate_limit(self):
		print("property of frame_rate_limit \n")
		# self.api_class.initialize_camera()
		print("Default frame_rate_limit :", self.api_class.frame_rate_limit)
		self.api_class.set_frame_rate_limit(0.5)		
		print("New frame_rate_limit: ", self.api_class.frame_rate_limit)
		print("\n")

	def test_buffer_count(self):
		print("property of buffer_count \n")
		# self.api_class.initialize_camera()
		print("Default buffer_count:", self.api_class.buffer_count)
		self.api_class.set_buffer_count(10)		
		print("New buffer_count: ", self.api_class.buffer_count)
		print("\n")

	def test_frame_timeout(self):
		print("property of frame_timeout \n")
		# self.api_class.initialize_camera()
		print("Default frame_timeout:", self.api_class.frame_timeout)
		self.api_class.set_frame_timeout(15.5)		
		print("New frame_timeout: ", self.api_class.frame_timeout)
		print("\n")

	def test_gain(self):
		print("property of gain \n")
		# self.api_class.initialize_camera()
		print("Default gain:", self.api_class.gain)
		self.api_class.set_gain(10.5)		
		print("New gain: ", self.api_class.gain)
		print("\n")

	def test_pixel_format(self):
		print("property of pixel_format \n")
		# self.api_class.initialize_camera()
		print("Default pixel_format:", self.api_class.pixel_format)
		self.api_class.set_pixel_format("PIXEL_FORMAT")		
		print("New pixel_format: ", self.api_class.pixel_format)
		print("\n")

	def test_resolution(self):
		print("property of resolution \n")
		# self.api_class.initialize_camera()
		print("Default camera resolution:", self.api_class.resolution)
		self.api_class.set_resolution(400, 500)		
		print("New camera_size resolution: ", self.api_class.resolution)
		print("\n")

	def test_auto_gain(self):
		print("property of auto_gain \n")
		# self.api_class.initialize_camera()
		print("Default auto_gain:", self.api_class.auto_gain)
		self.api_class.set_auto_gain("Once")		
		print("New auto_gain: ", self.api_class.auto_gain)
		print("\n")

	def test_auto_exposure(self):
		print("property of auto_exposure \n")
		# self.api_class.initialize_camera()
		print("Default auto_exposure:", self.api_class.auto_exposure)
		self.api_class.set_auto_exposure("Once")		
		print("New auto_exposure: ", self.api_class.auto_exposure)
		print("\n")



if __name__ =='__main__':
	unittest.main()

# setters are all functions 
