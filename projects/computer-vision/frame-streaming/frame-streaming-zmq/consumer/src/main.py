import cv2
import numpy as np
import time

from libs.settings import ConsumerSettings
from libs.subscriber import FrameSubscriber

def main():
    isRunning = True
    timeLastFPS = time.monotonic()
    fps = 0
    frameCount = 0
    sub = FrameSubscriber(ConsumerSettings.FRAME_ADDR)

    print("[CONSUMER] waiting for frames...")

    try:
        while isRunning:
            data = sub.recv()

            frame = cv2.imdecode(
                np.frombuffer(data, np.uint8),
                cv2.IMREAD_COLOR
            )

            if frame is None:
                continue

            frameCount += 1
            
            elapsed = time.monotonic() - timeLastFPS
            if elapsed >= 1.0:
                fps = frameCount / elapsed
                frameCount = 0
                timeLastFPS = time.monotonic()
            
            text = f"Consumer FPS: {fps:.2f}"
            cv2.putText(frame, text, (5, 70), 0, 0.7, (0, 255, 0), 2)

            cv2.imshow("Consumer", frame)

            # encerra o programa
            if cv2.waitKey(1) == ord("q"):
                isRunning = False

    except KeyboardInterrupt:
        print("[CONSUMER] interrupted")

    finally:
        cv2.destroyAllWindows()
        print("[CONSUMER] stopped")

if __name__ == "__main__":
    main()
