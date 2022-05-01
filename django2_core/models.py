from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criaçao', auto_now_add=True)
    editado = models.DateField('Editado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_sabe(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_sabe, sender=Produto)
