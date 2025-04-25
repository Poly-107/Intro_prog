# pida al usuario que ingrese su sueldo y defina el monto de impuesto de segunda categoria que
# debe pagar al SII 

"""
$ 922.132   	$ 2.049.180    2,20%
$ 2.049.181	    $ 3.415.300	   4,52%
$ 3.415.301  	$ 4.781.420	   7,09%
$ 4.781.421    	$ 6.147.540    10,62%
$ 6.147.541     $ 8.196.720    15,57%
$ 8.196.721        Y MAS       27,48%
"""

def definir_impuesto(sueldo):
    sueldo_int = int(sueldo)
    impuesto = 0
    if sueldo_int >= 8196721:
        impuesto = (sueldo_int * (100/27.48))
        print(f"con su sueldo de ${sueldo} usted debe pagar ${round(impuesto,2)} en impuestos")
    elif sueldo_int >= 6147541 and sueldo_int <= 8196720:
        impuesto = (sueldo_int * (100/15.57))
        print(f"con su sueldo de ${sueldo}, usted debe pagar ${round(impuesto,2)} en impuestos")
    elif sueldo_int >= 4781421 and sueldo_int <= 6147540:
        impuesto = (sueldo_int * (100/10.62))
        print(f"con su sueldo de ${sueldo}, usted debe pagar ${round(impuesto,2)} en impuestos")
    elif sueldo_int >= 3415301 and sueldo_int <= 4781420:
        impuesto = (sueldo_int * (100/7.09))
        print(f"con su sueldo de ${sueldo}, usted debe pagar ${round(impuesto,2)} en impuestos")
    elif sueldo_int >= 2049181 and sueldo_int <= 3415300:
        impuesto = (sueldo_int * (100/4.52))
        print(f"con su sueldo de ${sueldo}, usted debe pagar ${round(impuesto,2)} en impuestos")
    elif sueldo_int >= 922132 and sueldo_int <= 2049180:
        impuesto = (sueldo_int * (100/2.20))
        print(f"con su sueldo de ${sueldo}, usted debe pagar ${round(impuesto,2)} en impuestos")
    else:
        print(f"El impuesto de segunda categoria a pagar con el sueldo {sueldo_int} es: ${impuesto}")


    
sueldo_ingresado = int(input("ingrese su sueldo: "))

definir_impuesto(sueldo_ingresado)

print()