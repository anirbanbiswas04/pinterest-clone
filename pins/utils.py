from django.core.files import File
from io import BytesIO
from PIL import Image


def make_thumbnail(image):
    img = Image.open(image)
    img.thumbnail(size=(300, 200))

    thumb_io = BytesIO()
    img.save(thumb_io, 'PNG', quality=70)
    thumbnail = File(thumb_io, name=image.name)

    return thumbnail
