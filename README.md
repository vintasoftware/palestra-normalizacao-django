# Exemplos da palestra "Normalize até machucar, desnormalize até funcionar em Django"
Este repositório contem um projeto com diversos exemplos dos conceitos discutidos na palestra "Normalize até machucar, desnormalize até funcionar em Django" apresentada na Python Nordeste 2018. Slides disponíveis em: http://bit.ly/pyne-normal

## Rodando os exemplos
- Inicie um virtualenv
- Instale as dependências: `pip install -r requirements.txt`
- Crie um banco PostgreSQL chamado pizzaproject: `createdb pizzaproject` 
- Rode as migrações: `python manage.py migrate`
- Carregue os dados de exemplo: `python manage.py loaddata fixtures.json`
- Atualize as materialized views: `python manage.py sync_pgviews`
- Atualize os triggers: `python manage.py denorm_init`
- Rode o servidor local: `python manage.py runserver`


## Exemplos de problemas de normalização
### Concorrência + falta de chave candidata
Confira a lógica de múltiplos threads em [\_scripts/quebrar\_review\_pizza.py](_scripts/quebrar_review_pizza.py). Para gerar a anomalia, rodar antes `python manage.py migrate reviews 0001` para desativar o `unique_together` de `ReviewPizza`.


### Computando coluna histórica
Confira `valor_total` em [pedidos/models.py](pedidos/models.py). Veja a lógica de computação em [pedidos/helpers.py](pedidos/helpers.py) e a integração em [pedidos/admin.py](pedidos/admin.py).


### Evitando desnormalização computando atributos a nível de banco e em tempo de consulta
Confira `PizzariaQuerySet` em [pizzarias/models.py](pizzarias/models.py) e o uso dele em `PizzariaAdmin` do [pizzarias/admin.py](pizzarias/admin.py).


### Materialized Views
Confira `SaborPizzaMaterializedView` em [pizzas/models.py](pizzas/models.py). Após alterar `Ingrediente`s, rode `python manage.py sync_pgviews` para atualizar os valores da materialized view.


### Triggers + Colunas desnormalizadas
Confira `tem_lactose_denormalized` dentro de `SaborPizza` do [pizzas/models.py](pizzas/models.py). Se mudar a lógica ou os campos `denormalized`, rode `python manage.py denorm_init` para atualizar os triggers e `python manage.py makemigrations` + `python manage.py migrate` se necessário.


## Contato
Problemas? Contatar [@flaviojuvenal](https://twitter.com/flaviojuvenal)
