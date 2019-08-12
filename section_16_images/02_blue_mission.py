from PIL import Image

image_01 = Image.open('image_link.PNG')
image_02 = Image.open('cover_image.PNG')

image_02 = image_02.resize(image_01.size)
image_02.putalpha(120)

image_01.paste(im=image_02,box=(0,0),mask=image_02)
# image_02.paste(im=image_01,box=(0,0),mask=image_01)
image_01.show()
# image_02.show()


'''
If you are reading this link, then you’ve successfully read the hidden URL in the image.

Here is the information you will need:

The key for the encrypted message below is the largest known Fermat Prime passed through an SHA3_256 Hash. This number should be passed as a byte string by placing a b'' in front of the string.

Here is the message you need to decrypt:

b'gAAAAABaSsmdCFRxbqA6n-L0CMIMuhn26uGiIk5Wtx-V7wEPLBZYA67nGbNWyZziGyorwIlHqp3M5xrtzQj5tCab8XfBRCmdJXZYD1Fwp68AtD8WEMhblQ4I2DKDNFzqULH1DDETry3ptZnGZUgVo5gdDlnihqu1_oX-KboNpyRQ6J0DmeWTsm3L31btF_O6sX81rj3rBVI0qVuT7QdRT2burisQRnw5htA05llYgc1_fMkN_PSxCwY='


This message contains the next link. Best of luck.

'''
# image_01.show()
# image_02.show()