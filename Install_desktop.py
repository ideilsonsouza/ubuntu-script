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
def main():

 download_packages()
 
if __name__ == '__main__':
    main()
