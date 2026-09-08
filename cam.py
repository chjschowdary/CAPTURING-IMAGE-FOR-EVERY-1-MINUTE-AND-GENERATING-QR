"""import cv2
import qrcode
import base64
import os
import time
from datetime import datetime

os.makedirs("qr_codes", exist_ok=True)

print("QR capture system (HIGH RELIABILITY MODE)")

try:
    while True:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cam.release()

        if not ret:
            print("Camera error")
            time.sleep(60)
            continue

        # Smaller image → fewer QRs
        frame = cv2.resize(frame, (160, 160))

        # PNG encode
        success, buffer = cv2.imencode(".png", frame)
        if not success:
            continue

        img_bytes = buffer.tobytes()
        encoded = base64.b64encode(img_bytes).decode("ascii")

        # 🔑 SMALLER chunk size (very important)
        chunk_size = 400
        chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for i, chunk in enumerate(chunks):
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # 🔥 HIGH
                box_size=10,
                border=4,
            )
            qr.add_data(f"{timestamp}|{i+1}/{len(chunks)}|{chunk}")
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"qr_codes/qr_{timestamp}_{i+1}.png")

        print(f"[{timestamp}] Generated {len(chunks)} QRs (safe mode)")

        time.sleep(60)

except KeyboardInterrupt:
    print("Stopped")"""


import cv2
import qrcode
import hashlib
import time
from datetime import datetime
import os

os.makedirs("qr_codes", exist_ok=True)

cam = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cam.read()
        if not ret:
            time.sleep(60)
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create hash as image proof
        img_hash = hashlib.sha256(frame.tobytes()).hexdigest()

        qr_data = f"""
        Capture Time: {timestamp}
        Source: Webcam
        Image Hash: {img_hash}
        """

        qr = qrcode.make(qr_data)
        qr.save(f"qr_codes/qr_{timestamp.replace(':','-')}.png")

        print("QR saved:", timestamp)
        time.sleep(60)

except KeyboardInterrupt:
    cam.release()

