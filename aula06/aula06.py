nota = float(input("Qual é sua nota"))
if nota <= 0 or nota >10 :
    print (nota)
elif nota >=9:
   print("aprovado")
elif nota >=7:
   print("Recupeção")
else:
   print("Reprovado")
