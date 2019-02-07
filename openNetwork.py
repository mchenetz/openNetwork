import yaml
import glob
import os
from device import device

def main():
    print('openNetwork 1.0 - Michael Chenetz 2019')
    populateYamlDef()


def populateYamlDef():
    Device = device()
    cmdFiltList = []
    fileList = glob.glob(os.path.join(os.getcwd(), "Devices", "*.yaml"))
    settings = map(lambda fileList: yaml.load_all(open(fileList)), fileList)
    for data in settings:
        for item in data:
            # Populate System Names
            Device.model = item.get('system')[0]['model']
            # Populate Commands
            for cmd in item['commands']:
                for name in cmd:
                    Device.name = name
                    for engine in cmd[name]:
                        Device.engine = engine['engine']
                        Device.cmd = engine['cmd']
                        if 'method' in engine:
                            Device.method = engine['method']
                        Device.version = engine['ver']
                        Device.addRecord()
                        Device.engine = ""
                        Device.cmd = ""
                        Device.method = ""
                        Device.version = 0
    return Device.record


if __name__ == "__main__":
    main()

