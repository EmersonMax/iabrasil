from django.db import models

# Create your models here.
class Ferramentas(models.Model):
    origem = models.CharField(max_length=2000, null=True, blank=False)
    data = models.DateField(null=True, blank=False)
    origem_url = models.CharField(max_length=2000, null=True, blank=False)
    nome_ferramenta = models.CharField(max_length=500, null=True, blank=False)
    curtidas = models.IntegerField(null=True, blank=False)
    categoria = models.CharField(max_length=500, null=True, blank=False)
    subcategoria = models.CharField(max_length=500, null=True, blank=False)
    site_url = models.CharField(max_length=2000, null=True, blank=False)
    descricao_curta = models.CharField(max_length=1000, null=True, blank=False)
    descricao_longa = models.CharField(max_length=1000, null=True, blank=False)
    opnioes = models.CharField(max_length=1000, null=True, blank=False)
    estrelas = models.IntegerField(null=True, blank=False)
    data_inclusao = models.DateField(null=True, blank=False, auto_now_add=True)
    assinatura = models.CharField(max_length=1000, null=True, blank=False)
    valor_assinatura = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    foto_url_1 = models.CharField(max_length=2000, null=True, blank=False)
    foto_url_2 = models.CharField(max_length=2000, null=True, blank=False)
    tag_1 = models.CharField(max_length=2000, null=True, blank=False)
    tag_url_1 = models.CharField(max_length=2000, null=True, blank=False)
    tag_2 = models.CharField(max_length=2000, null=True, blank=False)
    tag_url_2 = models.CharField(max_length=2000, null=True, blank=False)
    relacionada_1 = models.CharField(max_length=2000, null=True, blank=False)
    relacionada_url_2 = models.CharField(max_length=2000, null=True, blank=False)
    url_youtube_1 = models.CharField(max_length=2000, null=True, blank=False)
    url_youtube_2 = models.CharField(max_length=2000, null=True, blank=False)
    
    def _str_(self):
        return self.nome_ferramenta