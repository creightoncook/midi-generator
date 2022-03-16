"""Parsers convert user input."""
from __future__ import annotations

from dataclasses import asdict

from midiutil.MidiFile import MIDIFile

from midi_generator.midi_generator_base import *
from midi_generator.music_types import *


def parse_note(notation: str) -> Note:
    """User input to music_types.Note."""

    # Only support notation like C, C3, C#2
    if not 1 <= len(notation) <= 3:
        raise UnsupportedNotation(f"Unsupported note {notation}")

    if len(notation) == 1:
        pitch = notation
        octave = BASE_OCTAVE
    else:
        pitch = notation[:-1]
        octave = notation[-1]

    if pitch not in SHARPS + FLATS:
        raise UnsupportedNotation(f"Unsupported note {notation}")

    return Note(pitch=pitch, octave=int(octave))


def _parse_numeral_chord(numeral: str) -> Chord:
    return Chord(numeral)
    
# def _parse_letter_chord() -> Chord:

def parse_chord(numeral: str) -> Chord:
    """User input to music_type.Chord."""
    """User input to Chord."""
    if numeral.lower() in NUMERALS:
        return _parse_numeral_chord(numeral)

    raise UnsupportedNotation(f"Unsupported numeral {numeral}")

    


def parse_chord_progression(text: str) -> list[Chord]:
    """User input to a list of music_type.Chord."""
    numerals = text.split("-")
    print(f"Numerals are {numerals}")

    chords = [parse_chord(numeral) for numeral in numerals]

    return chords


def main():
    """Main."""
    # create your MIDI object
    TEMPO = 120
    mf = MIDIFile(1)  # only 1 track
    track = 0  # the only track

    time = 0  # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, TEMPO)

    chords = parse_chord_progression("II-vi-IV-V")

    for chord in chords:
        print(chord)
        for note in chord_to_midi(chord):
            mf.addNote(**asdict(note))

    with open("prog.mid", "wb") as outf:
        mf.writeFile(outf)


if __name__ == "__main__":
    main()
