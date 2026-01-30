import time
import cv2

from libs.state import CoreParams
from libs.settings import CoreSettings
from libs.publisher import FramePublisher

def main():
    isRunning = True
    params = CoreParams()

    cap = cv2.VideoCapture(params.cameraIndex)
    if not cap.isOpened():
        raise RuntimeError("Camera indisponivel.")

    publisher = FramePublisher(CoreSettings.FRAME_ADDR)

    time.sleep(0.5)

    print("[CORE] streaming iniciado.")

    try:
        while isRunning:
            ret, frame = cap.read()
            if not ret:
                continue

            publisher.send(frame, params.jpegQuality)
            cv2.imshow("Producer", frame)
            key = cv2.waitKey(max(1, int(1000 / params.fps)))
            
            # encerra o core
            if key == ord("q"):
                isRunning = False

    finally:
        cap.release()
        print("[CORE] stopped.")


if __name__ == "__main__":
    main()
