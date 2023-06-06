def parse_FASTA(data):
    label = ""
    seq = ""
    parsed = {}

    for x in data.splitlines():
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
