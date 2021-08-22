a=input("Nome completo do funcionário:")
b=float(input("Salário atual:"))
c=float(input("Quantos anos o coloborador trabalha conosco?"))
soma=b/97*100
somab=b/87.5*100
somac=b/80*100
if c==3 or c<3:
    print("Senhor(a) {} seu salário era de R${:.2f} agora será de R$ {:.2f}".format(a,b,soma))
if c>3 and c<10:
    print("Senhor(a) {} seu salário era de R$ {:.2f} agora será de R$ {:.2f}".format(a,b,somab))
if c>10:
    print("Senhor(a) {} seu salário era de R${:.2f} agora será de R${:.2f}".format(a,b,somac))

