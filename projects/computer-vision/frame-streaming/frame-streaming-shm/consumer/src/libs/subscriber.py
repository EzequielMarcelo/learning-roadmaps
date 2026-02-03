import numpy as np
from multiprocessing import shared_memory, Semaphore
from libs.settings import SubscriberSettings

class FrameSubscriber:
    def __init__(self):
        settings = SubscriberSettings()
        self.shm = shared_memory.SharedMemory(name=settings.SHM_NAME)
        self.sem = Semaphore(1)
        self.current_frame_id = -1

        self.header = np.ndarray(
            shape=(1,),
            dtype=settings.HEADER_DTYPE,
            buffer=self.shm.buf[:settings.HEADER_DTYPE.itemsize]
        )

        self.frame = np.ndarray(
            (settings.FRAME_HEIGHT, settings.FRAME_WIDTH, settings.CHANNELS),
            dtype=settings.FRAME_DTYPE,
            buffer=self.shm.buf[settings.HEADER_DTYPE.itemsize:]
        )

    def recv_multipart(self) -> tuple[bool, int, np.ndarray]:
        self.sem.acquire()
        success = False
        try:
            frame = self.frame.copy()
            timestamp_ns = int(self.header["timestamp_ns"][0])
            frame_id = int(self.header["frame_id"][0])
            success = self.current_frame_id != frame_id
            self.current_frame_id = frame_id
        finally:
            self.sem.release()

        return success, timestamp_ns, frame

    def close(self):
        self.shm.close()
