"""Main module."""
from __future__ import annotations

from dataclasses import astuple

from midi_generator.music_types import *


def note_to_midi(note: Note) -> MIDINote:
    lookup = f"{note.pitch}{note.octave}"
    try:
        return MIDINote(pitch=NOTE_TO_MIDI_LOOKUP[lookup])
    except ValueError:
        raise UnsupportedMIDI(f"${lookup} is not convertable to MIDI")


def chord_to_notes(chord: Chord) -> list[Note]:
    # I -> [C4, E4, G4]
    notes = []
    for note in TRIAD:
        offset = sum(chord.interval[: note + 1])
        pitch = SHARPS[offset % 12]
        print(offset)
        notes.append(Note(pitch=pitch, octave=BASE_OCTAVE))
    return notes


def chord_to_midi(chord: Chord) -> list[MIDINote]:
    return list(map(note_to_midi, chord_to_notes(chord)))
