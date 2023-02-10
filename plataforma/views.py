from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
# Para Acesar Usuario tem que esta Logado
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.messages import constants
# importe table BD
from .models import Clientes, DadosCliente
# from .models import Clientes, DadosCliente, Refeicao, Opcao
from datetime import datetime

@login_required(login_url='/auth/logar/') # Autenticar usuario Logado
def clientes(request):
    # return HttpResponse("pacientes")
    if request.method == "GET":
        # Buscando o pacinte 
        cliente = Clientes.objects.filter(id_usuario=request.user)
        return render(request, 'clientes.html', {'clientesxyz' : cliente }) 
        
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        # if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0) or (len(email.strip()) == 0) or (len(telefone.strip()) == 0):
        #     messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        #     return redirect('/pacientes/')

        # if not idade.isnumeric():
        #     messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
        #     return redirect('/pacientes/')

        clientes = Clientes.objects.filter(email=email)

        if clientes.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um cliente com esse E-mail')
            return redirect('/clientes/')

        try:
            cl1 = Clientes(
                nome = nome,
                cpf = cpf,
                sexo = sexo,
                idade = idade,
                email = email,
                telefone = telefone,
                id_usuario = request.user
            )
            cl1.save()
            messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso')
            return redirect('/clientes/')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/clientes/')


        # return HttpResponse(f"{nome}, {sexo}, {idade}, {email}, {telefone}")

@login_required(login_url='/auth/logar/')
def dados_cliente_listar(request):
    if request.method == "GET":
        clientes = Clientes.objects.filter(id_usuario=request.user)
        return render(request, 'dados_cliente_listar.html', {'clientes': clientes})


@login_required(login_url='/auth/logar/')
def dados_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    # return HttpResponse(id)
    if not cliente.id_usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Ops! este cliente não é seu')
        return redirect('/dados_cliente/')
    if request.method == "GET":
        # buscando os Dados do paciente no banco de Dados
        dados_cliente = DadosCliente.objects.filter(cliente = cliente)
        # pegando o ID do paciente
        # p1 = Pacientes.objects.get(id=id)        
        return render(request, 'dados_cliente.html', {'cliente': cliente, 'dados_cliente' : dados_cliente })
    elif request.method == "POST":
        pai = request.POST.get('pai')
        mae = request.POST.get('mae')
        nacionalidade = request.POST.get('nacionalidade')
        naturalidade = request.POST.get('naturalidade')

        uf = request.POST.get('uf')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        # numero = request.POST.get('numero')
        # Salve os dados no banco de dados
        p_salvaBD = DadosCliente(
                            cliente           = cliente,                            
                            pai               = pai,
                            mae             = mae,
                            nacionalidade = nacionalidade,
                            naturalidade = naturalidade,
                            uf     = uf,
                            cidade     = cidade,
                            bairro   = bairro,
                            numero     = numero,
                            data               = datetime.now())

        p_salvaBD.save()

        messages.add_message(request, constants.SUCCESS, 'Dados cadastrado com sucesso')


        return redirect('/dados_cliente/')
    


# # Craindo uma API para o Grafico
# from django.views.decorators.csrf import csrf_exempt

# @login_required(login_url='/auth/logar/')
# @csrf_exempt
# def grafico_peso(request, id):
#     paciente = Pacientes.objects.get(id=id)
#     dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    
#     pesos = [dado.peso for dado in dados]
#     labels = list(range(len(pesos)))
#     data = {'peso': pesos,
#             'labels': labels}
#     return JsonResponse(data)

# # Plano alimentar listar
# def plano_alimentar_listar(request):
#     if request.method == "GET":
#         pacientes = Pacientes.objects.filter(nutri=request.user)
#         return render(request, 'plano_alimentar_listar.html', {'pacientes': pacientes})


# # Plano alimentar
# def plano_alimentar(request, id):
#     paciente = get_object_or_404(Pacientes, id=id)
#     if not paciente.nutri == request.user:
#         messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
#         return redirect('/plano_alimentar_listar/')

#     if request.method == "GET":
#         # pegando as refeicoes do paciente - Ordenando pelo horario
#         r1 = Refeicao.objects.filter(paciente=paciente).order_by("horario")
#         opcao = Opcao.objects.all() # Todas as Opçoes
#         return render(request, 'plano_alimentar.html', {'paciente': paciente, 'refeicao': r1, 'opcao': opcao })  #enviando para o HTML




# # Refeição
# def refeicao(request, id_paciente):
#     paciente = get_object_or_404(Pacientes, id=id_paciente)
#     if not paciente.nutri == request.user:
#         messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
#         return redirect('/dados_paciente/')

#     if request.method == "POST":
#         titulo = request.POST.get('titulo')
#         horario = request.POST.get('horario')
#         carboidratos = request.POST.get('carboidratos')
#         proteinas = request.POST.get('proteinas')
#         gorduras = request.POST.get('gorduras')

#         r1 = Refeicao(paciente=paciente,
#                       titulo=titulo,
#                       horario=horario,
#                       carboidratos=carboidratos,
#                       proteinas=proteinas,
#                       gorduras=gorduras)

#         r1.save()

#         messages.add_message(request, constants.SUCCESS, 'Refeição cadastrada')
#         return redirect(f'/plano_alimentar/{id_paciente}')


# def opcao(request, id_paciente):
#     if request.method == "POST":
#         id_refeicao = request.POST.get('refeicao')
#         imagem = request.FILES.get('imagem')
#         descricao = request.POST.get("descricao")

#         o1 = Opcao(refeicao_id=id_refeicao,
#                    imagem=imagem,
#                    descricao=descricao)

#         o1.save()

#         messages.add_message(request, constants.SUCCESS, 'Opção cadastrada')
#         return redirect(f'/plano_alimentar/{id_paciente}')