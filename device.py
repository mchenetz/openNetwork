class device:

    def __init__(self):
        self._commands = []
        self._model = ""
        self._name = ""
        self._engine = ""
        self._cmd = ""
        self._method = ""
        self._version = 0



    @property
    def getCmd(self):
        return self._commands
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

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
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method

    @property
    def record(self):
        return self._commands

    def addRecord(self):
        self._commands.append({'model': self._model, 'name': self._name, 'engine': self._engine, 'cmd': self._cmd, 'method:': self._method, 'version': self._version})
        return(200)

    def getDevBySys(self, model):
        results = []
        for dev in self.record:
            if dev['model'] == model:
                results.append(dev)
        return results