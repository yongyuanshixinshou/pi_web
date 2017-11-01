from flask import Response, render_template

# from .camera_test import Camera
from .camera_pi import Camera
# from .camera_opencv import Camera

from app.camera import camera


@camera.route('/camera/')
def index():
    return render_template("camera/index.html")


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@camera.route('/camera/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
