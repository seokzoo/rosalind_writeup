from Bio.Seq import translate

with open("data") as f:
    data = f.read().split('\n')
    for identifier in range(1, 16):
        if identifier == 7 or identifier == 8:
            continue
        if translate(data[0], table=identifier, stop_symbol='') == data[1]:
            print(identifier)
            break
