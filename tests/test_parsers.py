# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)





def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    TODO: Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    #pass
    for header,sequence in FastaParser('data/test.fa'):
        if header=="seq99":
            assert "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA"==sequence
        if header=="seq98":
            assert "CGAGCGAGAAACGCGCTAACTAGCAACCGGAACAACAATGCTGGGTTGAATTTGATTCGCACCCGACGATCACTAGAGAGTTTATCTGGGACTCCGGGAC"==sequence
    
    
def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    for header, sequence, quality in FastqParser('data/test.fq'):
        if header=="seq99":
            assert "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG"==sequence
        if header=="seq98":
            assert "AACCTGCCCGTAGCCTTTAGGTAGCCCGTCTACATGTCCTCCAGTACAGTGGAAGCTCCTACATCAACTGATCAAATAACATCGCAGCACTATATGTCAC"==sequence
    #pass
