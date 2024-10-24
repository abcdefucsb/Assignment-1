# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    result=""
    for char in seq:
        if char=="T":
            result += str("A")
        elif char=="A":
            result += str("U")
        elif char=="C":
            result += str("G")
        elif char=="G":
            result += str("C")
    return result.strip()
    


def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    RNA=transcribe(seq)
    result=""
    for char in RNA:
        result= char + result
    return result.strip()

    
