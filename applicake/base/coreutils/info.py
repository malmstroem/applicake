from configobj import ConfigObj

from applicake.base.coreutils import Keys


def get_handler(path):
    """
    this is the factory method
    """
    if path is None or path is '':
        return NoneInfoHandler()
    elif ".ini" in path:
        return IniInfoHandler()
    else:
        raise Exception("Unknown info type " + path)


####################################################

class IInfoHandler(object):
    def read(self, path):
        raise NotImplementedError

    def write(self, info, path):
        raise NotImplementedError


class NoneInfoHandler(IInfoHandler):
    def read(self, path):
        return {}

    def write(self, info, path):
        pass


class IniInfoHandler(IInfoHandler):
    def read(self, path):
        return ConfigObj(path)

    def write(self, info, path):
        info = info.copy()
        for key in [Keys.INPUT, Keys.OUTPUT, Keys.NAME, Keys.WORKDIR, Keys.EXECUTABLE, Keys.ALL_ARGS]:
            if key in info:
                del info[key]
        config = ConfigObj(info)
        config.filename = path
        config.write()

    def write_all(self, info, path):
        ''' same as write but does not do special key filtering. For debug purposes only'''
        info = info.copy()
        config = ConfigObj(info)
        config.filename = path
        config.write()
     
     
     
     
     
     
