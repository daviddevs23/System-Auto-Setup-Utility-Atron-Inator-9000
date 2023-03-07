from . import parser, packageManagement
import os, sys

# Globals for current packageManager and configDir
config = {}
config["packageManager"] = ""
config["configDir"] = ""
config["commandResults"] = ""

# main entry point for the whole script
def run():
    # Grab, read, and execute the main.json file
    mainConf = parser.readJson("main.json")
    if (mainConf):
        runCommands(mainConf)
        print(config["commandResults"])

    else:
        exit(0)


# Full list of supported commands
#   install - installs the following list of packages
#   packageManager - sets the package manager that should be used
#   commands - runs custom commands that are in the following list in order
#   runCommands - commands that should be run in that file
#   configDir - sets the config directory
#   edit - lets you change a file
#   systemd - work with systemd processes
#
# Returns true if everything worked and false if there was a fail.
# Prints out the status of the commands as they are run
def runCommands(conf):
    if (conf):
        for key in conf.keys():

            if key == "install":
                ret = packageManagement.install(conf[key], config["packageManager"])
                config["commandResults"] = ret + "\n"

            elif key == "install":
                ret = packageManagement.uninstall(conf[key], config["packageManager"])
                config["commandResults"] = ret + "\n"

            elif key == "packageManager":
                config["packageManager"] = conf[key]

            elif key == "configDir":
                config["configDir"] = conf[key]

            elif key == "runCommands":
                runCommands(conf[key])

            elif key == "commands":
                print("commands")

            elif key == "edit":
                print("edit")

            elif key == "systemd":
                print("systemd")

            else:
                print(f"Command: {key} could not be found")

