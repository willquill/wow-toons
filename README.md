# Introduction

For now, this is very early development - just a proof of concept while I work on developing it further.

# What this does

Eventually, this will be a website that lets you enter a region, realm, and character name from World of Warcraft. It will return data about reputation mounts to the user, letting them know which mounts they can buy with reputation, and how close they are to hitting the required reputation.

`build_server_lists.py` is meant to be run once in awhile, only after game data has actually changed. It builds local JSON files that reside on the server.

`build_client_lists.py` contains operations meant to be run after a user inputs their region, realm, and character. It references the local JSON files to return data to the user about which reputation mounts they don't have yet and what they need to get those mounts.

# How to make API calls work for you

1. Get a client id and client secret from Blizzard. Go to https://develop.battle.net.

2. Rename `.env-sample` to `.env` and put your id and secret in it.

3. Modify the u\_ variables to match your own character.

4. Run build_server_list.py

5. I need to develop build_client_lists.py further
