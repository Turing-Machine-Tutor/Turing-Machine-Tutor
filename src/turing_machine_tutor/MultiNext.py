class MultiNext:
    def __init__(self, *info):
        self.info = []
        for x in info:
            self.info.append(x)
    def __getitem__(self, index):
        return self.info[index]