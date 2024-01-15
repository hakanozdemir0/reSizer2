import imageio.v2
from PIL import Image

foto =Image.open("foto.jpg")

eni = int(input("Eni: "))
boyu = int(input("Boyu: "))


newsize = (eni, boyu)
foto1 = foto.resize(newsize)

foto1.show()

yeni_foto_adi = "yenifoto.jpg"
foto1.save(yeni_foto_adi)
