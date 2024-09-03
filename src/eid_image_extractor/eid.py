from eidreader import eid2dict
from eid_image_extractor import filesystem
import base64


class EidNotInsertedException(Exception):
    pass


class Eid:
    def __init__(self):
        self.eid_data = self.get_eid_data()
        if not self.eid_inserted():
            raise EidNotInsertedException()

    def eid_inserted(self):
        return self.eid_data["success"]

    def extract_and_write_image(self):
        eid_image_decode_string = self.get_decoded_eid_image()
        national_number = self.get_national_number()
        filesystem.write_file(eid_image_decode_string, f"{national_number}.jpg")
        return True

    def get_eid_data(self):
        return eid2dict()

    def get_eid_image(self):
        return self.eid_data["PHOTO_FILE"]

    def get_decoded_eid_image(self):
        return base64.b64decode(self.get_eid_image())

    def get_national_number(self):
        return self.eid_data["national_number"]
