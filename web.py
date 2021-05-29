import io


def index():
    file = io.open('pages/index.html', mode='r', encoding='utf-8')
    page = file.read()
    file.close()
    return {
        'content_type': 'text/html',
        'contents': bytes(page, 'utf8'),
    }


def braba_image():
    file = open('images/lansa_um_pix.jpeg', 'rb')
    image = file.read()
    file.close()
    return {
        'content_type': 'text/html',
        'contents': image,
    }
