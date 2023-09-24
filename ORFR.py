from Bio.Seq import Seq

if __name__ == "__main__":
    with open("data") as f:
        seq = f.read().strip()
        longest = ''

        for seq in [str(Seq(seq).reverse_complement()), str(Seq(seq))]:
            for i in [0, 1, 2]:
                orf = str(Seq(seq[i:]).translate()).strip()
                met_index_list = [i for i, x in enumerate(orf) if x == 'M']
                stop_index_list = [i for i, x in enumerate(orf) if x == '*']

                for x in met_index_list:
                    z = ''
                    try:
                        y = orf[x:].index('*')
                        z = orf[x:x+y]
                    except ValueError:
                        z = orf[x:]
                    if len(longest) < len(z):
                        longest = z
        print(longest)
