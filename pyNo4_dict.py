counts=dict()
names={'abc','def','abc','mno','mno'}
for name in names:
    if name not in names:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)