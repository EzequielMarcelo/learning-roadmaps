import zmq
import cv2
import numpy as np

class FramePublisher:
    def __init__(self, addr):
        ctx = zmq.Context.instance()
        self.socket: zmq.Socket = ctx.socket(zmq.PUB)
        self.socket.bind(addr)

    def send(self, frame: np.ndarray, time: int, quality: int):
        _, buf = cv2.imencode(
            ".jpg",
            frame,
            [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        )
        self.socket.send_multipart([
            b"frame",
            time.to_bytes(8, "big"),
            buf.tobytes()
            ])
