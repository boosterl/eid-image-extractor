from eidreader.main import eid2dict
import base64


def get_eid_data():
    return eid2dict()


def get_eid_image(eid_data):
    return eid_data['PHOTO_FILE']


def get_national_number(eid_data):
    return eid_data['national_number']


def eid_inserted(eid_data):
    return eid_data['success']


def write_image(eid_image_decode, national_number):
    eid_image = open('{}.jpeg'.format(national_number), 'wb')
    eid_image.write(eid_image_decode)
    eid_image.close()


if __name__ == '__main__':
    eid_data = get_eid_data()
    if (eid_inserted(eid_data)):
        eid_image_decode_string = base64.b64decode(get_eid_image(eid_data))
        national_number = get_national_number(eid_data)
        write_image(eid_image_decode_string, national_number)
    else:
        print('E-ID card not inserted, or could not be read')
