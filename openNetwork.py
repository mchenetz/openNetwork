import yaml
import glob
import os
from device import device
def main():
    print('openNetwork 1.0 - Michael Chenetz 2019')
    getYamlDef()


def getYamlDef():
    Device = device()
    cmdFiltList = []
    fileList = glob.glob(os.path.join(os.getcwd(), "Settings", "*.yaml"))
    settings = map(lambda fileList: yaml.load_all(open(fileList)), fileList)
    for data in settings:
        for item in data:
            # Populate System Names
            Device.systemName = item.get('system')[0]['name']
            # Populate Commands
            for cmd in item['commands']:
                for name in cmd:
                    Device.name = name
                    for engine in cmd[name]:
                        Device.engine = engine['engine']
                        Device.cmd = engine['cmd']
                        Device.version = engine['ver']
                        Device.addRecord()
    print(Device.getDevBySys('Nexus'))

    # for devs in Device.record:
    #     print (devs)

if __name__ == "__main__":
    main()

