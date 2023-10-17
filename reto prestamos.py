https://replit.com/join/tuzyrzlljm-jose-abrahamab9

#num1
cantidad = float(input("ingrese la cantidad del prestamo: "))
tasa_de_interes = float(input("ingrese la catidad del interes anual(%): "))
cantidad_del_prestamo_en_años = float(input("ingrese la cantidad del prestamo en años: "))


#calcular el nivel de riesgo
nivel_riesgo: "bajo riesgo" if tasa_interes <= 5 and plazo <=5 else "riesgo moderado"


#monto total
monto_total = cantidad + cantidad * (tasa_interes/100) * plazo

#resultados
print(f"nivel de riesgo del prestamo: {nivel_riesgo}")
print(f"monto total a pagar: ${monto_total:.2f}")
