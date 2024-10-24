from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    TODO: The main function
    """
    # Create instance of FastaParser
    aparser = FastaParser('data/test.fa')

    # Create instance of FastqParser
    qparser=FastqParser('data/test.fq')
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for header, sequence in aparser:
        print(header)
        print(transcribe(sequence))
        print("part1")
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for header, sequence, quality in qparser:
        print(header)
        print(transcribe(sequence))
        print("part2")


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for header,sequence in aparser:
        print(header)
        print(reverse_transcribe(sequence))
        print("part3")
    
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console

    for header,sequence,quality in qparser:
        print(header)
        print(reverse_transcribe(sequence))
        print("part4")

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
