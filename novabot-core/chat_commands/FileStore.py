class FileStore:
    def __init__(self):
        self.links = {}
        f = open('links.txt', 'r')
        lines = f.readlines()
        for line in lines:
            if len(line) > 0:
                data = line.split("====")
                self.links[data[0]] = data[1]

    def add_link(self, key, link):
        self.links[key] = link
        f = open('links.txt', 'a')
        f.write("%s====%s\n" % (key, link))
        f.close()

    def get_link(self, key):
        return self.links[key]