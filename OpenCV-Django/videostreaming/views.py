from django.shortcuts import render
import cv2
import threading
import gzip
from django.views.decorators.gzip import gzip_page
from django.http import StreamingHttpResponse

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		
		self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
		self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
		
		(self.grabbed, self.frame) = self.video.read()
		threading.Thread(target=self.update, args=()).start()
	
	def __del__(self):
		self.video.release()
		
	def get_frame(self):
		image = self.frame 
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()
	
	def update(self):
		while True:
			(self.grabbed, self.frame) = self.video.read()

cam = VideoCamera()

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield(b'--frame\r\n'b'Content-type: image\jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip_page
def live(request):
	try:
		return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
	except Exception as e: print(e)

def index(request):
	return render(request, 'videostreaming/index.html', {})
