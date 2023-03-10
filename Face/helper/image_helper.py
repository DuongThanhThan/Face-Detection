import simplejson as json


def list_image(image):
    jsonDec = json.decoder.JSONDecoder()
    list_img = jsonDec.decode(str(image))
    return list_img
