#!/usr/bin/env python3
"""
Higher-Lower Game
Author: brainiacweb-tech
"""
import random

CELEBRITIES = [
    ("Cristiano Ronaldo", 620_000_000),
    ("Justin Bieber", 285_000_000),
    ("Kylie Jenner", 399_000_000),
    ("Selena Gomez", 425_000_000),
    ("Dwayne Johnson", 389_000_000),
    ("Ariana Grande", 380_000_000),
    ("Lionel Messi", 500_000_000),
    ("Kim Kardashian", 364_000_000),
    ("Taylor Swift", 282_000_000),
    ("Beyonce", 319_000_000),
]

def play():
    score = 0
    pool = CELEBRITIES[:]
    random.shuffle(pool)
    print("\nHigher or Lower — Instagram Followers Edition!\n")
    current = pool.pop()
    while pool:
        challenger = pool.pop()
        print(f"A: {current[0]} — {current[1]:,} followers")
        print(f"B: {challenger[0]}")
        answer = input("Does B have (h)igher or (l)ower followers? ").strip().lower()
        if answer not in ('h','l'): continue
        correct = (answer=='h' and challenger[1]>current[1]) or (answer=='l' and challenger[1]<current[1])
        if correct:
            print(f"Correct! {challenger[0]} has {challenger[1]:,} followers.\n")
            score += 1
            current = challenger
        else:
            print(f"Wrong! {challenger[0]} has {challenger[1]:,} followers.")
            print(f"Game over! Score: {score}"); return
    print(f"You beat the game! Final score: {score}")

if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != 'y':
            break
