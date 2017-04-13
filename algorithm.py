#final code for product identifier
import shlex
import re
import mmap
from collections import Counter
global alphabet
global data
global temp


def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('ViserDictionary.txt').read()))

#print WORDS
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890..@'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# juke Ganior GARNIeR SHAMPOO fuit nautritron NAUTRITRON trpL elch Spidr Mthatry Atrian
# Weichs Welctrs GARNIER SHAMPOO Frult Ols FRUCTIS TRIPLE NUTRITIANT NUTRITHON
# Weichs Welctrs GARNIER SHAMPOO Frult Ols MHorton FRUCTIS TRIPLE NUTRITIANT NUTRITHON
# Bath rk IMOONI Rn16 LIGHT PATH SH
# Weichs Welctrs GARNIER SHAMPOO Frult Ols MHorton FRUCTIS TRIPLE NUTRITIANT NUTRITHON
# GARNIoR SHaMPO Frult FCTIS TRILE NUTRITIANT REY VODKA RANCE
# cORE 3 GARNICR fortifying shampod LFrut ols FRUCT TRIPLE mutrition
# GARNIOR Dry, Damaged Hair 25.4 FL OZ 050n FRUCTiS TRIPLE NUTRITION
# GARNIOR  ShampAo Nutro para un c Dry, Damaged Hair 25.4 FL OZ 050n FRUCTiS TRIPLE NUTRITION


productName = " "
temp = shlex.split("GARNIOR  ShampAo nupre dke Dry, Damaged Hair 25.4 FL OZ 050n FRUCTiS TRIPLE NUTRITION")
print temp
print type(temp) is list
for item in temp:
    item = item.lower()
    if(str(correction(item))) not in productName:
        productName += "  "+ str(correction(item))
if(len(productName)):
    print productName
    finalBrand = shlex.split(productName)
    with open('BrandName.txt', 'r') as searchfile:
        for line in searchfile:
            for brand in  finalBrand:
                if brand in line:
                    #print brand
                    postBrand = brand
                    print "Brand Name " + postBrand
    #finalBrand = shlex.split(productName)
    with open('ProductType.txt', 'r') as typefile:
        for listtype in typefile:
            for productType in  finalBrand:
                if productType in listtype:
                    postType = productType
                    print "Product Type " + postType
    tagline = " "
    with open('TagLine.txt', 'r') as tagfile:
        for tag in tagfile:
            for tagType in  finalBrand:
                if tagType in tag:
                    tagline = tagline + " " + tagType
        
        print "Tag Type " + tagline