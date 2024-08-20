from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import firestore, credentials

# Inicialização do Firebase
cred = credentials.Certificate('serviceKey.json')
firebase_admin.initialize_app(cred)

# Conecte ao Firestore
db = firestore.client()

def home(request):
    return render(request, 'home.html')

def criar_usuario(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')

        # Adiciona o novo usuário ao Firestore
        db.collection('users').document(user_id).set({
            'nome': nome,
            'email': email,
            'idade': int(idade)
        })

        return redirect('sucesso')  # Redireciona para uma página de sucesso ou de confirmação

    return render(request, 'criar_usuario.html')


def consultar_usuarios_por_idade(request):
    if request.method == 'POST':
        idade = int(request.POST.get('idade'))  # Idade a ser filtrada

        # Consulta os usuários com a idade especificada
        usuarios_ref = db.collection('users').where('idade', '==', idade)
        usuarios = usuarios_ref.stream()

        usuarios_list = []
        for usuario in usuarios:
            usuarios_list.append(usuario.to_dict())  # Converte os dados do usuário em um dicionário

        return render(request, 'resultados_usuarios.html', {'usuarios': usuarios_list})

    return render(request, 'consultar_usuarios.html')

def resultados_usuarios(request):
    return render(request, 'resultados_usuarios.html')

def sucesso(request):
    return render(request, 'sucesso.html')
