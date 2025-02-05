# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)
from seqparser import (
        FastaParser,
        FastqParser)

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """

    for result in FastaParser('data/test.fa'):#go though everything in test.fa
        (header,sequence)=result#unpack the tuple
        assert type(result)==tuple#check types
        assert type(sequence)==str
        assert type(header)==str
        if header=="seq99":#in header seq99, check if the transcribed sequence is "GUUUGGCCGCUACGCCCAUGAGGGAUGUUCAACCUGAGGCGUCGCUUGCGGCGUCCCCGGUAAUAUGCCGCCAGAACCGCCGCAGCUGGUCCGGCCAGGU"
            assert "GUUUGGCCGCUACGCCCAUGAGGGAUGUUCAACCUGAGGCGUCGCUUGCGGCGUCCCCGGUAAUAUGCCGCCAGAACCGCCGCAGCUGGUCCGGCCAGGU"==transcribe(sequence)
        if header=="seq98":#in header seq98, check if the transcribed sequence is "GCUCGCUCUUUGCGCGAUUGAUCGUUGGCCUUGUUGUUACGACCCAACUUAAACUAAGCGUGGGCUGCUAGUGAUCUCUCAAAUAGACCCUGAGGCCCUG"
            assert "GCUCGCUCUUUGCGCGAUUGAUCGUUGGCCUUGUUGUUACGACCCAACUUAAACUAAGCGUGGGCUGCUAGUGAUCUCUCAAAUAGACCCUGAGGCCCUG"==transcribe(sequence)

    
    for result in FastqParser('data/test.fq'):#go though everything in test.fq
        (header,sequence,quality)=result#unpack the tuple
        assert type(result)==tuple#check types
        assert type(sequence)==str
        assert type(header)==str
        assert type(quality)==str
        if header=="seq99":#in header seq99, check if the transcribed sequence is "GGCUCAAAACAUCACCCGAGUUGACUUUAGGAUAAGAAUCUGCUAACCAGUAUUUUGGGAAAGUGACAUGCCUGCAUCUGGGACGAGGCAGAAGGUCGUC"
            assert "GGCUCAAAACAUCACCCGAGUUGACUUUAGGAUAAGAAUCUGCUAACCAGUAUUUUGGGAAAGUGACAUGCCUGCAUCUGGGACGAGGCAGAAGGUCGUC"==transcribe(sequence)
        if header=="seq98":#in header seq98, check if the transcribed sequence is "UUGGACGGGCAUCGGAAAUCCAUCGGGCAGAUGUACAGGAGGUCAUGUCACCUUCGAGGAUGUAGUUGACUAGUUUAUUGUAGCGUCGUGAUAUACAGUG"
            assert "UUGGACGGGCAUCGGAAAUCCAUCGGGCAGAUGUACAGGAGGUCAUGUCACCUUCGAGGAUGUAGUUGACUAGUUUAUUGUAGCGUCGUGAUAUACAGUG"==transcribe(sequence)

def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    reverse transcribe function here.
    """
    for result in FastaParser('data/test.fa'):#go though everything in test.fa
        (header,sequence)=result#unpack the tuple
        assert type(result)==tuple#check types
        assert type(sequence)==str
        assert type(header)==str
        if header=="seq99":#in header seq99, check if the reversed transcribed sequence is "UGGACCGGCCUGGUCGACGCCGCCAAGACCGCCGUAUAAUGGCCCCUGCGGCGUUCGCUGCGGAGUCCAACUUGUAGGGAGUACCCGCAUCGCCGGUUUG"
            assert "UGGACCGGCCUGGUCGACGCCGCCAAGACCGCCGUAUAAUGGCCCCUGCGGCGUUCGCUGCGGAGUCCAACUUGUAGGGAGUACCCGCAUCGCCGGUUUG"==reverse_transcribe(sequence)
        if header=="seq98":#in header seq98, check if the reversed transcribed sequence is "GUCCCGGAGUCCCAGAUAAACUCUCUAGUGAUCGUCGGGUGCGAAUCAAAUUCAACCCAGCAUUGUUGUUCCGGUUGCUAGUUAGCGCGUUUCUCGCUCG"
            assert "GUCCCGGAGUCCCAGAUAAACUCUCUAGUGAUCGUCGGGUGCGAAUCAAAUUCAACCCAGCAUUGUUGUUCCGGUUGCUAGUUAGCGCGUUUCUCGCUCG"==reverse_transcribe(sequence)

    
    for result in FastqParser('data/test.fq'):#go though everything in test.fq
        (header,sequence,quality)=result#unpack the tuple
        assert type(result)==tuple#check types
        assert type(sequence)==str
        assert type(header)==str
        assert type(quality)==str
        if header=="seq99":#in header seq99, check if the reversed transcribed sequence is "CUGCUGGAAGACGGAGCAGGGUCUACGUCCGUACAGUGAAAGGGUUUUAUGACCAAUCGUCUAAGAAUAGGAUUUCAGUUGAGCCCACUACAAAACUCGG"
            assert "CUGCUGGAAGACGGAGCAGGGUCUACGUCCGUACAGUGAAAGGGUUUUAUGACCAAUCGUCUAAGAAUAGGAUUUCAGUUGAGCCCACUACAAAACUCGG"==reverse_transcribe(sequence)
        if header=="seq98":#in header seq98, check if the reversed transcribed sequence is "GUGACAUAUAGUGCUGCGAUGUUAUUUGAUCAGUUGAUGUAGGAGCUUCCACUGUACUGGAGGACAUGUAGACGGGCUACCUAAAGGCUACGGGCAGGUU"
            assert "GUGACAUAUAGUGCUGCGAUGUUAUUUGAUCAGUUGAUGUAGGAGCUUCCACUGUACUGGAGGACAUGUAGACGGGCUACCUAAAGGCUACGGGCAGGUU"==reverse_transcribe(sequence)
    
#I don't think it is necessary to write negative unit tests for transcribe and reverse_transcribe functions. Based on main.py, these two functions are dependent are parsing functions. If parsing functions raise warnings (in reality, an error will be raised), no surther step should be taken. Since negative unit tests have been written for parse functions, maybe doing so will be redundant for these two functions. 