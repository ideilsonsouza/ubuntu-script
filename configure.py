import subprocess
import configparser
import mysql.connector
import sys
import server
import var_global
import packages
import module


def configure_git():
    subprocess.call(['git', 'config', '--global',
                    'user.name', var_global.git_name])
    subprocess.call(['git', 'config', '--global',
                    'user.email', var_global.git_email])
    subprocess.call(['git', 'config', '--global', 'color.ui', 'auto'])
    subprocess.call(['git', 'config', '--global',
                    'init.defaultBranch', var_global.git_Branch])


def configure_mysql():
    # Carregar o arquivo de configuração
    config = configparser.ConfigParser()
    config.read('/etc/mysql/mariadb.conf.d/50-server.cnf')

    # Alterar a configuração para permitir acesso externo
    config.set('mysqld', 'bind-address', '0.0.0.0')

    # Trocar a porta para a porta desejada (por exemplo, 3307)
    config.set('mysqld', 'port', '3360')

    # Salvar as alterações
    with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'w') as configfile:
        config.write(configfile)

    subprocess.call(['sudo', 'systemctl', 'restart', 'mariadb.service'])


def create_users():
    # Conectar ao banco de dados

    from mysql.connector import (connection)
    connection = connection.MySQLConnection(host='127.0.0.1',
                                            user='root', port='3060'
                                            )

    cursor = connection.cursor()

    # Comandos SQL para criar usuários
    sql_commands = [
        "CREATE USER 'ideilson'@'%' IDENTIFIED BY '237091';",
        "CREATE USER 'admin'@'localhost' IDENTIFIED BY 'AdminMaster2023';",
        "GRANT ALL PRIVILEGES ON *.* TO 'ideilson'@'%' WITH GRANT OPTION;",
        "GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;",
    ]

    # Executar os comandos SQL
    for command in sql_commands:
        cursor.execute(command)

    # Criar o banco de dados
    cursor.execute("CREATE DATABASE main;")

    # Confirmar as alterações
    connection.commit()

    # Fechar a conexão
    cursor.close()
    connection.close()