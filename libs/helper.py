from libs.create_qr import CreateQr
import streamlit as st

qr_types = {
    "URL": CreateQr.url_qr,
    "TEXT": CreateQr.regular_qr,
    "WIFI": CreateQr.wifi_qr,
    "EMAIL": CreateQr.email_qr,
    "VCARD": CreateQr.vcard_qr,
    "SMS": CreateQr.sms_qr,
    "TWITTER": CreateQr.twitter_qr,
    "GPS": CreateQr.geo_qr,
    "WHATSAPP": CreateQr.whatsapp_qr,
    "EVENT": CreateQr.event_qr
}

def get_sidebar():

    st.sidebar.subheader("Customization")

    # Split color options into two columns
    col1, col2 = st.sidebar.columns(2)
    
    # Dark colors
    dark = col1.color_picker("Dark Color",value="#000000",help="Color of dark section")
    dark_color_finder = col1.color_picker("Finder Dark Color", value="#000000", key="finder_dark", help="Color of the dark modules of the finder patterns.")
    dark_color_data = col1.color_picker("Data Dark Color", value="#000000", key="data_dark", help="Color of the dark data modules.")

    # Light colors
    light = col2.color_picker("Light Color",value="#FFFFFF",help="Color of white section")
    light_color_finder = col2.color_picker("Finder Light Color", value="#FFFFFF", key="finder_light", help="Color of the light modules of the finder patterns.")
    light_color_separator = col2.color_picker("Separator Color", value="#FFFFFF", key="separator", help="Color of the separator.")
    light_color_data = col2.color_picker("Data Light Color", value="#FFFFFF", key="data_light", help="Color of the light data modules.")
    light_color_quiet_zone = col1.color_picker("Quiet Zone Color", value="#FFFFFF", key="quiet_zone", help="Color of the quiet zone / border.")

    scale = st.sidebar.slider("Select Image scale",value=10,step=1,max_value=20,min_value=5)
    border = st.sidebar.slider("Select Image border",value=4,step=1,max_value=10,min_value=1)
    options = {
                "dark":dark,
                "finder_dark": dark_color_finder,
                "data_dark": dark_color_data,
                "light": light,
                "finder_light": light_color_finder,
                "data_light": light_color_data,
                "separator": light_color_separator,
                "quiet_zone": light_color_quiet_zone,
                "border": border,
                "scale": scale
            }
    
    return options