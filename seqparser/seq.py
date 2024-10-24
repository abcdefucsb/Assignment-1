# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    result=""#initiate result with an empty string
    for char in seq: #go through every character in the sequence
        if char=="T":#transcribe them accordingly
            result += str("A")
        elif char=="A":
            result += str("U")
        elif char=="C":
            result += str("G")
        elif char=="G":
            result += str("C")
    return result.strip()#return the result
    


def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    RNA=transcribe(seq)#initate RNA to the transcribed seq
    result=""#initiate result with an empty string
    for char in RNA:#go through every character in RNA
        result= char + result#reverse RNA
    return result.strip()#return the result

    
