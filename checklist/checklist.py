checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def test():
    checklist.append("purple sox")
    checklist.append("red cloak")

    print(read(0))
    print(read(1))

    checklist[0] = ("purple socks")
    checklist.pop(1)

    print(read(0))
    print(read(1))

test()

# checklist = ['Blue', 'Cats']
# checklist.pop(1)
# print(checklist)
