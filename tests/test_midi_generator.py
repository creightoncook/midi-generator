#!/usr/bin/env python
"""Tests for `midi_generator` package."""

import pytest
from click.testing import CliRunner

from midi_generator import cli, midi_generator_base
from midi_generator.music_types import *


def test_note_to_midi():
    assert midi_generator_base.note_to_midi(Note("C", 4)) == MIDINote(pitch=60)
    with pytest.raises(UnsupportedMIDI):
        midi_generator_base.note_to_midi(Note("C", 10))


def test_chord_to_notes():
    assert midi_generator_base.chord_to_notes(Chord("I")) == [Note("C", 4), Note("E", 4), Note("G", 4)]
    assert midi_generator_base.chord_to_notes(Chord("i")) == [Note("C", 4), Note("D#", 4), Note("G", 4)]


def test_chord_to_midi():
    assert midi_generator_base.chord_to_midi(Chord("I")) == [MIDINote(pitch=60), MIDINote(pitch=64), MIDINote(pitch=67)]
    assert midi_generator_base.chord_to_midi(Chord("i")) == [MIDINote(pitch=60), MIDINote(pitch=63), MIDINote(pitch=67)]
