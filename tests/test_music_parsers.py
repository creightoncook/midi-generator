#!/usr/bin/env python
"""Tests for `midi_generator` music_parsers."""
import pytest
from midi_generator.music_parsers import *


def test_parse_notes():
    assert parse_note("C") == Note("C")
    assert parse_note("A2") == Note("A", 2)
    assert parse_note("D#5") == Note("D#", 5)
    with pytest.raises(UnsupportedNotation):
        parse_note("Not notation")
    with pytest.raises(UnsupportedNotation):
        parse_note("B&3")


def test_parse_chord():
    assert parse_chord("I") == Chord("I")
    assert parse_chord("vi") == Chord("vi")
    with pytest.raises(UnsupportedNotation):
        parse_chord("viii")


def test_parse_chord_progression():
    assert parse_chord_progression("ii-IV-V") == [Chord("ii"), Chord("IV"), Chord("V")]
    with pytest.raises(UnsupportedNotation):
        parse_chord_progression("V ii I vi")
