import zmq
import cv2
import numpy as np

class FrameSubscriber:
    def __init__(self, addr):
        ctx = zmq.Context.instance()
        self.socket = ctx.socket(zmq.SUB)
        self.socket.connect(addr)
        self.socket.setsockopt(zmq.SUBSCRIBE, b"")

    def recv(self):
        return self.socket.recv()
    
    def recv_multipart(self):
        success = False

        _, t0_bytes, jpg = self.socket.recv_multipart()

        timestamp_ns = int.from_bytes(t0_bytes, "big")

        frame = cv2.imdecode(
            np.frombuffer(jpg, np.uint8),
            cv2.IMREAD_COLOR
        )
        success = True
        return success, timestamp_ns, frame
