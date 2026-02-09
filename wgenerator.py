#!/usr/bin/env python3
# wgenerator by flandreiii

import os
import time
import random
import string
import sys

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

def clear():
    os.system("clear")

# COOL ASCII banner (100% Termux safe)
def banner():
    art = r"""
 __        __   _                                _             
 \ \      / /__| | ___ ___  _ __ ___   ___ _ __ | |_ ___  _ __ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ '_ \| __/ _ \| '__|
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | | | || (_) | |   
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|_| |_|\__\___/|_|   
                     wgenerator by flandreiii
"""
    for line in art.split("\n"):
        print(MAGENTA + line + RESET)
        time.sleep(0.02)

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def animated_menu():
    options = [
        "1) Generate a single word",
        "2) Generate multiple words (mass mode)",
        "3) Exit"
    ]
    for opt in options:
        slow_print(GREEN + opt + RESET, 0.02)

def ask_option(text):
    choice = input(YELLOW + text + " (y/n): " + RESET).strip().lower()
    return choice == "y"

def build_charset():
    slow_print(CYAN + "\n-- Choose character types --" + RESET, 0.01)

    include_lower = ask_option("Include lowercase?")
    include_upper = ask_option("Include uppercase?")
    include_digits = ask_option("Include digits?")
    include_symbols = ask_option("Include symbols?")

    charset = ""
    if include_lower:
        charset += string.ascii_lowercase
    if include_upper:
        charset += string.ascii_uppercase
    if include_digits:
        charset += string.digits
    if include_symbols:
        charset += "!@#$%^&*()-_=+<>?{}[]"

    if not charset:
        print(RED + "Error: No character types selected!" + RESET)
        sys.exit()

    return charset

def generate_word(charset, length):
    return "".join(random.choice(charset) for _ in range(length))

def main():
    while True:
        clear()
        banner()
        animated_menu()

        choice = input(YELLOW + "\nSelect option: " + RESET).strip()

        if choice == "1":
            charset = build_charset()
            length = int(input(YELLOW + "Word length: " + RESET))

            word = generate_word(charset, length)

            print(CYAN + "\nGenerated word: " + GREEN + word + RESET)
            input(CYAN + "\nPress Enter to continue..." + RESET)

        elif choice == "2":
            charset = build_charset()
            length = int(input(YELLOW + "Word length: " + RESET))
            amount = int(input(YELLOW + "How many words to generate? " + RESET))
            file_name = input(YELLOW + "Save to file: " + RESET)

            print(CYAN + "\nGenerating words..." + RESET)
            time.sleep(0.5)

            with open(file_name, "a") as f:
                for _ in range(amount):
                    w = generate_word(charset, length)
                    f.write(w + "\n")

            slow_print(GREEN + f"\nSaved {amount} words to {file_name}" + RESET, 0.01)
            input(CYAN + "\nPress Enter to continue..." + RESET)

        elif choice == "3":
            slow_print(GREEN + "Goodbye!" + RESET, 0.02)
            break

        else:
            print(RED + "Invalid choice!" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()
