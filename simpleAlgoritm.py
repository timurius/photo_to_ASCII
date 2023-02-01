from PIL import Image, ImageOps
import pyperclip

def neronNetworkProcess( image, pixelSize ):
	characters =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.  "
	allPixelsOfImage =  list(image.getdata())	
	ASCIIresult = "";
	i = 0
	for x in allPixelsOfImage:
		if i >= image.size[0]:
			ASCIIresult += "\n"
			i = 0
		print( characters[ round(x / 3.64) ], x )
		ASCIIresult += characters[ round( x / 3.64) ] + " "
		i += 1
	return ASCIIresult
	

imagePath = input("Give me the path of your image: ").replace( "\"", "", 2)
try:
	image = Image.open(imagePath)
except FileNotFoundError:
	print("Incorect path to the file")
	exit()

grayscaledImage = image.convert('L')
print("Grayscaling complited")

invertedImage = ImageOps.invert(grayscaledImage)
invertedImage.save("grayscale_image.jpg")

result = neronNetworkProcess(invertedImage, 2)
print(result)
print( "Copied to your clipboard" )
name = input( "how you want to name this art? " )
file = open("./arts/"+name+".txt", "w")
file.write(result)
pyperclip.copy(result)