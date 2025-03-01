from collections import defaultdict

with open('data') as f:
    s, ll = f.read().split('$')
    ll = [l for l in ll.split('\n') if l != '']
    k = int(ll[0])
    ll = ll[1:]

    g_rev = defaultdict(list)
    g = defaultdict(list)
    count = defaultdict(lambda: defaultdict(lambda: 0))
    edge = defaultdict(lambda: defaultdict(tuple))
    aa, bb = set(), set()

    for l in ll:
        a, b, location, length = map(int, l.replace('node', '').split(' '))
        g_rev[b].append(a)
        g[a].append(b)
        edge[a][b] = (length, location)
        aa.add(a)
        bb.add(b)

    stack = list(bb - aa)
    while stack:
        node = stack.pop()
        for b in g_rev[node]:
            count[b][node] += 1
            stack.append(b)

    stack = [(list(aa - bb)[0], 0, -1)]
    opt_pos = longest = 0
    while stack:
        node, length, pos = stack.pop()
        for b in g[node]:
            if count[node][b] >= k:
                if pos != -1:
                    stack.append((b, length + edge[node][b][0], pos))
                else:
                    stack.append((b, length + edge[node][b][0], edge[node][b][1]))
                if length + edge[node][b][0] > longest:
                    longest = length + edge[node][b][0]
                    opt_pos = pos

    print(s[opt_pos-1:opt_pos+longest-1])
