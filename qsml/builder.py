# Q S M L
# Builder Class
# michaelpeterswa 2020


class Builder(object):
    def __init__(self):
        self.data = {}
        self.groupnames = []

    def get_data(self):
        return self.data

    def set_group(self, groupname):
        self.data[groupname] = {}
        self.groupnames.append(groupname)

    def get_group(self, groupname):
        if groupname in self.groupnames:
            return self.data[groupname]
        else:
            return False

    def add_to_group(self, groupname, stock, shares):
        self.data[groupname][stock] = shares

    def get_from_group(self, groupname):
        return self.data[groupname]
