lista = [1,2,3,4,5,6]
tupla = (1,2,3,4,5,6)

x,y = (12, 24)

dic = {
    "name": "1tdcpa",
    "year": 2025,
    "alunos": 27
}

print("-----------------------")

print(dic)

# dic["periodo"] = "diurno"
dic.update(
    periodo="diurno"
)

print(dic)

print("-----------------------")

for chave, valor in dic.items():
    print(f"{chave}: {valor}")

print("-----------------------")

for item in dic.values():
    print(item)

print("-----------------------")

