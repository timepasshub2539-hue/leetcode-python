from PIL import Image

def encode(img_path, msg, out):
    img = Image.open(img_path).convert('RGB')
    px = img.load()
    bits = ''.join(f'{ord(c):08b}' for c in msg) + '00000000'
    i = 0
    for y in range(img.height):
        for x in range(img.width):
            if i >= len(bits): break
            r, g, b = px[x, y]
            px[x, y] = ((r & ~1) | int(bits[i]), g, b)
            i += 1
    img.save(out)

def decode(img_path):
    img = Image.open(img_path).convert('RGB')
    px = img.load()
    bits = ''
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = px[x, y]
            bits += str(r & 1)
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == '00000000': break
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

if __name__ == '__main__':
    encode('cover.png', 'meet at noon', 'secret.png')
    print(decode('secret.png'))
