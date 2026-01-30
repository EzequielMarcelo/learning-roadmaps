import cv2
import numpy as np

from libs.settings import ConsumerSettings
from libs.subscriber import FrameSubscriber

def main():
    isRunning = True
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

            cv2.imshow("Consumer", frame)

            if cv2.waitKey(1) == 27:  # ESC
                isRunning = False

    except KeyboardInterrupt:
        print("[CONSUMER] interrupted")

    finally:
        cv2.destroyAllWindows()
        print("[CONSUMER] stopped")

if __name__ == "__main__":
    main()
