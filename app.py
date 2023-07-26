import traceback
import streamlit as st
from pyzbar import pyzbar
from PIL import Image

from libs.create_qr import CreateQr
from libs.helper import qr_types,get_sidebar
from libs.show_qr import ShowQr

from segno import helpers as hp
import cv2


def qr_cam():
    camera_id = 0
    delay = 1
    window_name = 'OpenCV QR Code'

    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)

    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                        print(s)
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
            cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)



def read_qr_code(upload):
    try:
        image = Image.open(upload)
        qr_codes = pyzbar.decode(image)
        qr_data = []
        for qr in qr_codes:
            data = qr.data.decode('utf-8')
            qr_data.append(data)
        print(qr_data)
        return qr_data
    except Exception:
        traceback.print_exc()
        return []


def main():
    st.title("WEB QR 🖥🖥")

    options= get_sidebar()

    op = st.radio(
        "Select opeartion",
        ("Create QR", "Read QR"),
        horizontal=True
    )

    if op == "Create QR":
        cqr = CreateQr()
        qr_type = st.radio(label="Which Qr Code do you want to generate?", options= qr_types.keys(),horizontal=True, help="Choose the type of QR you want to generate")
        qr_data_func = qr_types[qr_type]
        qr_data = qr_data_func(cqr)
        if not qr_data:
            pass
        else:
            try:
                sqr = ShowQr(qrobj=qr_data)
                sqr.display_qr(qr_type=qr_type,options = options)
            except Exception:
                traceback.print_exc()
                st.warning("Cannot generate Qr code now")
    else:
        mode = st.radio("Choose Mode", ("Upload", "Camera"), horizontal=True)
        if mode == "Upload":
            upload = st.file_uploader("upload", ["png", "jpeg"])
        else:
            upload = st.camera_input("Capture Image")

        if upload is not None:
            data = read_qr_code(upload)
            if data:
                st.subheader("QR Code Contents 😀😀😀")
                for d in data:
                    st.code(d)
            else:
                st.info("QR code cannot be decoded....😥😥😥")


if __name__ == "__main__":
    main()
