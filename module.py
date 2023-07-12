import subprocess
import sys

session = {}
global command_apt_unlok
global command_dpkg_configure
global command_apt_install_f

command_apt_unlok = 'sudo rm /var/lib/dpkg/lock-frontend /var/lib/apt/lists/lock'
command_dpkg_configure = 'sudo dpkg --configure -a'
command_apt_install_f  = 'sudo apt install -f'



def command_pip_install(pip_package):
    subprocess.call([sys.executable, '-m', 'pip', 'install', pip_package])

def command_check_install(package_name):
    result = subprocess.run(['dpkg', '-s', package_name],
                            capture_output=True, text=True)
    return result.returncode == 0


def command_install_apt(package_name):
    if command_check_install(package_name):
        print(f"O pacote {package_name} já está instalado.")
        return False
    else:
        try:
            subprocess.call(['sudo', 'apt', 'install',
                            package_name, '-y'], stdout=subprocess.DEVNULL)
            print(f"O pacote {package_name} foi instalado com sucesso.")
            return True
        except subprocess.CalledProcessError:
            print(f"Ocorreu um erro ao instalar o pacote {package_name}.")
            return False


def command_install_snap(package_name):
    if command_check_install(package_name):
        print(f"O pacote Snap {package_name} já está instalado.")
        return False
    else:
        try:
            subprocess.call(
                ['sudo', 'snap', 'install', package_name, '--quiet'])
            print(f"O pacote Snap {package_name} foi instalado com sucesso.")
            return True
        except subprocess.CalledProcessError:
            print(f"Ocorreu um erro ao instalar o pacote Snap {package_name}.")
            return False


def command_install_dpkg(package_name):
    if command_check_install(package_name):
        print(f"O pacote {package_name} já está instalado.")
        return False
    else:
        try:
            subprocess.call(['sudo', 'dpkg', '-i', package_name],
                            stdout=subprocess.DEVNULL)
            print(f"O pacote {package_name} foi instalado com sucesso.")
            return True
        except subprocess.CalledProcessError:
            print(f"Ocorreu um erro ao instalar o pacote {package_name}.")
            return False


def command_add_repository(repository):
    existing_repos = get_installed_repositories()
    if repository in existing_repos:
        print(f"O repositório {repository} já está adicionado.")
        return False
    else:
        try:
            subprocess.call(['sudo', 'add-apt-repository', repository])
            subprocess.call(['sudo', 'apt', 'update'])
            print(f"O repositório {repository} foi adicionado com sucesso.")
            return True
        except subprocess.CalledProcessError:
            print(f"Ocorreu um erro ao adicionar o repositório {repository}.")
            return False


def get_installed_repositories():
    output = subprocess.check_output(['apt-cache', 'policy']).decode('utf-8')
    lines = output.split('\n')
    repositories = []
    for line in lines:
        if line.startswith('  '):
            repository = line.strip()
            repositories.append(repository)
    return repositories


def command_restart_service(service_name):
    try:
        subprocess.call(['sudo', 'systemctl', 'restart', service_name])
        print(f"O serviço {service_name} foi reiniciado com sucesso.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ocorreu um erro ao reiniciar o serviço {service_name}.")
        return False


def command_start_service(service_name):
    try:
        subprocess.call(['sudo', 'systemctl', 'start', service_name])
        print(f"O serviço {service_name} foi iniciado com sucesso.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ocorreu um erro ao iniciar o serviço {service_name}.")
        return False


def command_stop_service(service_name):
    try:
        subprocess.call(['sudo', 'systemctl', 'stop', service_name])
        print(f"O serviço {service_name} foi parado com sucesso.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ocorreu um erro ao parar o serviço {service_name}.")
        return False


def command_enable_service(service_name):
    try:
        subprocess.call(['sudo', 'systemctl', 'enable', service_name])
        print(f"O serviço {service_name} foi habilitado com sucesso.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ocorreu um erro ao habilitar o serviço {service_name}.")
        return False


def command_disable_service(service_name):
    try:
        subprocess.call(['sudo', 'systemctl', 'disable', service_name])
        print(f"O serviço {service_name} foi desabilitado com sucesso.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ocorreu um erro ao desabilitar o serviço {service_name}.")
        return False


def command_update_packages_apt():
    try:
        with open('/dev/null', 'w') as devnull:
            subprocess.call(['sudo', 'apt', 'update'],
                            stdout=devnull, stderr=devnull)
            subprocess.call(['sudo', 'apt', 'upgrade', '-y'],
                            stdout=devnull, stderr=devnull)
        print("Os pacotes foram atualizados com sucesso via APT.")
        return True
    except subprocess.CalledProcessError:
        print("Ocorreu um erro ao atualizar os pacotes via APT.")
        return False


def command_update_packages_snap():
    try:
        with open('/dev/null', 'w') as devnull:
            subprocess.call(['sudo', 'snap', 'refresh'],
                            stdout=devnull, stderr=devnull)
        print("Os pacotes foram atualizados com sucesso via Snap.")
        return True
    except subprocess.CalledProcessError:
        print("Ocorreu um erro ao atualizar os pacotes via Snap.")
        return False
