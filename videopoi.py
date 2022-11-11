import picamera
import time

camera.resolution = (640,480)
camera.start_recording('test_video.h264')
camera.wait_recording(100)
camera.stop_recording()
print('Finsihed")
