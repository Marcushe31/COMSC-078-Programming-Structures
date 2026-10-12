# Name: Marcus Hernandez
# COMSC-078, Section 202
# Week 7 Lab (Trees and Dictionaries)
# asks for a DNA sequence over and over and prints the amino acid for each
# group of 3 letters using a dictionary, press ENTER to quit

# codon table from the assignment (*** = no amino acid)
codons = {'TTT':'Phe', 'TTC':'Phe', 'TTG':'Leu', 'TTA':'Leu',
  'TCT':'Ser','TCC':'Ser','TCG':'Ser','TCA':'Ser',
  'TGT':'Cys', 'TGC':'Cys', 'TGG':'Trp', 'TGA':'***',
  'TAT':'Tyr','TAC':'Tyr','TAG':'***','TAA':'***',
  'CTT':'Leu','CTC':'Leu','CTG':'Leu','CTA':'Leu',
  'CCT':'Pro', 'CCC':'Pro', 'CCG':'Pro', 'CCA':'Pro',
  'CGT':'Arg','CGC':'Arg','CGG':'Arg','CGA':'Arg',
  'CAT':'His','CAC':'His', 'CAG':'Gln','CAA':'Gln',
  'GTT':'Val','GTC':'Val','GTG':'Val','GTA':'Val',
  'GCT':'Ala','GCC':'Ala','GCG':'Ala','GCA':'Ala',
  'GGT':'Gly', 'GGC':'Gly', 'GGG':'Gly', 'GGA':'Gly',
  'GAT':'Asp','GAC':'Asp','GAG':'Glu','GAA':'Glu',
  'ATT':'Ile','ATC':'Ile','ATG':'Met','ATA':'Ile',
  'ACT':'Thr','ACC':'Thr', 'ACG':'Thr','ACA':'Thr',
  'AGT':'Ser','AGC':'Ser','AGG':'Arg','AGA':'Arg',
  'AAT':'Asn','AAC':'Asn','AAG':'Lys','AAA':'Lys'}

def clean_sequence(s):
    # keep only letters, make them uppercase
    out = ''
    for c in s:
        if c.isalpha():
            out += c.upper()
    return out

def main():
    line = input('Enter a nucleotide sequence, or just press ENTER to quit: ')
    while line != '':
        seq = clean_sequence(line)
        if len(seq)%3 != 0:  # leftover letters so cant split into triples
            print('Error: You must give complete triples.')
        else:
            i = 0
            while i < len(seq):
                t = seq[i:i+3]
                # not in the dict = has a letter thats not A C G or T
                print(t, codons.get(t, 'invalid sequence'))
                i += 3
        print()
        line = input('Enter a nucleotide sequence, or just press ENTER to quit: ')

main()