import subprocess
import var_global

session = {}

global server
global server_snaps
global descktop
global descktop_snaps

pip_packages = [
    'mysql-connector-python',
    'pyinstaller'
]
nvm_packges = [
    'node'
]

if var_global.server_http == "apahce":
    server_http = 'apache2'
else:
    server_http = 'nginx'

php = f"php{var_global.php_version}"

server = [
    'xsel',
    'jq',
    'libnss3-tools',
    'network-manager',
    'python3-pip',
    'curl',
    'git',
    'zip',
    'rar',
    'curl',
    'unzip',
    'unrar',
    'ca-certificates',
    'apt-transport-https',
    'lsb-release',
    'software-properties-common',
    var_global.server_database,
    server_http,
    'libapache2-mod-php',
    f"{php}-intl",
    f"{php}-sqlite3",
    f"{php}-mysql",
    f"{php}-pgsql",
    f"{php}-redis"
    f"{php}-gd",
    f"{php}-mbstring",
    f"{php}-curl",
    f"{php}-cli",
    f"{php}-xml",
    f"{php}-zip",
    f"{php}-redis",
]

server_spans = [
    ''
]

# Pacotes para desktop
descktop = [
    'inkscape',
    'ubuntu-restricted-extras',
    'libavcodec-extra',
    'libavc1394-tools',
    'vlc',
    'telegram-desktop'
    'kazam'
]

composer_packages = [
    'laravel/installer'
]


def install_composer():
    # Baixar o instalador do Composer
    subprocess.call(['curl', '-sS', 'https://getcomposer.org/installer',
                    '-o', '/tmp/composer-setup.php'])

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
    subprocess.call(['sudo', 'php', '/tmp/composer-setup.php',
                    '--install-dir=/usr/local/bin', '--filename=composer'])

    # Testar a instalação
    subprocess.call(['composer'])


def composer_install_pkgs():
    for composer in composer_packages:
        subprocess.call(['composer', 'global', 'riquere', composer])
        print(f'O pacote composer {composer} instalado.')


def install_nvm():
    subprocess.call(
        ['curl', 'https://raw.githubusercontent.com/creationix/nvm/master/install.sh', '|', 'bash'])
    subprocess.call(['source', '~/.profile'])


def nvm_install_pkgs():
    for nvm in nvm_packges:
        subprocess.call(['nvm', 'install', nvm])
