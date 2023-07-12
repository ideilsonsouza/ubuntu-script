import subprocess
import configparser
import sys

def download_package(package_name):
    # Instalar o pacote
    subprocess.call(['wget','-f', package_name,])

def download_packages():
    packages = [
     "https://az764295.vo.msecnd.net/stable/695af097c7bd098fbf017ce3ac85e09bbc5dda06/code_1.79.2-1686734195_amd64.deb",
    ]
    
    subprocess.call(['cd','/tmp'])  
    subprocess.call(['mkdir','pkgs'])
    subprocess.call(['cd','/pkgs'])
            
    for package in packages:       
            
            download_package(package)   
            subprocess.call(['sudo','dpkg','-i','*.deb'])     
            print(f'O pacote {package} foi baixado.')

def install_package(package_name):
    # Instalar o pacote
    subprocess.call(['sudo', 'apt', 'install', package_name, '-y'])

def check_package_installed(package_name):
    # Verificar se o pacote está instalado
    result = subprocess.run(['dpkg', '-s', package_name],
                            capture_output=True, text=True)
    return result.returncode == 0            

def install_packages():
    packages = [
        'inkscape',
        'ubuntu-restricted-extras',
        'libavcodec-extra', 
        'libavc1394-tools',
        'vlc',
        'telegram-desktop'
        'kazam'
    ]

    # Verificar se cada pacote está instalado e instalá-lo se não estiver
    for package in packages:
        if not check_package_installed(package):
         install_package(package)
        else:
            print(f'O pacote {package} já está instalado.')
