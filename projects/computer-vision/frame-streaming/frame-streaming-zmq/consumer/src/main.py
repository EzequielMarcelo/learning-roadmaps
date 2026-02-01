import cv2
import numpy as np
import time
from collections import deque

from libs.settings import ConsumerSettings
from libs.subscriber import FrameSubscriber

def main():
    isRunning = True
    timeLastFPS = time.monotonic()
    fps = 0
    frameCount = 0
    sub = FrameSubscriber(ConsumerSettings.FRAME_ADDR)
    latencyQueue = deque(maxlen=100)
    textColor = (0, 0, 255)

    print("[CONSUMER] waiting for frames...")

    try:
        while isRunning:
            _, t0, frame = sub.recv_multipart()

            t1 = time.time_ns()

            latency_ms = (t1 - t0) / 1e6
            latencyQueue.append(latency_ms)
            latency_ms_avg = np.mean(latencyQueue)


            if frame is None:
                continue

            frameCount += 1
            
            elapsed = time.monotonic() - timeLastFPS
            if elapsed >= 1.0:
                fps = frameCount / elapsed
                frameCount = 0
                timeLastFPS = time.monotonic()
            
            text = f"Consumer FPS: {fps:.2f}"
            cv2.putText(frame, text, (5, 70), 0, 0.7, textColor, 2)

            text = f"Latency: {latency_ms_avg:.2f} ms"
            cv2.putText(frame, text, (5, 90), 0, 0.7, textColor, 2)

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
