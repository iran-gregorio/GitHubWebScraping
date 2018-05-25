class Element:
    'Class Element'

    def __init__(self, href, title, level):
        self._href = href
        self._title = title
        self._level = level
        self._lines = 0
        self._size = 0
        self._isFile = False
        self._extensionFile = ''

    @property
    def href(self):
        return self._href

    @property
    def title(self):
        return self._title

    @property
    def level(self):
        return self._level

    @property
    def isFile(self):
        return self._isFile

    @isFile.setter
    def isFile(self, value):
        self._isFile = value

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def extensionFile(self):
        return self._extensionFile

    def setExtensionFile(self):
        splt = self.title.split('.')
        if (len(splt) > 2 or (len(splt) == 2 and len(splt[0]) > 0)):
            self._extensionFile = splt.pop()
        else:
            self._extensionFile = '<outro>'
