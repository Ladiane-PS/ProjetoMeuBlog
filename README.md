

# 📝 Meu Blog - Django
Um blog simples desenvolvido com Django, onde é possível criar, listar e visualizar posts.

---

**🚀 Funcionalidades**
- ✅ Criar, editar e excluir posts.
- ✅ Listar todos os posts.
- ✅ Visualizar detalhes de um post.
- ✅ Interface de administração para gerenciar os posts.

---
**🛠️ Tecnologias Utilizadas** 

- Python (Django Framework)

- HTML, CSS (Frontend básico)

- SQLite (Banco de dados)

- Django ORM (Para interagir com o banco de dados)



## 🗄️ Banco de Dados e SQL no Projeto
Este projeto utiliza Django ORM, que gera automaticamente consultas SQL para interagir com o banco de dados.

**Definição das tabelas (models.py)**

```
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)  # Equivalente a VARCHAR(200)
    conteudo = models.TextField()  # Equivalente a TEXT
    data_criacao = models.DateTimeField(auto_now_add=True)  # Equivalente a DATETIME

```
**Consultas SQL geradas pelo Django**
Buscar todos os posts

```
Post.objects.all()     #Equivalente a select * from blog_post;
```
**Gerenciando o banco de dados**

Criar e aplicar migrações para gerar tabelas SQL:
```
python manage.py makemigrations
python manage.py migrate

```
**Se quiser visualizar as consultas SQL geradas pelo Django, use:**
```
python manage.py sqlmigrate blog 0001
```
---

## 🛠️ Como Rodar o Projeto

**1️⃣ Clone o repositório**

```
https://github.com/Ladiane-PS/ProjetoMeuBlogo.git

```

**2️⃣ Entre na pasta do projeto**

```
cd meublog
```


**3️⃣ Crie um ambiente virtual e ative:**

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

**4️⃣ Instale as dependências**

```
pip install -r requirements.txt
```

**5️⃣ Rode as migrações do banco de dados**

```
python manage.py migrate
```

**6️⃣ Inicie o servidor**

```
python manage.py runserver
```
**Acesse o blog no navegador: http://127.0.0.1:8000/**

# 📌 Contribuições

Sinta-se à vontade para contribuir com melhorias! 🚀