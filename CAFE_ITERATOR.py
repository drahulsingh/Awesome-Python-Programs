class cafe:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        for item in self.name:
            yield item

c = cafe(["ali cafe", "nilofar cafe", "deccan cafe"])

for i in c:
    print(i)

for i in c:
    print(i)

for i in c:
    print(i)