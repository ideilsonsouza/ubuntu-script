import subprocess

def compress_and_copy_folder(local_folder, remote_folder, server_address, username):
    # Comprimir a pasta para um arquivo tar.gz temporário
    temp_archive = '/tmp/temp_archive.tar.gz'
    subprocess.run(f'tar -czf {temp_archive} -C {local_folder} .', shell=True)

    # Copiar o arquivo compactado para o servidor
    subprocess.run(f'scp {temp_archive} {username}@{server_address}:{remote_folder}', shell=True)

    # Descompactar o arquivo do lado do servidor
    command = f'ssh {username}@{server_address} "tar -xzf {remote_folder}/temp_archive.tar.gz -C {remote_folder} && rm {remote_folder}/temp_archive.tar.gz"'
    subprocess.run(command, shell=True)

    # Remover o arquivo compactado localmente
    subprocess.run(f'rm {temp_archive}', shell=True)

# Exemplo de uso:
local_folder = '/home/ideilson/Documentos/code/zabe'
remote_folder = '/var/www/site'
server_address = 'ideilson.dev.br'
username = 'ideilson'

compress_and_copy_folder(local_folder, remote_folder, server_address, username)

