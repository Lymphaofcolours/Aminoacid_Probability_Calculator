
from Bio.Data import CodonTable
from Bio.Data import IUPACData
# Bio.Alphabet is no longer continued

target_select = [
    'Standard', #1
    'Vertebrate Mitochondrial', #2
    'Yeast Mitochondrial', #3
    'Mold Mitochondrial', 'Protozoan Mitochondrial', 'Coelenterate Mitochondrial', 'Mycoplasma', 'Spiroplasma', #4 Same Codon Tables
    'Invertebrate Mitochondrial', #5
    'Ciliate Nuclear', 'Dasycladacean Nuclear', 'Hexamita Nuclear', #6 Same Codon Tables
    'Echinoderm Mitochondrial', 'Flatworm Mitochondrial', #7 Same Codon Tables
    'Euplotid Nuclear', #8
    'Bacterial', 'Archaeal', 'Plant Plastid', #9 Same Codon Tables
    'Alternative Yeast Nuclear', #10
    'Ascidian Mitochondrial', #11
    'Alternative Flatworm Mitochondrial', #12
    'Blepharisma Macronuclear', #13
    'Chlorophycean Mitochondrial', #14
    'Trematode Mitochondrial', #15
    'Scenedesmus obliquus Mitochondrial', #16
    'Thraustochytrium Mitochondrial', #17
    'Pterobranchia Mitochondrial', #18
    'Candidate Division SR1', 'Gracilibacteria', #19 Same Codon Tables
    'Pachysolen tannophilus Nuclear', #20
    'Karyorelict Nuclear', #21
    'Condylostoma Nuclear', #22
    'Mesodinium Nuclear', #23
    'Peritrich Nuclear', #24
    'Blastocrithidia Nuclear', #25
    'Balanophoraceae Plastid', #26
    'Cephalodiscidae Mitochondrial' #27
               ]

def user_input_selection():
    print('Select Table Number:')
    for index, content in enumerate(target_select):
        print(f'[{index}] {content}')
user_input_selection()

def user_selection(s=input(('Table Number:'))):
    try:
        s = int(s)
        if s <= len(target_select):
            return s
        else:
            print('Wrong Number. Try Again:')
            return user_selection(s=input(('Table Number:')))
    except ValueError:
        print('Wrong Input. Try Again')
        return user_selection(s=input(('Table Number:')))
selection = user_selection()


class Protein_Dictionary:
    def __init__(self):
        self._codon_dict = CodonTable.unambiguous_dna_by_name[target_select[selection]].forward_table
        self._amino_string = list(self._codon_dict.values())

    def __str__(self):
        return f'Codon Table'

    def probabilities(self):
        for i in self._amino_letters:
            amino_count = self._amino_string.count(i)
            amino_prob = int(amino_count) / 64
            print(f'{i}({self._amino_words[i]}) probability is {round(amino_prob, 4)} ({amino_count}/64)')

class Normal_IUPAC_Dictionary(Protein_Dictionary):
    _amino_letters = IUPACData.protein_letters
    _amino_words = IUPACData.protein_letters_1to3

class Extended_IUPAC_Dictionary(Protein_Dictionary):
    _amino_letters = IUPACData.extended_protein_letters
    _amino_words = IUPACData.protein_letters_1to3_extended


normal_instance = Normal_IUPAC_Dictionary()
def print_normal_dict():
    print(f'REGULAR AMINOACID PROBABILITIES FOR {target_select[selection].upper()}')
    print('========================================================')
    return normal_instance.probabilities()

extended_instance = Extended_IUPAC_Dictionary()
def print_extended_dict():
    print(f'EXTENDED AMINOOACID PROBABILITIES FOR {target_select[selection].upper()}')
    print('========================================================')
    return extended_instance.probabilities()


print_normal_dict()
print('')
print_extended_dict()

