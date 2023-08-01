import streamlit as st
from PIL import Image
import numpy as np
import cv2
from pyzbar import pyzbar
import time

class ReadQr:

    def _convert_to_rgb(self, image_np):
        if image_np.shape[-1] == 4:  # Check if the image has an alpha channel
            image_np = cv2.cvtColor(image_np, cv2.COLOR_BGRA2BGR)  # Convert from BGRA to BGR mode

        return image_np
    

    def _get_boundry_box(self,np_image,qr_code,index):
        qr_code_polygon = qr_code.polygon

        try:
            # Draw a green boundary box around the detected QR code
            pts = np.array(qr_code_polygon, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(np_image, [pts], True, (0, 255, 0), 2)

            # Draw the index above the boundary box
            x, y, _, _ = cv2.boundingRect(pts)
            cv2.putText(np_image, str(index), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception:
            pass

        return np_image
        

    def decode_uploaded_qr(self):
        upload = st.file_uploader("Upload an image", ["png", "jpeg", "jpg"], help="Upload an image with QR code")
        if upload is not None:
            image = Image.open(upload)
            decoded_qr_codes = pyzbar.decode(image)

            if decoded_qr_codes:
                image_np = np.array(image)

                # Convert the image to RGB mode without alpha channel
                image_np = self._convert_to_rgb(image_np)
                
                st.subheader("QR Code Contents 😀😀😀")
                img_place_holder = st.empty()
                for i, qr_code in enumerate(decoded_qr_codes, start=1):

                    image_np = self._get_boundry_box(np_image=image_np,qr_code=qr_code,index=i)

                    st.code(f"{i} -> {qr_code.data.decode('utf-8')}")

                image_with_boundary_boxes = Image.fromarray(image_np).convert("RGB")
                img_place_holder.image(image_with_boundary_boxes)
            else:
                st.info("QR code cannot be decoded....😥😥😥")

    def decode_from_video(self):
        """
            Could not be accomplished when hosted on remote server since cv uses server side camera,
            cannot use devices camera while running from server,
            This function is only usefull when running this script in local machine
        """
        cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
        stop_button_pressed = st.button("Stop")

        start_time = time.time()
        frame_count = 0
        decode_frequency = 5  # Decode QR codes every 5 frames (adjust as needed)

        while cap.isOpened() and not stop_button_pressed:
            ret, frame = cap.read()
            if not ret:
                st.write("Video Capture Ended")
                break

            frame_count += 1
            if frame_count % decode_frequency == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                decoded_qr_codes = pyzbar.decode(frame_rgb)

                if decoded_qr_codes:
                    st.subheader("QR Code Contents 😀😀😀")
                    for i, qr_code in enumerate(decoded_qr_codes, start=1):
                        st.code(f"{i} -> {qr_code.data.decode('utf-8')}")
                        frame_rgb = self._get_boundry_box(np_image=frame_rgb, qr_code=qr_code, index=i)

                    frame_placeholder.image(frame_rgb, channels="RGB")
                    break

            frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

            # Check if 30 seconds have elapsed and no QR code is detected
            if time.time() - start_time > 30:
                st.error("QR code not detected in 30 seconds. Please refresh the page to scan again")
                break

            if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
                break

        cap.release()
        cv2.destroyAllWindows()


    def decode_from_image(self):
        upload = st.camera_input("Capture Qr code", help="Capture Image of a qr code",key="camera ino")
        if upload is not None:
            image = Image.open(upload)
            decoded_qr_codes = pyzbar.decode(image)

            if decoded_qr_codes:
                image_np = np.array(image)
                st.subheader("QR Code Contents 😀😀😀")
                img_place_holder = st.empty()
                for i, qr_code in enumerate(decoded_qr_codes, start=1):

                    image_np = self._get_boundry_box(np_image=image_np,qr_code=qr_code,index=i)

                    st.code(f"{i} -> {qr_code.data.decode('utf-8')}")

                image_with_boundary_boxes = Image.fromarray(image_np).convert("RGB")
                img_place_holder.image(image_with_boundary_boxes)
            else:
                st.info("QR code cannot be decoded....😥😥😥")