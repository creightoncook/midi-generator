"""Utility script used to generate music_types.MIDI_LOOKUP"""
from midi_generator.music_types import *

def midi_lookup(*notations: str):
    from itertools import product
    return (
        (Note(pitch=note[1], octave=note[0]) for note in product(range(10), notation))
        for notation in notations
    )
    # for notations in [SHARPS, FLATS]:

    # from itertools import product
    # sharps = (Note(pitch=note[1], octave=note[0]) for note in product(range(10), SHARPS))
    # flats = (Note(pitch=note[1], octave=note[0]) for note in product(range(10, FLATS)))
    # return sharps, flats


def main_create_table():
    # Pulled from https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
    MIDI_NOTE_START = 12
    MIDI_NOTE_STOP = 128
    sharps, flats = midi_lookup(SHARPS, FLATS)

    sharp_labels = map(
        lambda note: str(note),
        sharps
    )

    sharp_table = dict(
        zip(
            sharp_labels,
            range(MIDI_NOTE_START, MIDI_NOTE_STOP), 
        )
    )

    return sharp_table