import base64
import traceback
import streamlit as st
import segno
from pyzbar import pyzbar
from PIL import Image

def get_image_byts(qr_uri):
    _, base64_data = qr_uri.split(';base64,')
    img_byts = base64.b64decode(base64_data)
    return img_byts


def create_qr_code(data):
    qrcode = segno.make(data, micro=False)
    return qrcode


def read_qr_code(upload):
    try:
        image = Image.open(upload)
        qr_codes = pyzbar.decode(image)
        qr_data = []
        for qr in qr_codes:
            data = qr.data.decode('utf-8')
            qr_data.append(data)
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
        qr_data = st.text_input('Please enter the data you want to encode')
        if qr_data == "":
            st.warning("Please enter data you want to encode in text box")
        else:
            try:
                qr = create_qr_code(qr_data)
                st.header("Here is your qr code 🙂🙂🙂🙂")
                qr_uri = qr.png_data_uri(scale=10)
                st.image(qr_uri)
                image_bytes = get_image_byts(qr_uri)
                st.download_button(label='Download QR Code', data=image_bytes, file_name='qrcode.png', mime='image/png')
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
                    st.write(d)
            else:
                st.info("QR code cannot be decoded....😥😥😥")


if __name__ == "__main__":
    main()
