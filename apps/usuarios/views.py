from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form =  LoginForms(request.POST)
        
        if form.is_valid:
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar o login')
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {"form":form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            nome = form["nome_cadastro"].value()
            email = form["email"].value() # ajusta os valores do usuario
            senha = form["senha_1"].value()
            

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuario já existente')
                return redirect('cadastro')  # verifica se os valores do usuario ja existe
            
            usuario = User.objects.create_user(
                username = nome, 
                email = email,    # cria o novo usuario
                password = senha
                
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')


    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
<<<<<<< HEAD:apps/usuarios/views.py
    return redirect('login')
=======
    return redirect('login')
>>>>>>> 5c51dda87eb777f9468bfe3916f8f9c7329be9eb:usuarios/views.py
