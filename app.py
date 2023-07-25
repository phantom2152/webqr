import traceback
import streamlit as st
from pyzbar import pyzbar
from PIL import Image

from libs.create_qr import CreateQr
from libs.helper import qr_types
from libs.show_qr import ShowQr

from segno import helpers as hp



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
                sqr.display_qr(qr_type=qr_type)
            except Exception:
                traceback.print_exc()
                st.warning("Cannot generate Qr code now")
    else:
        mode = st.radio("Choose Mode", ("Upload", "Camera"), horizontal=True)
        if mode == "Upload":
            upload = st.file_uploader("upload", ["png", "jpeg"])
        else:
            upload = st.camera_input("Take a picture")

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
