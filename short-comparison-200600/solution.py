from PIL import Image, ImageDraw
img = Image.new('RGB', (600, 400))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 600, 133], fill='orange')
