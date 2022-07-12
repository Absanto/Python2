from django.db import models

# Cris seus modelos aqui.
class Departamento(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
        
class Funcionario(models.Model):
    CARGOS = [
        ('ES','Estagiário'),
        ('AS','Assistente'),
        ('JR','Júnior'),
        ('PL','Pleno'),
        ('SR','Sênior'),
        ('GR','Gerente')
    ]
    SEXO = [
        ('F','Feminino'),
        ('M','Masculino')
    ]
    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=2, choices=CARGOS)
    sexo = models.CharField(max_length=1 , choices=SEXO,null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField(null=True)

    class Meta:
        ordering = ['nome']



