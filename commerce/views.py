from django.shortcuts import render
from .models import Products
from .forms import ProductsForm

# Create your views here.

def index(request):
    total_products = Products.objects.count()
    context = {
        'total_products' : total_products,
    }
    return render(request, "commerce/index.html",context)


# def aluno_editar(request,id):
#     aluno = get_object_or_404(Aluno,id=id)
   
#     if request.method == 'POST':
#         form = AlunoForm(request.POST,instance=aluno)

#         if form.is_valid():
#             form.save()
#             return redirect('aluno_listar')
#     else:
#         form = AlunoForm(instance=aluno)

#     return render(request,'aluno/form_aluno.html',{'form':form})


# def aluno_remover(request, id):
#     aluno = get_object_or_404(Aluno, id=id)
#     aluno.delete()
#     return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'


# def aluno_criar(request):
#     if request.method == 'POST':
#         form = AlunoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = AlunoForm()
#     else:
#         form = AlunoForm()

#     return render(request, "aluno/form_aluno.html", {'form': form})


# def aluno_listar(request):
#     alunos = Aluno.objects.all()
#     context ={
#         'alunos':alunos
#     }
#     return render(request, "aluno/alunos.html",context)