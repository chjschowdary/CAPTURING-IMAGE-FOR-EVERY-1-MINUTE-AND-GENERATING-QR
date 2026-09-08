import cv2
import qrcode
import os
import time
from datetime import datetime

# Create folders if not existclea
if not os.path.exists("photos"):
    os.mkdir("photos")

if not os.path.exists("qr_codes"):
    os.mkdir("qr_codes")

# Open webcam
camera = cv2.VideoCapture(0)

print("Webcam started... Press CTRL+C to stop")

try:
    while True:
        # Read frame from webcam
        ret, frame = camera.read()

        if ret:
            # Timestamp for unique file names
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Image file path
            image_path = f"photos/image_{timestamp}.jpg"
            cv2.imwrite(image_path, frame)

            # Generate QR code with image path
            qr = qrcode.make(os.path.abspath(image_path))

            qr_path = f"qr_codes/qr_{timestamp}.png"
            qr.save(qr_path)

            print(f"Captured image and QR saved at {timestamp}")

        else:
            print("Failed to capture image")

        # Wait for 1 minute (60 seconds)
        time.sleep(10)

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    camera.release()
    cv2.destroyAllWindows()
