import src.camera as cam
import src.webstreaming as web
import src.controller as controller

if __name__ == "__main__":
    camera = cam.Camera(4, model_path="models/efficientdet_lite0_edgetpu.tflite")
    controller = controller.Controller(camera)
    controller.start()
    web.start(camera=camera, address="10.0.0.18", port=5000)
