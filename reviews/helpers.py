from reviews.models import ReviewPizza


def criar_review(sabor, pizzaria, avaliacao):
    review, created = ReviewPizza.objects.get_or_create(
        sabor=sabor,
        pizzaria=pizzaria,
        defaults={
            'avaliacao': avaliacao
        })
    if not created:
        raise Exception(f"Já existia este review: {review}")
