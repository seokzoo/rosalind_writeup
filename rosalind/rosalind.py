def parse_fasta(data):
    label = ""
    seq = ""
    parsed = {}

    for x in data.splitlines():
        if x.strip() == '':
            continue
        if x[0] == '>':
            if seq != "":
                parsed[label] = seq
                seq = ""
            label = x[1:]
        else:
            seq += x
    if seq != "":
        parsed[label] = seq

    return parsed

def get_rc(seq):
    rc = ''
    for b in seq[::-1]:
        match b:
            case 'A':
                rc += "T"
            case 'T':
                rc += "A"
            case 'G':
                rc += "C"
            case 'C':
                rc += "G"
    return rc
