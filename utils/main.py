from . import parser

# main entry point for the whole script
def run():
    packageManager = ""
    configDir = ""
    # Grab, read, and execute the main.json file
    mainConf = parser.readJson("main.json")
    if (mainConf):
        packageManager = mainConf["packageManager"]
        configDir = mainConf["configDir"]
        runCommands(mainConf["preRunCommands"])

    else:
        exit(0)

def runCommands(conf):
    success = True
    if (conf):
        print(conf)
        return success
    else:
        return success and False
