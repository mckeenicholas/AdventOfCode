
class tree:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.dir = []

    def __str__(self, level = 0):
        to_return = "\t" * level + self.name + "\n"
        for d in self.dir:
            to_return += "\t"* (level + 1) + str(d) + "\n"
        for child in self.children:
            to_return += "\t" + child.__str__(level + 1)
        return to_return

    def size(self):
        size = 0
        if self.dir is not None:
            for d in self.dir:
                size += d
        if self.children is not None:
            for child in self.children:
                size += child.size()
        return size

    def find_size_under(self):
        total_size = 0
        if self.size() <= 100000:
            total_size = self.size()
        if files.children is not None:
            for child in self.children:
                total_size += child.find_size_under()
        return total_size

    def get_all_directories(self):
        directories = {self.name: self.size()}
        for child in self.children:
            temp_dir = child.get_all_directories()
            for item in temp_dir.keys():
                directories[item] = temp_dir[item]
        return directories


if __name__ == "__main__":
    f = open("data7.txt")
    line = f.readline()
    line = f.readline()
    files = tree("\\")
    curr = files
    while line != "":
        if line[:4] == "$ cd":
            if line[:7] == "$ cd ..":
                curr = curr.parent
            else:
                new = tree(line[4:])
                new.parent = curr
                curr.children.append(new)
                curr = new
            line = f.readline()
        elif line[:4] == "$ ls":
            line = f.readline()
            while line != "" and line[0] != "$":
                if line[0] != "d":
                    curr.dir.append(int(line[:line.find(" ")]))
                line = f.readline()
    print(files)


    # Part 1
    print(files.find_size_under())

    # Part 2
    print(30000000-(70000000-files.size()))
    directories = files.get_all_directories()
    min = files.size()
    for item in directories.values():
        if 8518336 <= item < min:
            min = item
    print(min)