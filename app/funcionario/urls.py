from django.urls import path
from .views import FuncionarioList, FuncionarioMethodObject, SetorList, SetorMethodObject

urlpatterns = [
    path('funcionarios/', FuncionarioList.as_view()),
    path('funcionario/<int:id>', FuncionarioMethodObject.as_view()),
    path('setores/', SetorList.as_view()),
    path('setor/<int:id>', SetorMethodObject.as_view()),

]