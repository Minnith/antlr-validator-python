import os
from antlr4 import *
from CICSParser import CICSParser
from CICSListener import CICSListener
from CICSLexer import CICSLexer

def main():   
    input_stream = InputStream(input_code.txt)
    lexer = CICSLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CICSParser(stream)
    tree = parser.cicsProgram()  # Start rule

    print("CICS code parsed successfully.")

if __name__ == '__main__':
    main()
