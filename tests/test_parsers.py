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

    #positive unit tests
    for result in FastaParser('data/test.fa'):#go though everything in test.fa
        (header,sequence)=result#unpack the tuple
        assert type(result)==tuple#check types
        assert type(sequence)==str
        assert type(header)==str
        if header=="seq99":#in header seq99, check if the sequence is "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA"
            assert "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA"==sequence
        if header=="seq98":#in header seq98, check if the sequence is "CGAGCGAGAAACGCGCTAACTAGCAACCGGAACAACAATGCTGGGTTGAATTTGATTCGCACCCGACGATCACTAGAGAGTTTATCTGGGACTCCGGGAC"
            assert "CGAGCGAGAAACGCGCTAACTAGCAACCGGAACAACAATGCTGGGTTGAATTTGATTCGCACCCGACGATCACTAGAGAGTTTATCTGGGACTCCGGGAC"==sequence
    #negative unit tests
    for header,sequence in FastaParser('data/1.txt'):#go though everything in 1.txt
        pass
        #you should see warnings 
        

    
def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    #positive unit tests
    for result in FastqParser('data/test.fq'):#go though everything in test.fq
        (header,sequence,quality)=result#unpack the tuple
        assert type(result)==tuple#check types
        assert type(sequence)==str
        assert type(header)==str
        assert type(quality)==str
        if header=="seq99":#in header seq99, check if the sequence is "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG"
            assert "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG"==sequence
        if header=="seq98":#in header seq98, check if the sequence is "AACCTGCCCGTAGCCTTTAGGTAGCCCGTCTACATGTCCTCCAGTACAGTGGAAGCTCCTACATCAACTGATCAAATAACATCGCAGCACTATATGTCAC"
            assert "AACCTGCCCGTAGCCTTTAGGTAGCCCGTCTACATGTCCTCCAGTACAGTGGAAGCTCCTACATCAACTGATCAAATAACATCGCAGCACTATATGTCAC"==sequence
    #negative unit tests
    for header,sequence,quality in FastaParser('data/2.txt'):#go though everything in 2.txt
        pass
        #you should see warnings 