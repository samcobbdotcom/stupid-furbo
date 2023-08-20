from flask import Response
from flask import Flask
from flask import Request
from flask import render_template
from src import camera
import threading
import time
import cv2

_DEFAULT_ADDR = "10.0.0.18"
_DEFAULT_PORT = 5000

app = Flask(__name__)
_camera = None
_camera_thread = None
    
def start(camera, address=_DEFAULT_ADDR, port=_DEFAULT_PORT):
    global _camera, _camera_thread
    _camera = camera
    _camera_thread = threading.Thread(target=_camera.ingest_frames)
    _camera_thread.daemon = True
    _camera_thread.start()

    time.sleep(2)

    app.run(host=address, port=port, debug=True,
    threaded=True, use_reloader=False)


def stop():
    _camera_thread.join()
    func = Request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")


def generate():
    global _camera
    while True:
        if _camera is None:
            continue
        _out_frame = _camera.get_frame()
        if _out_frame is None:
            continue

        (flag, encoded_img) = cv2.imencode(".jpg", _out_frame)
        if not flag:
            print("bad flag detected!")
            continue

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_img) + b'\r\n')
