from eid_image_extractor.eid import Eid, EidNotInsertedException
from eid_image_extractor import filesystem


def main():
    try:
        print("Reading E-ID data")
        eid = Eid()
        eid_image_decode_string = eid.get_decoded_eid_image()
        national_number = eid.get_national_number()
        print("Writing image from E-ID to file")
        filesystem.write_file(eid_image_decode_string, f"{national_number}.jpg")
        print("Done!")
    except EidNotInsertedException:
        print("E-ID card not inserted, or could not be read")


if __name__ == "__main__":
    main()
