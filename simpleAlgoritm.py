from PIL import Image, ImageOps
import pyperclip

def neronNetworkProcess( image, pixelSizeH = 2, pixelSizeW = 1 ):
	characters =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.  "
	allPixelsOfImage = list(image.getdata())	
	ASCIIresult = ""
    h = 0
	w = 0
	while h < image.size(1):
	    if w >= image.size[0]:
			ASCIIresult += "\n"
			w = 0
            h += pixelSizeH
		ASCIIresult += characters[ round( characters[ image.size[0] * h + w ] / 3.64) ]
		w += pixelSizeW
	return ASCIIresult
	

imagePath = input("Give me the path of your image: ").replace( "\"", "", 2)
try:
	image = Image.open(imagePath)
except FileNotFoundError:
	print("Incorect path to the file")
	exit()

grayscaledImage = image.convert('L')

invertedImage = ImageOps.invert(grayscaledImage)
invertedImage.save("grayscale_image.jpg")

width = invertedImage.size[0]
height = invertedImage.size[1]

maxWidth = eval(input("Input max width of image: "))

if( width > maxWidth ):
    changer = (width / maxWidth)
    width = round(width / changer)
    height = round(height / changer)
    
result = neronNetworkProcess(invertedImage.resize( (width, height) ), 2)
print(result)
print( "Copied to your clipboard" )
name = input( "how you want to name this art? " )
file = open("./arts/"+name+".txt", "w")
file.write(result)
pyperclip.copy(result)
