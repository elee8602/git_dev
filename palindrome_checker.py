#!/usr/bin/env python3
"""
palindrome_checker.py
"""

__author__ = "Edward Lee"
__version__ = "2-22-23"

from atds import Deque

class PalindromeChecker:
    def __init__(self):
        self.strict_mode = False

    def setStrictMode(self, mode):
        if mode:
            self.strict_mode = True
        else:
            self.strict_mode = False

    def sanitize(self, phrase):
        phrase = phrase.lower()
        sanitized = ""
        for i in range(len(phrase)-1):
            if phrase[i] in 'abcdefghijklmnopqrstuvwxyz':
                sanitized += phrase[i]
        return sanitized

    def isPalindrome(self, phrase):
        sanitized_phrase = phrase
        if not self.strict_mode:
            sanitized_phrase = self.sanitize(phrase)
        d = Deque()
        for i in range(len(sanitized_phrase)):
            d.addRear(sanitized_phrase[i])
        while d.size() > 1:
            if d.removeFront() != d.removeRear():
                return False
            return True
                


def main():
    # The program code goes here!
    pc = PalindromeChecker()
    print("This is a palindrome checker!")
    mode = int(input("Do you want strict mode 1) on, or 2) off? "))
    if mode == 1:
        pc.setStrictMode("True")
    phrase = input("Phrase: ")
    if pc.isPalindrome(phrase):
        print("Is a palindrome.")
    else:
        print("Not a palindrome.")


if __name__ == "__main__":
    main()