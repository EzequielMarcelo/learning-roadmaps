import zmq
import cv2

class FramePublisher:
    def __init__(self, addr):
        ctx = zmq.Context.instance()
        self.socket = ctx.socket(zmq.PUB)
        self.socket.bind(addr)

    def send(self, frame, quality):
        _, buf = cv2.imencode(
            ".jpg",
            frame,
            [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        )
        self.socket.send(buf.tobytes())
