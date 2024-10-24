from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    TODO: The main function
    """
    
    aparser = FastaParser('data/test.fa')# Create instance of FastaParser

    
    qparser=FastqParser('data/test.fq')# Create instance of FastqParser
        
  
    for header, sequence in aparser: #go through evrything in aparser, print out the header, print out the transcribed sequence, and print out "aparser_transcribe"
        print(header)
        print(transcribe(sequence))
        print("aparser_transcribe")
       

    for header, sequence, quality in qparser:#go through evrything in qparser, print out the header, print out the transcribed sequence, and print out "qparser_transcribe"
        print(header)
        print(transcribe(sequence))
        print("qparser_transcribe")



    for header,sequence in aparser:#go through evrything in aparser, print out the header, print out the reversed transcribed sequence, and print out "aparser_reverse_transcribe"
        print(header)
        print(reverse_transcribe(sequence))
        print("aparser_reverse_transcribe")
    

    for header,sequence,quality in qparser:#go through evrything in qparser, print out the header, print out the reversed transcribed sequence, and print out "qparser_reverse_transcribe"
        print(header)
        print(reverse_transcribe(sequence))
        print("qparser_reverse_transcribe")

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
