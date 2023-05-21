class dictObj(object):
    def __init__(self):
        self.x = 'vine red'
        self.y = 'orange'
        self.z = 'violet'

    def do_nothing(self):
        pass

run = dictObj()
print(run.__dict__)
