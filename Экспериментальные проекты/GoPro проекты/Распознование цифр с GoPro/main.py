from goprocam import GoProCamera
from goprocam import constants
from PIL import Image, ImageDraw

gopro = GoProCamera.GoPro()
TIMER=1
COUNT=0
while COUNT < 4:
    COUNT += 1
    gopro.downloadLastMedia(gopro.take_photo(TIMER), "Photo_" + str(COUNT) + ".jpg")
    gopro.delete("last")
    image = Image.open("Photo_" + str(COUNT) + ".jpg") #Открываем изображение.
    factor = 100
    size = factor, int(float(image.size[1]) * float(factor / float(image.size[0])))
    image.thumbnail(size, Image.ANTIALIAS)
    image.save("Photo_" + str(COUNT) + ".jpg", "JPEG")
    width = image.size[0] #Определяем ширину.
    height = image.size[1] #Определяем высоту.
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    pix = image.load() #Выгружаем значения пикселей.
    for i in range(width):
	    for j in range(height):
		    a = pix[i, j][0]
		    b = pix[i, j][1]
		    c = pix[i, j][2]
		    S = a + b + c
            # 1 - параметр, определяющий силу эффекта
		    if (S > (((255 - 80) // 2) * 3)):
			    a, b, c = 255, 255, 255
		    else:
			    a, b, c = 0, 0, 0
		    draw.point((i, j), (a, b, c))

    image.save("Photo_" + str(COUNT) + ".jpg", "JPEG")
    del draw