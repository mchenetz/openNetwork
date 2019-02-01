class device:

    def __init__(self):
        self._commands = []
        self._systemName = ""
        self._name = ""
        self._engine = ""
        self._cmd = ""
        self._version = 0



    @property
    def getCmd(self):
        return self._commands
    @property
    def systemName(self):
        return self._systemName

    @systemName.setter
    def systemName(self, sysName):
        self._systemName = sysName

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        self._cmd = cmd

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, ver):
        self._version = ver

    @property
    def record(self):
        return self._commands

    def addRecord(self):
        self._commands.append({'systemName': self._systemName, 'name': self._name, 'engine': self._engine, 'cmd': self._cmd, 'version': self._version})
        return(200)

    def getDevBySys(self, sysName):
        results = []
        for dev in self.record:
            if dev['systemName'] == sysName:
                results.append(dev)
        return results