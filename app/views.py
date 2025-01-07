from django.shortcuts import render
from django.http import JsonResponse
from app.models import Book
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_new_book_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        book = Book.objects.create(
            titulo = data.get("titulo"),
            ano_pub = data.get("ano_pub"),
            autor = data.get("autor"),
            numero_paginas = data.get("numero_paginas"),
        )
        book.save()
        return JsonResponse({"message":"Livro criado com sucesso"})
    
@csrf_exempt
def get_books_view(request,id):
    if request.method == "GET":
        book = Book.objects.get()
        data = {
            "titulos":book.titulo,
            "ano_pub":book.ano_pub,
            "autor":book.autor,
            "numero_paginas":book.numero_paginas
        }
        return JsonResponse(data)