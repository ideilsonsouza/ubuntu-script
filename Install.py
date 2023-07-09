import subprocess
import configparser
import sys

def configure_git():
    subprocess.call(['git', 'config', '--global', 'user.name', 'Ideilson Souza'])
    subprocess.call(['git', 'config', '--global', 'user.email', 'ideilson.raise@gmail.com'])
    subprocess.call(['git', 'config', '--global', 'color.ui', 'auto'])

def install_composer():
    # Baixar o instalador do Composer
    subprocess.call(['curl', '-sS', 'https://getcomposer.org/installer', '-o', '/tmp/composer-setup.php'])
    
    # Obter o hash do instalador
    hash_command = ['curl', '-sS', 'https://composer.github.io/installer.sig']
    result = subprocess.run(hash_command, capture_output=True, text=True)
    composer_hash = result.stdout.strip()
    
    # Verificar o hash do instalador
    verify_command = [
        'php', '-r',
        f"if (hash_file('SHA384', '/tmp/composer-setup.php') === '{composer_hash}') "
        "{ echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
    ]
    subprocess.call(verify_command)
    
    # Instalar o Composer
    subprocess.call(['sudo', 'php', '/tmp/composer-setup.php', '--install-dir=/usr/local/bin', '--filename=composer'])
    
    # Testar a instalação
    subprocess.call(['composer'])

def check_package_installed(package_name):
    # Verificar se o pacote está instalado
    result = subprocess.run(['dpkg', '-s', package_name], capture_output=True, text=True)
    return result.returncode == 0

def install_package(package_name):
    # Instalar o pacote
    subprocess.call(['sudo', 'apt', 'install', package_name, '-y'])

def install_packages():
    packages = [
    'python3-pip'
    ,'curl'
    ,'git'
    ,'zip'
    ,'rar'
    ,'curl'
    ,'unzip'
    ,'unrar'
    ,'ca-certificates'
    ,'apt-transport-https' 
    ,'lsb-release' 
    ,'software-properties-common'
    ,'apache2'
    ,'mariadb-server' 
    ,'php'
    ,'mariadb-client'
    ,'libmariadb-dev'
    ,'libapache2-mod-php'
    ,'php-intl'
    ,'php-sqlite3'
    ,'php-gd'
    ,'php-mbstring'
    ,'php-curl' 
    ,'php-cli' 
    ,'php-xml'
    ]

    # Verificar se cada pacote está instalado e instalá-lo se não estiver
    for package in packages:
        if not check_package_installed(package):
            install_package(package)
        else:
            print(f'O pacote {package} já está instalado.')

    # Reiniciar o Apache
    subprocess.call(['sudo', 'systemctl', 'restart', 'apache2'])
       
def main():
    install_packages()
    print("Ambiente de desenvolvimento configurado com sucesso!")
      
    configure_git()
    print("Configuração do Git concluída!")
    
    install_composer()
    print("Composer instalado com sucesso!")

if __name__ == '__main__':
    main()
