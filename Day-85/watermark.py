from PIL import Image, ImageFont, ImageDraw

base = Image.open("D:/Python/Day-85/base.jpg")
watermark = Image.open("Day-85/watermark.png")

base.show()

width,height = base.size

font = ImageFont.truetype("arial.ttf", 4)

draw = ImageDraw.Draw(base)
text = "sample watermark"

draw.text((0,0),text=text,font=font)
base.show()

transparent = Image.new('RGBA', (width, height), (0,0,0,0))
transparent.paste(base,(0,0))
transparent.paste(watermark, (0,0))
transparent.show()


# from PIL import Image

# background = Image.open("Day-85/base.jpg")
# foreground = Image.open("Day-85/watermark.png")

# background.paste(foreground,())
# background.show()