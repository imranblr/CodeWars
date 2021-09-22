def DNA_strand(dna):
    _size=len(dna)
    _code=list(dna)
    for i in range(_size):
        if dna[i]=="A":_code[i]='T'
        elif dna[i]=="T":_code[i]='A'
        elif dna[i]=="G":_code[i]='C'
        elif dna[i]=="C":_code[i]='G'
    return str("".join(_code))