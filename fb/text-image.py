import Image
import ImageDraw
import ImageFont


fontname = "font.ttf"
fontsize = 20
text = "spandey2405@gmail.com"

colorText = "#81F7D8"

font = ImageFont.truetype(fontname, fontsize)
img = Image.new( 'RGB', (500,300), "#0B615E")
d = ImageDraw.Draw(img)
d.text((20,20), text, fill=colorText, font=font)
img.save("image.png")