from PIL import Image

def decode_image(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")

    binary_data = ""

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    # split into 8-bit chunks
    all_bytes = [
        binary_data[i:i+8]
        for i in range(0, len(binary_data), 8)
    ]

    decoded_message = ""
    for byte in all_bytes:
        decoded_message += chr(int(byte, 2))
        if decoded_message.endswith("########"):
            break

    return decoded_message.replace("########", "")

# run decode
secret = decode_image("image/encoded.png")
print("Hidden message:", secret)