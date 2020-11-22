from PIL import Image,ImageDraw,ImageFont

image=Image.open("C:\\PROJECTS\\Clock\\clock.png")
draw =ImageDraw.Draw(image)
font1=ImageFont.truetype("arial.ttf,100")
points=100,400
string="Imran"
color="black"

draw.text(points,string,color,font=font1)
image.show()
