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
                Device.sysName = item.get('system')[0]['name']
                item.
                for command in cmd:
                    print(command)
                    Device.name = command
                Device.engine = item.get('commands')[cmd][0]['engine']
                Device.cmd = item.get('commands')[0][cmd][0]['cmd']
                Device.version = item.get('commands')[0][cmd][0]['ver']
                Device.addRecord()
    print (Device.record[1]['systemName'])
    print (Device.getDevBySys('Nexus')['name'])

if __name__ == "__main__":
    main()

