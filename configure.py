import subprocess
import configparser
import sys

def install_mysql_connector():
    try:
        subprocess.call([sys.executable, '-m', 'pip', 'install', 'mysql-connector-python'])
        import mysql.connector
        print("O módulo mysql-connector-python foi instalado com sucesso.")
    except Exception as e:
        print("Ocorreu um erro ao instalar o módulo mysql-connector-python:", str(e))
        
def configure_mysql():
    # Carregar o arquivo de configuração
    config = configparser.ConfigParser()
    config.read('/etc/mysql/mariadb.conf.d/50-server.cnf')

    # Alterar a configuração para permitir acesso externo
    config.set('mysqld', 'bind-address', '0.0.0.0')

    # Salvar as alterações
    with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'w') as configfile:
        config.write(configfile)
        
   subprocess.call(['sudo', 'systemctl', 'restart', 'mariadb.service']) 

def create_users():
    # Conectar ao banco de dados
   # subprocess.call(['sudo','mysql_secure_installation'])
    
    from mysql.connector import (connection)
    connection = connection.MySQLConnection(host='127.0.0.1',
                                         user='root',
                                         )
  
    
    cursor = connection.cursor()

    # Comandos SQL para criar usuários
    sql_commands = [
        "CREATE USER 'ideilson'@'%' IDENTIFIED BY '@Ics#2304';",
        "CREATE USER 'admin'@'localhost' IDENTIFIED BY 'AdminMaster2023';",
        "GRANT ALL PRIVILEGES ON *.* TO 'ideilson'@'%' WITH GRANT OPTION;",
        "GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;",
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
    
    
   def main():
    
    configure_mysql()
    print("Configuração do MySQL atualizada com sucesso!")
    
    install_mysql_connector()
    
    create_users()
    print("Usuários criados com sucesso no MariaDB!")

if __name__ == '__main__':
    main()

