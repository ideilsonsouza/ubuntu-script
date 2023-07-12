import subprocess

def copy_folder_to_server(local_folder, remote_folder, server_address, username):
    command = f'scp -r {local_folder} {username}@{server_address}:{remote_folder}'
    subprocess.run(command, shell=True)

# Exemplo de uso:
local_folder = '/home/ideilson/Documentos/code/zabe'
remote_folder = '/var/www/zabe'
server_address = 'zabe.com.br'
username = 'ideilson'

copy_folder_to_server(local_folder, remote_folder, server_address, username)
