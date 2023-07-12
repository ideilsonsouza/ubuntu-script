import subprocess
import module
import packages
import var_global


def install_packages():
    for package in packages.server:
        module.command_install_apt(package)

def install_packages_snap():
    for package in packages.server_spans:
        module.command_install_snap(package)

        print("Projeto foi copilado")

def configure_https():  
    
    if var_global.server_http == "apache":
        server_http = "apache2"
    else:
        server_http = "nginx"
  
        if module.command_check_install(server_http):
            if module.command_check_install('certbot'):
                subprocess.call(['sudo', 'apt', 'remove', 'certbot'])
            else:
                module.command_install_snap('core')
                module.command_install_snap('certbot')
                subprocess.call(['sudo', 'snap', 'refresh', 'core',])
                subprocess.call(
                    ['sudo', 'ln', '-s', '/snap/bin/certbot', '/usr/bin/certbot'])
                subprocess.call(['certbot', f"--{var_global.server_http}", '--redirect', '-d', var_global.domaine,
                                '-d', f"www.{var_global.domaine}", '-m', f"admin@{var_global.domaine}", '--agree-tos'])
        else:
            print(
                f"Certificado SSL não pode ser instalado, esta faltando o {var_global.server_http}")
