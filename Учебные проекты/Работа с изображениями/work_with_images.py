import random
from PIL import Image, ImageDraw

mode = int(input('mode:')) #Считываем номер преобразования. 

if (mode == 0):
	# Оттенок серого
	# Для получения этого преобразования необходимо «усреднить» каждый пиксел.
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() #Выгружаем значения пикселей.
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))

	image.save("Учебные проекты/Работа с изображениями/images/grey.jpg", "JPEG")
	image.close()
	del draw

elif (mode == 1):
	# Сепия
	# Чтобы получить сепию, нужно посчитать среднее значение и взять какой — нибудь коэффициент. 
	# middle = (R + G + B) / 3
	# Первое значение пиксела ( R ) = middle + 2 * k
	# Второе значение пиксела ( G ) = middle + k
	# Третье значение пиксела ( B ) = middle
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() #Выгружаем значения пикселей.
	depth = int(input('depth:')) #Например равное 30
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			a = S + depth * 2
			b = S + depth
			c = S
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	image.save("Учебные проекты/Работа с изображениями/images/sepia.jpg", "JPEG")
	del draw

elif (mode == 2):
	# Негатив
	# Для получения негатива достаточно каждое значение пиксела вычесть из 255.
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() #Выгружаем значения пикселей.
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))

	image.save("Учебные проекты/Работа с изображениями/images/negative.jpg", "JPEG")
	del draw

elif (mode == 3):
	# Добавление шумов
	# Для получения шумов, будем всегда добавлять к пикселу какое — нибудь рандомное значение.
	# Чем больше разброс этих значений, тем больше шумов.
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() #Выгружаем значения пикселей.
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			rand = random.randint(-factor, factor)
			a = pix[i, j][0] + rand
			b = pix[i, j][1] + rand
			c = pix[i, j][2] + rand
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	image.save("Учебные проекты/Работа с изображениями/images/noise.jpg", "JPEG")
	del draw

elif (mode == 4):
	# Яркость
	# Для регулирования яркости к каждому пикселу мы будем добавлять определенное значение.
	# Если оно > 0, то картинка становится ярче, иначе темнее.
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() #Выгружаем значения пикселей.
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0] + factor
			b = pix[i, j][1] + factor
			c = pix[i, j][2] + factor
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	image.save("Учебные проекты/Работа с изображениями/images/brightness.jpg", "JPEG")
	del draw

elif (mode == 5):
	# Черно-белое
	# Все пикселы надо разбить на 2 группы: черные и белые.
	# Для проверки принадлежности к определенной группе мы будем смотреть
	# к чему ближе значение пиксела: к белому цвету или к чёрному.
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() #Выгружаем значения пикселей.
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)):
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))

	image.save("Учебные проекты/Работа с изображениями/images/black&white.jpg", "JPEG")
	del draw

elif (mode == 6):
	# Сжатие изображений
	image = Image.open("Учебные проекты/Работа с изображениями/images/original.jpg") #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 
	factor = int(input('factor:'))	
	size = factor, int(float(height) * float(factor / float(width)))
	pix = image.load() #Выгружаем значения пикселей.
	image.thumbnail(size, Image.ANTIALIAS)
	image.save("Учебные проекты/Работа с изображениями/images/resize.jpg", "JPEG")
	del draw
	