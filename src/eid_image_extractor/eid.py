import base64

from eidreader import eid2dict


class EidNotInsertedException(Exception):
    pass


class Eid:
    def __init__(self):
        self.eid_data = self.get_eid_data()
        if not self.eid_inserted():
            raise EidNotInsertedException()

    def eid_inserted(self):
        return self.eid_data["success"]

    def get_eid_data(self):
        return eid2dict()

    def get_eid_image(self):
        return self.eid_data["PHOTO_FILE"]

    def get_decoded_eid_image(self):
        return base64.b64decode(self.get_eid_image())

    def get_national_number(self):
        return self.eid_data["national_number"]
