from django.db import models
from django.db.models import Exists, OuterRef


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
    nome = models.CharField(max_length=255)
    ingredientes = models.ManyToManyField('pizzas.Ingrediente', related_name='pizzas')

    objects = SaborPizzaQuerySet.as_manager()

    @property
    def tem_lactose(self):
        if hasattr(self, '_tem_lactose'):
            return self._tem_lactose

        # return self.ingredientes.filter(tem_lactose=True).exists()
        return SaborPizza.objects.annotate_tem_lactose().filter(pk=self.pk).get()._tem_lactose

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=255)
    tem_lactose = models.BooleanField()

    def __str__(self):
        return self.nome
