import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *
print('Setup complete.')

tuites = ["Wow, what a great day today!! #sunshine","I feel sad about the things going on around us. #covid19","I'm really excited to learn Python with @JovianML #zerotopandas","This is a really nice song. #linkinpark","The python programming language is useful for data science","Why do bad things happen to me?","Apple announces the release of the new iPhone 12. Fans are excited.","Spent my day with family!! #happy","Check out my blog post on common string operations in Python. #zerotopandas","Freecodecamp has great coding tutorials. #skillup"]
#todos os tuites do banco de dados estão posicionados nos arrays acima
numero_de_tuites = len(tuites)
print (numero_de_tuites )
tuite_corrigidos = [tuites.upper() for tuites in tuites] #ideia de normalizar todos os tuites para que não tenham problemas com letras maiusculas e minusclas 


#catalogar todas as palvras que podem limar as letras, e deixa-las em maiusculo 
palavras_do_bem = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
palavras_do_bem_corrigidas = [palavras_do_bem.upper() for palavras_do_bem in palavras_do_bem]
palavras_do_mal =['sad', 'bad', 'tragic', 'unhappy', 'worst']
palavras_do_mal_corrigidas = [palavras_do_mal.upper() for palavras_do_mal in palavras_do_mal]


#Variaveis auxiliares 
tuite_feliz = False 
tuite_triste = False
contador_de_tuites_felizes = 0 
contador_de_tuites_tristes = 0
contador_geral =0



for i in (tuite_corrigidos):
    for j in (palavras_do_bem_corrigidas):
        if  j  in i:
            print (i)
            tuite_feliz = True 
            contador_de_tuites_felizes = contador_de_tuites_felizes+1
            contador_geral = contador_geral + 1
        
print (contador_de_tuites_felizes)