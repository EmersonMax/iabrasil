from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ferramentas
from django.core.paginator import Paginator
import pandas as pd
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm 
from django.contrib.auth.models import User
# Create your views here.



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Use o email como nome de usuário

        if user is not None:
            login(request, user)
            # Redirecionar para uma página após o login bem-sucedido
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')

  
def logout_view(request):
    logout(request)
    # Redirecionar para uma página após o logout
    return redirect('home')

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Verifica se o campo "username" está vazio e gera um nome de usuário se necessário
            if not user.username:
                user.username = f"{form.cleaned_data['first_name']}_{form.cleaned_data['last_name']}"

            user.save()
            login(request, user)
            return redirect("home")  # Redirecione para a página desejada após o registro
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def home(request):
   
    # Ordene as ferramentas pelo número de curtidas (maior para menor)
    ferramentas = Ferramentas.objects.order_by('-curtidas')
    categorias_distintas = Ferramentas.objects.values_list('categoria', flat=True).distinct()
    # Configure a paginação
    paginator = Paginator(ferramentas, 12)  # 12 itens por página
    page_number = request.GET.get('page')
    page_ferramentas = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_ferramentas': page_ferramentas,'categorias_distintas': categorias_distintas,})

def importar_planilha(request):
    if request.method == 'POST' and request.FILES['planilha']:
        planilha = request.FILES['planilha']
        dados = pd.read_excel(planilha)

        # Criar uma lista para armazenar as instâncias do modelo
        instancias = []

        for index, linha in dados.iterrows():
            if linha['ESTRELAS'] == '-':
                estrelas = 0
            else:
                estrelas = linha['ESTRELAS']
            if linha['VALOR_ASSINATURA'] == '-':
                vl_assinatura = 0
            else:
                vl_assinatura = linha['VALOR_ASSINATURA']
            instancia = Ferramentas()
            instancia = Ferramentas()
            instancia.origem = linha['ORIGEM']
            instancia.data = linha['DATE']
            instancia.origem_url = linha['ORIGIN_URL']
            instancia.nome_ferramenta = linha['NOME']
            instancia.curtidas = linha['CURTIDAS']
            instancia.categoria = linha['CATEGORIA']
            instancia.subcategoria = linha['SUBCATEGORIA']
            instancia.site_url = linha['SITE_URL']
            instancia.descricao_curta = linha['DESCRICAO_CURTA']
            instancia.descricao_longa = linha['DESCRICAO_LONGA']
            instancia.opnioes = linha['OPINIOES']
            instancia.estrelas = estrelas
            instancia.assinatura = linha['ASSINATURA']
            instancia.valor_assinatura = vl_assinatura
            instancia.foto_url_1 = linha['FOTO_URL']
            instancia.foto_url_2 = linha['FOTO_URL_2']
            instancia.tag_1 = linha['TAG']
            instancia.tag_url_1 = linha['URL_TAG']
            instancia.tag_2 = linha['TAG_1']
            instancia.tag_url_2 = linha['URL_TAG_1']
            instancia.relacionada_1 = linha['RELACIONADA_1']
            instancia.relacionada_url_2 = linha['URL_RELACIONADA_2']
            instancia.url_youtube_1 = linha['URL_YOUTUBE_1']
            instancia.url_youtube_2 = linha['URL_YOUTUBE_2']
            instancia.save()

        # Inserir as instâncias em lote no banco de dados
       

        return render(request, 'sucesso.html')
   
    return render(request, 'upload_form.html')

def search_view(request):
    query = request.GET.get('q')  # Obtém o valor do parâmetro de consulta 'q' da URL
    categorias_distintas = Ferramentas.objects.values_list('categoria', flat=True).distinct()
    if query:
        # Realiza a pesquisa nos campos relevantes usando a cláusula Q para combinar múltiplos campos
        results = Ferramentas.objects.filter(
            Q(categoria__icontains=query) |          # Contém a categoria
            Q(nome_ferramenta__icontains=query) |    # Contém o nome da ferramenta
            Q(subcategoria__icontains=query) |       # Contém a subcategoria
            Q(tag_1__icontains=query) |              # Contém a tag_1
            Q(tag_2__icontains=query)                 # Contém a tag_2
        )
        paginator = Paginator(results, 12)  # 12 itens por página
        page_number = request.GET.get('page')
        page_ferramentas = paginator.get_page(page_number)
    else:
        results = Ferramentas.objects.none()  # Retorna uma queryset vazia se não houver consulta

    context = {
        'results': results,
        'query': query,
        'page_ferramentas': page_ferramentas,
        'categorias_distintas': categorias_distintas,
    }

    return render(request, 'search_results.html', context)

def ferramenta_detail(request, ferramenta_id):
    ferramenta = get_object_or_404(Ferramentas, id=ferramenta_id)
    categorias_distintas = Ferramentas.objects.values_list('categoria', flat=True).distinct()
    return render(request, 'ferramenta_detail.html', {'ferramenta': ferramenta,'categorias_distintas': categorias_distintas})

def categoria_view(request, categoria):
    ferramentas = Ferramentas.objects.filter(categoria=categoria)
    paginator = Paginator(ferramentas, 12)  # 12 itens por página
    page_number = request.GET.get('page')
    page_ferramentas = paginator.get_page(page_number)
    categorias_distintas = Ferramentas.objects.values_list('categoria', flat=True).distinct()
    context = {'ferramentas': ferramentas, 'categoria': categoria,'categorias_distintas': categorias_distintas, 'page_ferramentas': page_ferramentas,}
    return render(request, 'categoria.html', context,)

def all_categories_view(request):
    categorias_distintas = Ferramentas.objects.values_list('categoria', flat=True).distinct()
    return render(request, 'all_categories.html', {'categorias_distintas': categorias_distintas})