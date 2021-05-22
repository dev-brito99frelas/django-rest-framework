# DjangoRestFramework
## Bem vindo a esse  repositorio Django, esse read-me contem elementos que demonstram como o django framework funciona !

### Estrutura de um projeto criado com django:  
![django](https://user-images.githubusercontent.com/54487740/117697380-f0127000-b1b1-11eb-9c6c-aadafd41d576.png)

### Estrutura de Processo para requisições web request e response utilizada pelo django na web:

![Processo de requisições](https://miro.medium.com/max/624/0*TdYuUBdQsaeChHh9.jpg)  

## Ferramentas que precisam ter na sua maquina:
* Python 3.7 + Python3-venv

* Criar uma Virtual ENV 
    ```
    sudo apt-get install python3-venv
    ```
* Ativar Venv
    ```
    . venv/bin/activate ou source venv/bin/activate
    ```
* pip3
    ```
    sudo apt-get install python3-pip

    ```  
* Instalar Django  
    ```
    pip3 install Django

    ```
## Passo a passo para rodar o projeto : 
- Baixar todas as Dependencias:
    ```
    pip3 install -r requiriments.txt
    ```  
- Rodar as migrações:
    ```
    python3 manage.py migrate
    ```  
- Criar Usuarrio admin:
    ```
    python3 manage.py createsuperuser
    ```  
- Rodar:
    ```
    python3 manage.py runserver
    ```
E visualizar no navegador no http://127.0.0.1:8000/
