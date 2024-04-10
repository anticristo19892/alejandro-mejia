def obtener_ganador_escrutinio(votos_candidatos):
    max_votos = max(votos_candidatos.values())
    ganadores = [candidato for candidato, votos in votos_candidatos.items() if votos == max_votos]
    return ganadores
candidatos = ["Candidato Andres", "Candidato Baltazar", "Candidato Camilo"]
votos_candidatos = {candidato: 0 for candidato in candidatos}
num_electores = 200
for _ in range(num_electores):
    voto = int(input("carlos 40 votos, baltazar 40 votos camilos 120 votos (1, 2 o 3): "))
    if 1 <= voto <= 3:
        votos_candidatos[candidatos[voto - 1]] += 1  # Restar 1 para ajustar el índice
ganadores = obtener_ganador_escrutinio(votos_candidatos)
print("Resultados del escrutinio:")
for candidato, votos in votos_candidatos.items():
    print(f"{candidato}: {votos} votos")
    if len(ganadores) == 1:
        print(f"\nEl ganador por mayoría simple es: {ganadores[0]}")
    else:
        print("\nHubo un empate entre los siguientes candidatos:")
        for ganador in ganadores:
            print(ganador)