import simplejson as json


<<<<<<< HEAD:Face/helper/image_helper.py
def list_image(image):
    jsonDec = json.decoder.JSONDecoder()
    list_img = jsonDec.decode(str(image))
    return list_img
=======
def list_image(image : str) -> list:
    jsonDec = json.decoder.JSONDecoder()
    list_img = jsonDec.decode(str(image))
    return list_img
>>>>>>> 2257d60 (image upload):apps/Face/helper/image_helper.py
