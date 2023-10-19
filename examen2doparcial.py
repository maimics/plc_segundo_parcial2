#examen 2do parcial 

#datos iniciales
guia_semana = input("dia de la semana: ")
hora_actual = int(input("hora actual (en formato de 24 horas): "))
tipo_tarea= input("tipo de tarea estudio (estudio, deportes, descanso o trabajo): ")

#criterio 1
if 1 < hora_actual <= 5:
  print("debes estar dormido")
elif 5 < hora_actual < 14:
  print("debes estar en clases")
elif 14 <= hora_actual < 22:
  print("puedes hacer tareas")

#criterio2
if 18 < hora_actual < 22 and tipo_tarea == "descanso":
  print("ademas de tomar una siesta, puedes comenzar a realizar tus tareas")
