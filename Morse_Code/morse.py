#!/usr/bin/env python
# Script for generating Morse Code (https://thecodeaddict.wordpress.com/2012/06/18/morse_code/)

def set_code(ch) :
        ch = ch.lower()
        dict = {'a': '.-',
                'b': '-...',
                'c': '-.-.',
                'd': '-..',
                'e': '.',
                'f': '..-.',
                'g': '--.',
                'h': '....',
                'i': '..',
                'j': '.---',
                'k': '-.-',
                'l': '.-..',
                'm': '--',
                'n': '-.',
                'o': '---',
                'p': '.--.',
                'q': '--.-',
                'r': '.-.',
                's': '...',
                't': '-',
                'u': '..-',
                'v': '...-',
                'w': '.--',
                'x': '-..-',
                'y': '-.--',
                'z': '--..',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                '0': '-----',
                '.': '.-.-.-',
                ',': '--..--',
                '?': '..--..',
                '\'': '.----.',
                '!': '-.-.--',
                '/': '-..-.',
                '(': '-.--.',
                ')': '-.--.-',
                '&': '.-...',
                ':': '---...',
                ';': '-.-.-.',
                '=': '-...-',
                '+': '.-.-.',
                '-': '-....-',
                '_': '..--.-',
                '\"': '.-..-.',
                '$': '...-..-',
                '@': '.--.-.',
                ' ': ' '
                }
        return dict[ch]

def morse_code(english) :
        code = []
        for i in english:
                code.append(set_code(i))
        return code

def dit_dah() :
        input_string = input()
        result_string = ""
        for i in input_string:
                result_string += morse_code(i)[0] + '   '
        return result_string[:-1]

def return_audio(string) :
        audio_result = ""
        bell = '\a'
        for i in string:
                for j in i:
                        if j == '.': audio_result += bell+' '
                        elif j == '-': audio_result += bell+' '+bell+' '+bell+' '
                        elif j == ' ': audio_result+='      '
        print(audio_result[:-1])

def main():
        ip = dit_dah()  # get input text and convert to Morse code
        print(ip)       # return Morse code in dots and dashes
        return_audio(ip)# return audio result of the input text

if __name__ == "__main__": main()