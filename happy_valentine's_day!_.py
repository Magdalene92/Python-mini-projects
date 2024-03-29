# -*- coding: utf-8 -*-
"""Happy Valentine's day! .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S4MnhK_01Syba1XzBFmoLd0R6ynNbhvg
"""

import random

def generate_valentine_message():
    messages = [
        "You are the key to my heart.",
        "Roses are red, violets are blue, sugar is sweet, and so are you.",
        "Love is not just looking at each other, it's looking in the same direction.",
        "You make my heart skip a beat.",
        "You are the peanut butter to my jelly.",
        "I love you more than words can express.",
        "Every love story is beautiful, but ours is my favorite.",
        "You complete me.",
        "You are the sunshine in my life.",
        "I'm so grateful to have you in my life.",
    ]

    return random.choice(messages)

if __name__ == "__main__":
    valentine_message = generate_valentine_message()
    print("Happy Valentine's Day!")
    print(valentine_message)