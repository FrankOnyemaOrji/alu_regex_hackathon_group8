#!/usr/bin/python3
import re
song_lyrics = re.compile(r'[Verse\s\d+]\s(.*)')

song_lyrics_search = input("Enter text>> ")
song_lyrics_match = song_lyrics.search(song_lyrics_search)
print(song_lyrics_match)

song_lyrics_matches = song_lyrics.finditer(song_lyrics_search)

for song_lyrics_match in song_lyrics_matches:
    print(f"Your song lyrics found are {song_lyrics_match.group()}")