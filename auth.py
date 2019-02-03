class auth


def __init__(self):
    self._username = ""
    self._password = ""
    self._host = ""
    self._url = ""


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
    return self_.host


@setter.host
def host(self, host):
    self._host = host


@property
def url(self):
    return self._url


@host.setter
def url(self, url):
    self._url = url