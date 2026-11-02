#!/usr/bin/env python3
"""
Simple menu launcher for the six AI practicals.

Run from anywhere:
    python3 RUN_PRACTICAL.py

The launcher uses the same Python interpreter that started it, so the
programs work on Ubuntu even if the default python is Python 3.x.
"""

import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

PRACTICALS = {
    "1": ("DFS and BFS", "Practical_1_DFS_BFS/code/main.py"),
    "2": ("A* for 8-puzzle", "Practical_2_A_Star_8_Puzzle/code/main.py"),
    "3": ("Selection sort + Job scheduling", "Practical_3_Greedy_Search/code/main.py"),
    "4": ("N-Queens", "Practical_4_N_Queens/code/main.py"),
    "5": ("Restaurant chatbot", "Practical_5_Chatbot/code/main.py"),
    "6": ("Medical expert system", "Practical_6_Expert_System/code/main.py"),
}


def show_menu():
    print("\n" + "=" * 58)
    print(" AI PRACTICAL LAUNCHER")
    print("=" * 58)
    for key in sorted(PRACTICALS):
        name, path = PRACTICALS[key]
        print(f" {key}. {name}")
    print(" 7. Investment chatbot (Practical 5 handout version)")
    print(" 0. Exit")
    print("=" * 58)


def main():
    while True:
        show_menu()
        choice = input("Choose a practical (0-7): ").strip()

        if choice == "0":
            print("Bye.")
            break

        if choice == "7":
            script = os.path.join(
                BASE, "Practical_5_Chatbot", "code", "investment_chatbot.py"
            )
        elif choice in PRACTICALS:
            script = os.path.join(BASE, PRACTICALS[choice][1])
        else:
            print("Please choose a number from 0 to 7.")
            continue

        if not os.path.exists(script):
            print("File not found:", script)
            continue

        print("\nRunning:", script)
        print("(Use the sample input from DO_THIS_FIRST.txt. Press Ctrl+C to stop.)\n")

        try:
            subprocess.run([sys.executable, script], check=False)
        except KeyboardInterrupt:
            print("\nStopped.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
