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
