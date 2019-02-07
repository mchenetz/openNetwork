class auth:

    def __init__(self):
        self._username = ""
        self._password = ""
        self._host = ""
        self._url = ""
        self._authDB = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, user):
        self._username = user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def save_auth(self):
        self._authDB.append({self._username, self._password, self._host, self._url})
