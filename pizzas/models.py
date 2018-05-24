from django.db import models
from django.db.models import Exists, OuterRef

from django_pgviews import view


class SaborPizzaQuerySet(models.QuerySet):

    def annotate_tem_lactose(self):
        ingredientes_com_lactose_subquery = Ingrediente.objects.filter(
            pizzas=OuterRef('pk'),
            tem_lactose=True)
        return self.annotate(_tem_lactose=Exists(ingredientes_com_lactose_subquery))

    def com_lactose(self):
        return self.annotate_tem_lactose().filter(_tem_lactose=True)

    def sem_lactose(self):
        return self.annotate_tem_lactose().filter(_tem_lactose=False)


class SaborPizza(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    ingredientes = models.ManyToManyField('pizzas.Ingrediente', related_name='pizzas')

    objects = SaborPizzaQuerySet.as_manager()

    @property
    def tem_lactose(self):
        if hasattr(self, '_tem_lactose'):
            return self._tem_lactose

        # return self.ingredientes.filter(tem_lactose=True).exists()
        return SaborPizza.objects.filter(pk=self.pk)\
            .annotate_tem_lactose().values('_tem_lactose').get()['_tem_lactose']

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=255)
    tem_lactose = models.BooleanField()

    def __str__(self):
        return self.nome


class SaborPizzaMaterializedView(view.MaterializedView):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    sem_lactose = models.BooleanField()

    sql = '''
        SELECT
            id,
            nome,
            EXISTS(
                SELECT U0."id", U0."nome", U0."tem_lactose"
                FROM "pizzas_ingrediente" U0
                INNER JOIN "pizzas_saborpizza_ingredientes" U1 ON U0."id" = U1."ingrediente_id"
                WHERE U1."saborpizza_id" = "pizzas_saborpizza"."id" AND U0."tem_lactose" = TRUE
            ) AS sem_lactose
        FROM
            pizzas_saborpizza
    '''

    def __str__(self):
        return self.nome
