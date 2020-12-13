# Introduction

For now, this is very early development - just a proof of concept while I work on developing it further.

# What this does

This script tells you how much gold you'd need to spend right now to buy all BFA reputation mounts you are currently eligible for.

# How to make API calls work for you

1. Get a client id and client secret from Blizzard. Go to https://develop.battle.net.

2. Rename ```.env-sample``` to ```.env``` and put your id and secret in it.

3. Modify the u_ variables to match your own character.

4. Run get.py

5. Sample output:
```
You have already met the reputation requirements to get one or more mounts you don't have.

To get all eligible mounts right now would cost you 814,538 gold.
```
