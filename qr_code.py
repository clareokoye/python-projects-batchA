import qrcode


def create_qrcode(text):
    qrc = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 11,
        border = 4,
    )
    qrc.add_data(text)
    qrc.make(fit=True)
    
    imag = qrc.make_image(fill_color = "black", back_color = "white")
    imag.save("qrgforcenwa.png")

url = input ("Enter your url:  ")

create_qrcode(url)

        