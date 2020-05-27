class Station:
    def __init__(self, rinex_path):
        self._path = rinex_path
        self._name = None
        self._doy = None
        self._year = None

    @property
    def name(self):
        return self._name

    @property
    def doy(self):
        return self._doy

    @property
    def year(self):
        return self._year

    @property
    def path(self):
        return self._path