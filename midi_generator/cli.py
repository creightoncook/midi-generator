"""Console script for midi_generator."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("midi-generator")
    click.echo("=" * len("midi-generator"))
    click.echo("Fun project to easily generate MIDI using music notation.    ")


if __name__ == "__main__":
    main()  # pragma: no cover
