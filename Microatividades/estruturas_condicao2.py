tempoExperiencia = 10 #variavel que indica o tempo de experiência em numero.

if tempoExperiencia <2 : #se o tempo de experiencia for menor que dois anos
    print("nivel de conhecimento junior")
elif tempoExperiencia >= 2  and tempoExperiencia <= 5: #se o tempo de experiencia for entre dois a cinco anos
    print("nivel de conhecimento pleno") 
else: #acima de 5 anos
    print("nivel de conhecimento senior")
