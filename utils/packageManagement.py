import subprocess

# Takes an array of packages and the package manager
def install(packages, packageManager):
    installCommand = []

    if packageManager == "yay":
        installCommand = ["yay", "-Sy", "--noconfirm"]

    elif packageManager == "pacman":
        installCommand = ["sudo", "pacman", "-Sy", "--noconfirm"]

    elif packageManager == "dnf":
        installCommand = ["sudo", "dnf", "install", "-y"]

    elif packageManager == "apt":
        installCommand = ["sudo", "apt", "install", "-y"]

    else:
        return f"\t# Uknown package manager, can't uninstall: {packageManager}"

    for package in packages:
        installCommand.append(package)

    retCodes = subprocess.run(installCommand)
    
    if retCodes.returncode == 0:
        return f"\t# Success: Successfully installed {packages}"

    else:
        return f"\t# Error: There was an error installing one of the following packages {packages}"

# Takes an array of packages and the package manager
def uninstall(packages, packageManager):
    uninstallCommand = []

    if packageManager == "yay":
        uninstallCommand = ["yay", "-R", "--noconfirm"]

    elif packageManager == "pacman":
        uninstallCommand = ["sudo", "pacman", "-R", "--noconfirm"]

    elif packageManager == "dnf":
        uninstallCommand = ["sudo", "dnf", "remove", "-y"]

    elif packageManager == "apt":
        uninstallCommand = ["sudo", "apt", "autoremove", "-y"]

    else:
        return f"\t# Uknown package manager, can't uninstall: {packageManager}"

    for package in packages:
        uninstallCommand.append(package)

    retCodes = subprocess.run(uninstallCommand)
    
    if retCodes.returncode == 0:
        return f"\t# Success: Successfully uninstalled {packages}"

    else:
        return f"\t# Error: There was an error uninstalling one of the following packages {packages}"
