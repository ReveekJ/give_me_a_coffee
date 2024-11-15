from uuid import uuid4

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.main import QRCode

qr = QRCode(
    image_factory=StyledPilImage
)

def generate_qr(link: str) -> str:
    qr.add_data(link)
    img: StyledPilImage = qr.make_image(module_drawer=RoundedModuleDrawer())
    path = f'/qr_codes/{uuid4()}.png'
    img.save(path)

    return path

# TODO: автоудаление картинки при закрытии контейнера
