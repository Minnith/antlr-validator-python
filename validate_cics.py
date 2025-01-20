import os
from antlr4 import *
from CICSParser import CICSParser
from CICSListener import CICSListener
from CICSLexer import CICSLexer

def main():
    # Sample CICS code to be validated
    input_code = """
    IDENTIFICATION DIVISION.
    PROGRAM-ID. SampleCICSProgram.
    AUTHOR. John Doe.
    INSTALLATION. ExampleCorp.
    DATE-WRITTEN. October 2023.
    REMARKS. This is a sample CICS program for testing.
    ENVIRONMENT DIVISION.
    CONFIGURATION SECTION.
    SOURCE-COMPUTER. IBM-370.
    OBJECT-COMPUTER. IBM-370.
    DATA DIVISION.
    FILE SECTION.
    FD  CUSTOMER-FILE.
    01  CUSTOMER-RECORD.
        05  CUSTOMER-ID    PIC 9(5).
        05  CUSTOMER-NAME  PIC X(20).
    WORKING-STORAGE SECTION.
    01  WS-VARIABLES.
        05 WS-CUSTOMER-ID    PIC 9(5).
        05 WS-CUSTOMER-NAME  PIC X(20).
        05 WS-TRANS-NAME     PIC X(8).
    LINKAGE SECTION.
    01  LK-VARIABLES.
        05 LK-ITEM           PIC X(10).
    SQLCA SECTION.
    EXEC SQL INCLUDE SQLCA END-EXEC.
    PROCEDURE DIVISION.
    MAIN-PARA.
        EXEC CICS HANDLE ABEND
            PROGRAM('ABEND-PROGRAM')
        END-EXEC.
        EXEC CICS XCTL
            PROGRAM('ANOTHER-PROGRAM')
        END-EXEC.
        EXEC CICS LINK
            PROGRAM('LINK-PROGRAM')
        END-EXEC.
        PERFORM READ-CUSTOMER-FILE.
        IF WS-CUSTOMER-ID = 12345 THEN
            DISPLAY 'Customer Found'
        ELSE
            DISPLAY 'Customer Not Found'
        END-IF.
        EXEC SQL
            COMMIT
        END-EXEC.
        EXEC CICS RETURN END-EXEC.
    READ-CUSTOMER-FILE.
        OPEN INPUT CUSTOMER-FILE.
        READ CUSTOMER-FILE INTO WS-CUSTOMER-NAME
            AT END
                DISPLAY 'End of File'
        END-READ.
        CLOSE CUSTOMER-FILE.
    EVALUATE WS-TRANS-NAME
        WHEN 'INQUIRE'
            DISPLAY 'Inquire Transaction'
        WHEN 'UPDATE'
            DISPLAY 'Update Transaction'
        WHEN OTHER
            DISPLAY 'Unknown Transaction'
    END-EVALUATE.
    GOBACK.
    """

    input_stream = InputStream(input_code)
    lexer = CICSLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CICSParser(stream)
    tree = parser.cicsProgram()  # Start rule

    print("CICS code parsed successfully.")

if __name__ == '__main__':
    main()
