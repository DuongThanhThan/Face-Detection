import simplejson as json


<<<<<<< HEAD:apps/Face/helper/image_helper.py
def list_image(image : str) -> list:
    jsonDec = json.decoder.JSONDecoder()
    list_img = jsonDec.decode(str(image))
    return list_img
=======
def list_image(image):
    jsonDec = json.decoder.JSONDecoder()
    list_img = jsonDec.decode(str(image))
    return list_img
>>>>>>> 6680004 (new version):Face/helper/image_helper.py
