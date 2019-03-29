text = input('Enter string to find frequency, or nothing to use default: ')

if text == '':
    text = 'The first known recorded explanation of frequency analysis (indeed, of any kind of cryptanalysis) was given in the 9th century by Al-Kindi, an Arab polymath, in A Manuscript on Deciphering Cryptographic Messages.[3] It has been suggested that close textual study of the Quran first brought to light that Arabic has a characteristic letter frequency.[4] Its use spread, and similar systems were widely used in European states by the time of the Renaissance. By 1474, Cicco Simonetta had written a manual on deciphering encryptions of Latin and Italian text.[5] Arabic Letter Frequency and a detailed study of letter and word frequency analysis of the entire book of Quran are provided by Intellaren Articles.[6] Several schemes were invented by cryptographers to defeat this weakness in simple substitution encryptions. These included: Homophonic substitution: Use of homophones — several alternatives to the most common letters in otherwise monoalphabetic substitution ciphers. For example, for English, both X and Y ciphertext might mean plaintext E. Polyalphabetic substitution, that is, the use of several alphabets — chosen in assorted, more or less devious, ways (Leone Alberti seems to have been the first to propose this); and Polygraphic substitution, schemes where pairs or triplets of plaintext letters are treated as units for substitution, rather than single letters, for example, the Playfair cipher invented by Charles Wheatstone in the mid-19th century. A disadvantage of all these attempts to defeat frequency counting attacks is that it increases complication of both enciphering and deciphering, leading to mistakes. Famously, a British Foreign Secretary is said to have rejected the Playfair cipher because, even if school boys could cope successfully as Wheatstone and Playfair had shown, "our attachés could never learn it!". The rotor machines of the first half of the 20th century (for example, the Enigma machine) were essentially immune to straightforward frequency analysis. However, other kinds of analysis ("attacks") successfully decoded messages from some of those machines. Letter frequencies in Spanish. Frequency analysis requires only a basic understanding of the statistics of the plaintext language and some problem solving skills, and, if performed by hand, tolerance for extensive letter bookkeeping. During World War II (WWII), both the British and the Americans recruited codebreakers by placing crossword puzzles in major newspapers and running contests for who could solve them the fastest. Several of the ciphers used by the Axis powers were breakable using frequency analysis, for example, some of the consular ciphers used by the Japanese. Mechanical methods of letter counting and statistical analysis (generally IBM card type machinery) were first used in World War II, possibly by the US Armys SIS. Today, the hard work of letter counting and analysis has been replaced by computer software, which can carry out such analysis in seconds. With modern computing power, classical ciphers are unlikely to provide any real protection for confidential data.'

characters = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

text = text.lower()

for c in text.strip():
    if c in  characters:
        characters[c] += 1

for key, value in sorted(characters.items()):
    print(str(key) + ' : ' + str(value))