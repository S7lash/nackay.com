from django.shortcuts import render
from django.http import HttpResponse

tilte = "Nackay"
message = f"Bienvenu sur le site de {tilte} !"

def index(request):
    return HttpResponse(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{tilte}</title>
    </head>
    <body>
        <h1>{message}</h1>
    </body>
    </html>
    ''')
