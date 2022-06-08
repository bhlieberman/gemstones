import unicodedata

DESCRIPTIONS = ['HEBREW LETTER ' + letter for letter in ['ALEF', 'BET', 'GIMEL', 'DALET', 'HE', 'VAV', 'ZAYIN', 'HET', 'TET', 'YOD', 'FINAL KAF', 'KAF', 'LAMED', 'FINAL MEM', 'FINAL NUN', 'NUN', 'SAMEKH', 'AYIN', 'FINAL PE', 'PE', 'FINAL TSADI', 'TSADI', 'QOF', 'RESH', 'SHIN', 'TAV']]

HEBREW_CHARACTERS = [unicodedata.lookup(desc) for desc in DESCRIPTIONS]

chars_ord = [num for num in range(1,11)] + [num * 10 for num in range(1,11)] + [num * 100 for num in range(2,10)]

CHARS_MAP = {k: v for k, v in zip(chars_ord, HEBREW_CHARACTERS)}
