import numpy as np

class PublisherSettings:
    FRAME_HEIGHT = 720
    FRAME_WIDTH = 1280
    CHANNELS = 3

    FRAME_DTYPE = np.uint8
    HEADER_DTYPE = np.dtype([
        ("timestamp_ns", np.uint64),
        ("frame_id", np.uint32),
    ])

    SHM_NAME = "core_webcam_frame"

