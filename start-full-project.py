import os
import subprocess

# Função para criar uma classe Laravel
def criar_classe(nome_classe):
    subprocess.run(f"php artisan make:model {nome_classe} --migration --controller --resource --factory", shell=True)

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
        f.write(f"Route::middleware(['auth'])->resource('{nome_classe.lower()}', {nome_classe}Controller::class);\n")

# Criar projeto Laravel com Breeze, tema dark e Jetstream
nome_projeto = input("Digite o nome do projeto Laravel: ")
# Navegar até o diretório do projeto

# Criar o projeto Laravel
subprocess.run(f"laravel new {nome_projeto} --jet --stack=livewire --teams --dark", shell=True)

os.chdir(nome_projeto)

# Executar comandos do Artisan para configurações adicionais
subprocess.run("php artisan key:generate", shell=True)

# Criar controllers para as três seções da empresa
secoes = ['Britador', 'Rebritagem', 'Moagem', 'Empresa', 'Balanca']
for secao in secoes:
    criar_classe(secao)
    criar_views(secao)
    adicionar_rotas(secao)

# Definir as configurações do .env
subprocess.run(f'cp .env.example .env', shell=True) 
subprocess.run(f'sed -i "s/DB_HOST=127.0.0.1/DB_HOST=zabe.com.br/g" .env', shell=True)
subprocess.run(f'sed -i "s/DB_PORT=3306/DB_PORT=3360/g" .env', shell=True)
subprocess.run(f'sed -i "s/DB_DATABASE=laravel/DB_DATABASE={nome_projeto}/g" .env', shell=True)
subprocess.run(f'sed -i "s/DB_USERNAME=root/DB_USERNAME=zabe/g" .env', shell=True)
subprocess.run(f'sed -i "s/DB_PASSWORD=/DB_PASSWORD=81330808/g" .env', shell=True)
subprocess.run(f'sed -i "s/APP_NAME=Laravel/APP_NAME={nome_projeto}/g" .env', shell=True)
subprocess.run(f'sed -i "s/UTC/America\/Sao_Paulo/g" .env', shell=True)

# Executar as migrations novamente para atualizar as tabelas
subprocess.run("php artisan migrate", shell=True)

subprocess.run("npm install && npm run dev", shell=True)
