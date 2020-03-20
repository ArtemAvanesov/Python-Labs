# Делает фотографии каждые 5 сек и отправляет их на компьютер, в камере фото не сохраняются!

from goprocam import GoProCamera
from goprocam import constants
from PIL import Image
gopro = GoProCamera.GoPro()
TIMER=5
num_photo=5
COUNT = 0
while COUNT<num_photo:
	gopro.downloadLastMedia(gopro.take_photo(TIMER), "GoPro проекты/Фото каждые 5 сек/Фото/Photo_" + str(COUNT) + ".jpg")
	gopro.delete("last")
	img = Image.open(r"GoPro проекты/Фото каждые 5 сек/Фото/Photo_" + str(COUNT) + ".jpg")
	img.show()
	COUNT += 1
print("Готово!")