from django.db import models
from django.contrib.auth.models import User

class Clientes(models.Model): # Tabela Pacientes
    choices_sexo = (('F', 'Feminino'),
                    ('M', 'Maculino'))
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Qual usuario/deste cliente?

    def __str__(self):
        return self.nome


class DadosCliente(models.Model):

    choices_uf = (('Alagoas', 'Alagoas'),
                  ('Amapá', 'Amapá'),
                  ('Amazonas', 'Amazonas'),
                  ('Bahia', 'Bahia'),
                  ('Ceará', 'Ceará'),
                  ('Distrito Federal', 'Distrito Federal'),
                  ('Espírito Santo', 'Espírito Santo'),
                  ('Goiás', 'Goiás'),
                  ('Maranhão', 'Maranhão'),
                  ('Mato Grosso', 'Mato Grosso'),
                  ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
                  ('Minas Gerais', 'Minas Gerais'),
                  ('Pará', 'Pará'),
                  ('Paraíba', 'Paraíba'),
                  ('Paraná', 'Paraná'),
                  ('Pernambuco', 'Pernambuco'),
                  ('Piauí', 'Piauí'),
                  ('Rio de Janeiro', 'Rio de Janeiro'),
                  ('Rio Grande do Norte', 'Rio Grande do Norte'),
                  ('Rio Grande do Sul', 'Rio Grande do Sul'),
                  ('Rondônia', 'Rondônia'),
                  ('Roraima', 'Roraima'),
                  ('Santa Catarina', 'Santa Catarina'),
                  ('São Paulo', 'São Paulo'),
                  ('Sergipe', 'Sergipe'),
                  ('Tocantins', 'Tocantins'))
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)
    naturalidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=50, choices=choices_uf)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    data = models.DateTimeField()
    # percentual_musculo = models.IntegerField()
    # colesterol_hdl = models.IntegerField()
    # colesterol_ldl = models.IntegerField()
    # colesterol_total = models.IntegerField()
    # trigliceridios = models.IntegerField()
    
    def __str__(self):
        return f"Cliente({self.cliente.nome}, {self.mae})"


# class Refeicao(models.Model):
#     paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
#     titulo = models.CharField(max_length=50)
#     horario = models.TimeField()
#     carboidratos = models.IntegerField()
#     proteinas = models.IntegerField()
#     gorduras = models.IntegerField()

#     def __str__(self):
#         return self.titulo


# class Opcao(models.Model):
#     refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
#     imagem = models.ImageField(upload_to="opcao")
#     descricao = models.TextField()

#     def __str__(self):
#         return self.descricao