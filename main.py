# Author: Md. Rashedul Alam Anik
# University of Chittagong
#
# This is a simple implementation of enigma machine

import sys


def initialize():
    alphabets = []
    rotor1 = []
    rotor2 = []
    rotor3 = []
    alphabets[:0] = "abcdefghijklmnopqrstuvwxyz"
    rotor1[:0] = "dmtwsilruyqnkfejcazbpgxohv"
    rotor2[:0] = "hqzgpjtmoblncifdyawveusrkx"
    rotor3[:0] = "uqntlszfmrehdpxkibvygjcwoa"
    reflector = {'a': 'y', 'b': 'r', 'c': 'u', 'd': 'h', 'e': 'q', 'f': 's', 'g': 'l', 'i': 'p', 'j': 'x', 'k': 'n', 'm': 'o', 't': 'z', 'v': 'w',
                 'y': 'a', 'r': 'b', 'u': 'c', 'h': 'd', 'q': 'e', 's': 'f', 'l': 'g', 'p': 'i', 'x': 'j', 'n': 'k', 'o': 'm', 'z': 't', 'w': 'v'}

    return alphabets, rotor1, rotor2, rotor3, reflector


def getSettingsInput():
    settings = input(
        "Insert the 3 letter settings (in lower case letter only): ")

    settings = settings.lower()

    # quick check for any unnecessary letters
    for ch in settings:
        if ch < 'a' or ch > 'z':
            sys.exit()

    return settings


def getIndexesInRotor(settings, rotor1, rotor2, rotor3):
    index1 = rotor1.index(settings[0])
    index2 = rotor2.index(settings[1])
    index3 = rotor3.index(settings[2])

    return index1, index2, index3


def setRotorInConfiguredPosition(rotor1, rotor2, rotor3, index1=0, index2=0, index3=0):
    rotor1 = rotor1[index1:] + rotor1[:index1]
    rotor2 = rotor2[index2:] + rotor2[:index2]
    rotor3 = rotor3[index3:] + rotor3[:index3]


def getEncryptedOrDecryptedMessage(message, alphabets, rotor1, rotor2, rotor3, reflector):
    index1 = 0
    index2 = 0
    index3 = 0

    output_message = ""

    for ch in message:
        if ch < 'a' or ch > 'z':
            output_message += ch
            continue

        newch1 = rotor1[alphabets.index(ch)]
        newch1 = rotor2[alphabets.index(newch1)]
        newch1 = rotor3[alphabets.index(newch1)]

        newch2 = reflector[newch1]
        newch2 = alphabets[rotor3.index(newch2)]
        newch2 = alphabets[rotor2.index(newch2)]
        newch2 = alphabets[rotor1.index(newch2)]

        output_message += newch2

        index1 = (index1 + 1) % 26
        rotor1 = rotor1[1:] + rotor1[:1]

        if index1 == 0:
            index2 = (index2 + 1) % 26
            rotor2 = rotor2[1:] + rotor2[:1]

            if index2 == 0:
                index3 = (index3 + 1) % 26
                rotor3 = rotor3[1:] + rotor3[:1]

    return output_message


def main():
    alphabets, rotor1, rotor2, rotor3, reflector = initialize()

    settings = getSettingsInput()

    index1, index2, index3 = getIndexesInRotor(
        settings, rotor1, rotor2, rotor3)

    setRotorInConfiguredPosition(
        rotor1, rotor2, rotor3, index1, index2, index3)

    message = input("Enter message in lower case english letter only: ")

    message = message.lower()

    encrypted_message = getEncryptedOrDecryptedMessage(
        message, alphabets, rotor1, rotor2, rotor3, reflector)

    print("The encrypted message is:", encrypted_message)

    setRotorInConfiguredPosition(
        rotor1, rotor2, rotor3, index1, index2, index3)

    decrypted_message = getEncryptedOrDecryptedMessage(
        encrypted_message, alphabets, rotor1, rotor2, rotor3, reflector)

    print("The decrypted message is:", decrypted_message)


if __name__ == "__main__":
    main()
