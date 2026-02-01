import time
import cv2

from libs.state import CoreParams
from libs.settings import CoreSettings
from libs.publisher import FramePublisher

def main():
    isRunning = True
    params = CoreParams()
    timeLastFPS = time.monotonic()
    fps = 0
    frameCount = 0

    cap = cv2.VideoCapture(params.cameraIndex)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
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

            frameCount += 1

            elapsed = time.monotonic() - timeLastFPS
            if elapsed >= 1.0:
                fps = frameCount / elapsed
                frameCount = 0
                timeLastFPS = time.monotonic()

            text = f"Producer FPS: {fps:.2f}"
            cv2.putText(frame, text, (5, 50), 0, 0.7, (255, 0, 0), 2)
            
            t0 = time.time_ns()
            publisher.send(frame, t0, params.jpegQuality) 
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
