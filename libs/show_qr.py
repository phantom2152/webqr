import streamlit as st
import base64

class ShowQr:
    def __init__(self, qrobj) -> None:
        self.qrobj = qrobj

    def _get_image_byts(self,qr_uri):
        _, base64_data = qr_uri.split(';base64,')
        img_byts = base64.b64decode(base64_data)
        return img_byts


    def display_qr(self,qr_type):
        qr_uri = self.qrobj.png_data_uri(scale=10)
        _,img,_ = st.columns((1,3,1.2))
        with img:
            st.header(f"Here is your {qr_type} QR")
            st.image(qr_uri)
            image_bytes = self._get_image_byts(qr_uri)
            st.download_button(label='Download QR Code', data=image_bytes, file_name='qrcode.png', mime='image/png')
