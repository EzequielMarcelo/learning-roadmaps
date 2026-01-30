import zmq

class FrameSubscriber:
    def __init__(self, addr):
        ctx = zmq.Context.instance()
        self.socket = ctx.socket(zmq.SUB)
        self.socket.connect(addr)
        self.socket.setsockopt(zmq.SUBSCRIBE, b"")

    def recv(self):
        return self.socket.recv()
