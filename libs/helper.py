from libs.create_qr import CreateQr


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

