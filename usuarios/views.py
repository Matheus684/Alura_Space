from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
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
            return redirect('index')
        else:
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {"form":form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid(): # verifica se o formulario e valido 
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect('cadastro') # verifica se a senha sao iguais

            nome = form["nome_cadastro"].value()
            email = form["email"].value() # ajusta os valores do usuario
            senha = form["senha_1"].value()
            

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')  # verifica se os valores do usuario ja existe
            
            usuario = User.objects.create_user(
                username = nome, 
                email = email,    # cria o novo usuario
                password = senha
                
            )
            usuario.save
            return redirect('login')


    return render(request, 'usuarios/cadastro.html', {'form':form})

