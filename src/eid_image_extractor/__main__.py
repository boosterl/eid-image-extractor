import click

from eid_image_extractor.eid import Eid, EidNotInsertedException


@click.command()
@click.option(
    "--destination", help="Image from E-ID will be written to the following file"
)
def main(destination):
    try:
        click.echo("Reading E-ID data ⌛")
        eid = Eid()
        eid_image_decoded_string = eid.get_decoded_eid_image()
        destination_file = (
            destination if destination else f"{eid.get_national_number()}.jpg"
        )
        click.echo(f"Writing image from E-ID to file {destination_file} ⌛")
        with click.open_file(destination_file, "wb") as f:
            f.write(eid_image_decoded_string)
        click.echo(f"Done! ✅")
    except EidNotInsertedException:
        print("E-ID card not inserted, or could not be read ❌")


if __name__ == "__main__":
    main()
