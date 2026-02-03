import numpy as np
from multiprocessing import shared_memory, Semaphore
from libs.settings import PublisherSettings

class FramePublisher:
    def __init__(self):
        settings = PublisherSettings()
        self.frame_bytes = settings.FRAME_HEIGHT * settings.FRAME_WIDTH * settings.CHANNELS
        self.total_size = settings.HEADER_DTYPE.itemsize + self.frame_bytes

        self.shm = shared_memory.SharedMemory(
            name=settings.SHM_NAME,
            create=True,
            size=self.total_size
        )

        self.sem = Semaphore(1)

        # HEADER
        self.header = np.ndarray(
            shape=(1,),
            dtype=settings.HEADER_DTYPE,
            buffer=self.shm.buf[:settings.HEADER_DTYPE.itemsize]
        )

        # FRAME
        self.frame = np.ndarray(
            (settings.FRAME_HEIGHT, settings.FRAME_WIDTH, settings.CHANNELS),
            dtype=settings.FRAME_DTYPE,
            buffer=self.shm.buf[settings.HEADER_DTYPE.itemsize:]
        )

        self.frame_id = 0
        print("[SHM] FramePublisher inicializado.")

    def send(self, frame: np.ndarray, timestamp_ns: int):
        self.sem.acquire()
        try:
            self.header["timestamp_ns"][0] = timestamp_ns
            self.header["frame_id"][0] = self.frame_id

            self.frame[:] = frame
            self.frame_id += 1
        finally:
            self.sem.release()

    def close(self):
        self.shm.close()
        self.shm.unlink()
