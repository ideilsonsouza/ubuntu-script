import server
import packages
import module
    
def main():   
    
    server.install_packages_snap()
    server.install_packages()

    packages.install_composer()
    packages.install_nvm()

    packages.composer_install_pkgs()
    packages.nvm_install_pkgs()

if __name__ == '__main__':
    main()
