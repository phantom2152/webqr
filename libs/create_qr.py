import streamlit as st
from segno import helpers as hp
import segno
import urllib
import datetime


class CreateQr:

    def _create_qr_code(self, data):
        qrcode = segno.make(data, micro=False)
        return qrcode
    

    def regular_qr(self):
        with st.form("regular_qr_form"):
            st.info("Please Enter the data you want to encode")
            
            qr_data = st.text_area('Text', key="regular_qr", help="Enter the text you want to encode as a QR code.")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if not qr_data == "":
                    qr = self._create_qr_code(qr_data)
                    return qr
                else:
                    st.warning("Please enter data you want to encode in text box")



    def wifi_qr(self):
        with st.form("wifi_qr_form"):
            st.info("Please fill in the details")
            
            ssid = st.text_input("SSID", key="ssid", help="Enter the name of your Wi-Fi network (Service Set Identifier).")
            password = st.text_input("Password", key="password", help="Enter the password for your Wi-Fi network.")
            security = st.selectbox("Security", ("None", "WEP", "WPA/WPA2"), index=2, key="security", help="Select the security type for your Wi-Fi network.").replace("None","nopass")
            hidden = st.checkbox("Hidden", key="hidden", help="Check this if your Wi-Fi network is hidden (not broadcasted).")
            submitted = st.form_submit_button("Submit")

            if submitted:
                if not ssid == "":
                    wifi_config = hp.make_wifi_data(ssid=ssid, password=password, security=security, hidden=hidden)
                    qr = self._create_qr_code(wifi_config)
                    return qr
                else:
                    st.warning("Please enter SSID")


    def url_qr(self):
        with st.form("url_qr_form"):
            st.info("Please Enter the url you want to encode")
            
            url_data = st.text_input('URL', key="url_qr", help="Enter the URL you want to encode as a QR code.")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if not url_data == "":
                    qr = self._create_qr_code(url_data)
                    return qr
                else:
                    st.warning("Please enter the url you want to encode.")

    
    def email_qr(self):
        with st.form("email_qr_form"):
            st.info("Please fill in the details")
            st.code("Please separate multiple email addresses by comma(,). Not all fields are mandatory.")

            to = st.text_input("TO", help="Enter the email address of the recipient(s) in the 'To' field. Separate multiple addresses with a comma(,).").split(",")
            cc = st.text_input("CC", help="Enter the email address of the recipient(s) in the 'CC' field. Separate multiple addresses with a comma(,).").split(",")
            bcc = st.text_input("BCC", help="Enter the email address of the recipient(s) in the 'BCC' field. Separate multiple addresses with a comma(,).").split(",")
            subject = st.text_input("Subject", help="Enter the subject of the email.")
            body = st.text_area("Body", help="Enter the main content of the email.")
            submitted = st.form_submit_button("Submit")
            if submitted:
                if not to == ['']:
                    email_config = hp.make_make_email_data(to=to,cc=cc,bcc=bcc,subject=subject,body=body)
                    qr = self._create_qr_code(email_config)
                    return qr
                else:
                    st.warning("Please enter TO email address")

    def sms_qr(self):
        with st.form("sms_qr_form"):
            st.info("Please fill in the details")
            
            number = st.text_input("Number", help="Enter the recipient's phone number in international format (e.g., +123456789).")
            message = st.text_area("Message", help="Enter the content of the SMS message.")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if not number == "":
                    sms_config = f"SMSTO:{number}:{message}"
                    qr = self._create_qr_code(sms_config)
                    return qr
                else:
                    st.warning("Please enter Number")
            

    def twitter_qr(self):

        option = st.selectbox("Choose an option", ("Link to your profile", "Post a tweet"))
        with st.form("twitter_qr_form"):

            if option == "Link to your profile":
                profile = st.text_input("@username", help="Enter your Twitter username (without the @ symbol).")
                profile = profile.lstrip("@")  # Remove leading @ symbol if present
                encoded_profile = urllib.parse.quote_plus(profile)
                data = f"https://twitter.com/{encoded_profile}"
            else:
                text = st.text_area("Text", max_chars=280, help="Enter the text for your tweet.")
                encoded_text = urllib.parse.quote_plus(text)
                data = f"https://twitter.com/intent/tweet?text={encoded_text}"

            submitted = st.form_submit_button("Submit")

            if submitted:
                qr = self._create_qr_code(data)
                return qr
            
    def vcard_qr(self):
        with st.form("vcard_qr_form"):
            st.info("Please fill in the details")
            st.code("Not all fields are mandatory.")

            name = st.text_input("Name", key="name", help="Enter the name of the contact. If the name consists of first and last name separated by a semicolon (;), enter it accordingly.")
            displayname = st.text_input("Display Name", key="displayname", help="Enter the name to be displayed for the contact.")
            email = st.text_input("Email", key="email", help="Enter the email address of the contact. For multiple emails, separate them with commas.").split(",")
            phone = st.text_input("Phone", key="phone", help="Enter the phone number of the contact. For multiple phone numbers, separate them with commas.").split(",")
            fax = st.text_input("Fax", key="fax", help="Enter the fax number of the contact. For multiple fax numbers, separate them with commas.").split(",")
            nickname = st.text_input("Nickname", key="nickname", help="Enter the nickname of the contact.")
            birthday = st.date_input("Birthday", key="birthday", help="Select the birthday of the contact.",min_value=datetime.date(1947, 1, 1))
            url = st.text_input("URL", key="url", help="Enter the URL associated with the contact. For multiple URLs, separate them with commas.").split(",")
            pobox = st.text_input("PO Box", key="pobox", help="Enter the PO Box of the contact.")
            street = st.text_input("Street", key="street", help="Enter the street address of the contact.")
            city = st.text_input("City", key="city", help="Enter the city of the contact.")
            region = st.text_input("Region", key="region", help="Enter the region or state of the contact.")
            zipcode = st.text_input("Zipcode", key="zipcode", help="Enter the postal or zip code of the contact.")
            country = st.text_input("Country", key="country", help="Enter the country of the contact.")
            org = st.text_input("Organization", key="org", help="Enter the organization of the contact.")
            title = st.text_input("Title", key="title", help="Enter the title or job position of the contact. For multiple titles, separate them with commas.").split(",")
            photo_uri = st.text_input("Photo URI", key="photo_uri", help="Enter the URL of the contact's photo. For multiple photo URIs, separate them with commas.").split(",")
            
            submitted = st.form_submit_button("Submit")

            if submitted:
                vcard_config = hp.make_vcard_data(
                    name=name,displayname=displayname,email=email,phone=phone,fax=fax,nickname=nickname,birthday=birthday,url=url,pobox=pobox,street=street,
                    city=city,region=region,zipcode=zipcode,country=country,org=org,title=title,photo_uri=photo_uri)
                qr = self._create_qr_code(vcard_config)
                return qr

            
    
    def geo_qr(self):
        with st.form("geo_qr_form"):
            st.info("Please fill in the details")

            lat = st.text_input("Latitude", key="lat", help="Enter the latitude of the location as a decimal number.")
            lng = st.text_input("Longitude", key="lng", help="Enter the longitude of the location as a decimal number.")
            
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                try:
                    lat_value = float(lat)
                    lng_value = float(lng)
                    geo_config = hp.make_geo_data(lat=lat_value,lng=lng_value)
                    qr = self._create_qr_code(geo_config)
                    return qr
                except ValueError:
                    st.error("Invalid input! Please enter valid decimal numbers for latitude and longitude.")
                


    

    

            

    
