numa = int(input())
numn = int(input())
nouns = []
adjectives = []
txt = "{adj} as {nun}"
for i in range(numa):
    adjectives.append(input())
for i in range(numn):
    nouns.append(input())
for adjective in adjectives:
    for noun in nouns:
        print(txt.format(adj=adjective,nun=noun))
