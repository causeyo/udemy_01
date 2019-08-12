from PIL import Image

mac = Image.open('mac.jpg')

# mac.show()

print(mac.size)

print(mac.filename)

print(mac.format)

'''
(0,0)         X
  X -----------------------> 
  |           w
  |
Y | h
  |
  |
  V
'''
# mac.show()
computer = mac.crop((100, 100, 200, 200))
# mac.paste(im=computer, box=(10,10))
# computer.show()
mac = mac.resize((3000,100))
# mac.show()

mac = mac.rotate(90)
mac.show()