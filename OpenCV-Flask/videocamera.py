import cv2
class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
		self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
	
	def __del__(self):
		self.video.release()
	
	def get_frame(self):
		ret, frame = self.video.read()
		ret, jpeg = cv2.imencode('.jpg',frame)
		return jpeg.tobytes()
