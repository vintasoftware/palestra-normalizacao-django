import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # fix PYTHONPATH
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaproject.settings")
import django
django.setup()

from django.db.models import Count

from multiprocessing.dummy import Pool as ThreadPool

from pizzarias.models import Pizzaria
from pizzas.models import SaborPizza
from reviews.models import ReviewPizza
from reviews.helpers import criar_review as criar_review_helper


def criar_pizzaria():
    Pizzaria.objects.update_or_create(nome="Mamma's")


def criar_sabor_pizza():
    SaborPizza.objects.update_or_create(nome="Margherita")


def deletar_reviews_antigos():
    ReviewPizza.objects.all().delete()


def criar_review():
    pizzaria = Pizzaria.objects.get(nome="Mamma's")
    sabor = SaborPizza.objects.get(nome="Margherita")
    avaliacao = 5
    try:
        criar_review_helper(sabor, pizzaria, avaliacao)
    except Exception as e:
        print(e)


def criar_concorrentemente(tamanho_pool):
    pool = ThreadPool(tamanho_pool)

    for __ in range(tamanho_pool):
        pool.apply_async(criar_review)

    pool.close()
    pool.join()


def detectar_anomalia():
    # esta anomalia só vai acontecer na migração 0001 de reviews,
    # que é a que não tem `unique_together` em `ReviewPizza`,
    # então rodar: python manage.py migrate reviews 0001
    qs = ReviewPizza.objects.values(
        'sabor__nome', 'pizzaria__nome'
    ).annotate(
        # não usar distinct aqui,
        # pois queremos identificar se {sabor, pizzaria} são únicos na tabela inteira
        count=Count('sabor')
    ).filter(count__gt=1)
    for anomalia in qs:
        print(
            f"Anomalia detectada: "
            f"{anomalia['sabor__nome']}, {anomalia['pizzaria__nome']}")


criar_pizzaria()
criar_sabor_pizza()
deletar_reviews_antigos()
criar_concorrentemente(4)
detectar_anomalia()
