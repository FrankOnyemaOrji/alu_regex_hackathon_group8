#!/usr/bin/env python3
import re

episode_pattern = re.compile(r"[a-zA-z]+ S[0-9]{2}E[0-9]{2}: .+")
def find_episodes(string):
    episodes = episodes_pattern.findall(string)
    if episodes:
        return 'Episode title(s) found: ' + ', '.join(episodes)
    else:
        return 'No episode title found.'
