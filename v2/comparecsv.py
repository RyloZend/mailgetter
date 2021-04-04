with open('unis.csv') as f:
    full = f.read().splitlines()

with open('unimails.csv') as f:
    compare = f.read().splitlines()

unis = []
mailUnis = []

for ent in full:
    ent = ent.split(";")[0]
    ent = ent[1:]
    ent = ent[:-1]
    unis.append(ent)

for ent in compare:
    ent = ent.split(";")[0]
    ent = ent[1:]
    ent = ent[:-1]
    mailUnis.append(ent)

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

diff = Diff(unis, mailUnis)

for i in diff:
    diffFile = open("diff.csv", "a")
    diffFile.write(f"{i}\n")
    diffFile.close()

print("Ready")