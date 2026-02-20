from PIL import Image

# convert message to binary
def message_to_binary(message):
    return ''.join(format(ord(i), '08b') for i in message)

# encode message into image
def encode_image(image_path, message):
    image = Image.open(image_path)
    image = image.convert("RGB")

    # add end marker
    message += "########"
    binary_message = message_to_binary(message)

    data_index = 0
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            if data_index < len(binary_message):
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1

            if data_index < len(binary_message):
                g = (g & ~1) | int(binary_message[data_index])
                data_index += 1

            if data_index < len(binary_message):
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1

            pixels[x, y] = (r, g, b)

            if data_index >= len(binary_message):
                image.save("image/encoded.png")
                print("✅ Message hidden successfully!")
                return

# run encode
secret_message = input("Enter secret message: ")
encode_image("image/sample.jpg", secret_message)