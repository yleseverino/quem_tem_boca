from os import environ

BUCKET = environ.get('BUCKET')
ENDPOINT_URL = environ.get('ENDPOINT_URL')
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')

def get_restaurant_logo(restaurant_id):
        if not AWS_ACCESS_KEY_ID:
                return "https://cdn.pixabay.com/photo/2013/07/13/09/36/pizza-155771_960_720.png"
        return f'{ENDPOINT_URL}/{BUCKET}/restaurantes/{restaurant_id}/logo.webp?AWSAccessKeyId={AWS_ACCESS_KEY_ID}'

def get_restaurant_background(restaurant_id):
        if not AWS_ACCESS_KEY_ID:
                return "https://cdn.pixabay.com/photo/2014/04/22/02/56/pizza-329523_960_720.jpg"
        return f'{ENDPOINT_URL}/{BUCKET}/restaurantes/{restaurant_id}/backgroud.webp?AWSAccessKeyId={AWS_ACCESS_KEY_ID}'

