import re
import requests

data = open("data").read().splitlines()

for UID in data:
    SEQ = ''.join(requests.get("https://rest.uniprot.org/uniprotkb/" + UID.split('_')[0] + ".fasta").text.splitlines()[1:])

    p = re.compile("(?=N[^P][ST][^P])")
    idx = [str(x.span()[0] + 1) for x in p.finditer(SEQ)]
    if len(idx) > 0:
        print(UID)
        print(' '.join(idx))
