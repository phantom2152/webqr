import traceback
import streamlit as st

from libs.create_qr import CreateQr
from libs.helper import qr_types
from libs.show_qr import ShowQr
from libs.read_qr import ReadQr
from libs.layout.sidebar import get_sidebar
from libs.layout.footer import get_footer

st.set_page_config(page_title="WEB QR 🖥🖥")

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
        st.caption("⬅️ Customize your QR code using the side bar")
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
        st.caption("Multiple QR codes in a photo can also be detected")
        rqr = ReadQr()
        if mode == "Upload":
            rqr.decode_uploaded_qr()
        else:
            rqr.decode_from_image()

    



if __name__ == "__main__":
    main()
    get_footer()
