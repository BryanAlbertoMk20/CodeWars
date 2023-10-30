def dna_to_rna(dna):
    if "T" in dna:
        rna = dna.replace("T", "U")
        return rna
    else:
        return dna


print(dna_to_rna("TTTT"))
print(dna_to_rna("GCAT"))
print(dna_to_rna("GACCGCCGCC"))
