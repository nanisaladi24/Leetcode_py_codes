def repDna(s):
    res, seen = [], set()
    for i in range(len(s)-9):
        sequence = s[i:i+10]
        if sequence in res: continue
        if sequence in seen:
            res.append(sequence)
        else:
            seen.add(sequence)
    return res

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print (repDna(s))