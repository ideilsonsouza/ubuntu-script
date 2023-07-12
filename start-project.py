import os
import subprocess

# Função para criar uma classe Laravel
def criar_classe(nome_classe):
    subprocess.run(f"php artisan make:model {nome_classe} --migration --controller --resource --factory --views", shell=True)

# Função para criar as views de uma classe Laravel
def criar_views(nome_classe):
    pasta_views = f"resources/views/{nome_classe.lower()}"
    os.makedirs(pasta_views, exist_ok=True)
    with open(os.path.join(pasta_views, 'index.blade.php'), 'w') as f:
        f.write("<!-- Conteúdo da view index -->")
    with open(os.path.join(pasta_views, 'create.blade.php'), 'w') as f:
        f.write("<!-- Conteúdo da view create -->")
    with open(os.path.join(pasta_views, 'edit.blade.php'), 'w') as f:
        f.write("<!-- Conteúdo da view edit -->")
    with open(os.path.join(pasta_views, 'show.blade.php'), 'w') as f:
        f.write("<!-- Conteúdo da view show -->")

# Função para adicionar as rotas no arquivo web.php
def adicionar_rotas(nome_classe):
    with open("routes/web.php", 'a') as f:
        f.write(f"Route::resource('{nome_classe.lower()}', {nome_classe}Controller::class);\n")

# Criar projeto Laravel com Jetstream
nome_projeto = input("Digite o nome do projeto Laravel: ")
subprocess.run(f"laravel new {nome_projeto} --jet --stack=breeze --teams --dark", shell=True)

# Navegar até o diretório do projeto
os.chdir(nome_projeto)

# Criar a classe Empresa
criar_classe('Empresa')

# Criar controllers para as três seções da empresa
secoes = ['Britador', 'Rebritagem', 'Moagem']
for secao in secoes:
    criar_classe(secao)
    criar_views(secao)
    adicionar_rotas(secao)

# Criar views e controllers para cadastro de balanças
criar_classe('BalancaController')
criar_views('Balanca')
adicionar_rotas('Balanca')

# Executar as migrations para criar as tabelas no banco de dados
subprocess.run("php artisan migrate", shell=True)
