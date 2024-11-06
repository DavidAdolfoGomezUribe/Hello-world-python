import random

# Inicialización de puntajes
Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0

# Preguntas y respuestas
quiz = [
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options": [
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Entras en un jardín encantado. ¿Qué sería lo que más le interesaría examinar primero?:",
        "options": [
            {
                "statement": "Las setas gordas rojas que parecen estar hablando entre sí",
                "answer": "Ravenclaw"
            },
            {
                "statement": "El estanque burbujeante, en cuyas profundidades se arremolina algo luminoso",
                "answer": "Gryffindor"
            },
            {
                "statement": "El árbol de hojas de plata con manzanas doradas.",
                "answer": "Slytherin"
            },
            {
                "statement": "La estatua de un viejo mago con un extraño centelleo en los ojos.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Si pudieras escoger una habilidad mágica, ¿cuál elegirías?:",
        "options": [
            {
                "statement": "La capacidad de resolver problemas complejos con facilidad y rapidez.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "La habilidad para inspirar valentía y liderar a otros en tiempos de peligro.",
                "answer": "Gryffindor"
            },
            {
                "statement": "La capacidad de manipular a los demás para conseguir tus objetivos.",
                "answer": "Slytherin"
            },
            {
                "statement": "La capacidad de hacer el bien sin esperar nada a cambio.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Estás en un torneo de magia y te enfrentan a otro mago. ¿Cómo te preparas para el combate?:",
        "options": [
            {
                "statement": "Estudias cuidadosamente la técnica de tu oponente antes de actuar.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Te lanzas a la batalla con valentía, sin miedo de lo que pueda ocurrir.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Observas sus debilidades y planificas cómo derrotarlo con astucia.",
                "answer": "Slytherin"
            },
            {
                "statement": "Te concentras en mantener la calma y la integridad, sin hacerle daño innecesario.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Si tuvieras que elegir entre salvar a una persona o conseguir un gran poder, ¿qué escogerías?:",
        "options": [
            {
                "statement": "Elegirías salvar a la persona, sin importar las consecuencias para ti.",
                "answer": "Hufflepuff"
            },
            {
                "statement": "Elegirías el poder, porque crees que con él podrías hacer mucho bien.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Elegirías el poder, porque crees que solo con él podrías asegurar tu éxito.",
                "answer": "Slytherin"
            },
            {
                "statement": "Elegirías salvar a la persona, pero pensando en las consecuencias futuras.",
                "answer": "Ravenclaw"
            },
        ]
    }
]
1

# Función para mostrar las opciones
def options(list):
    numeral = 0
    plantilla = ""
    while numeral < 4:
        plantilla += f"""\t {numeral+1}. {list[numeral].get("statement")} \n"""
        numeral += 1
    return plantilla

# Proceso del cuestionario
for value in quiz:
    print(f""" 
    {value.get("question")}

       {options(value.get("options"))}
    """)

    number = int(input("\t Ingrese su respuesta: "))
    
    if not (number > 0 and number < 5):
        print("Ingrese un número válido entre 1 y 4.")
    else:
        # Actualiza los puntajes según la respuesta
        match value.get("options")[number-1].get("answer"):
            case "Gryffindor":
                Gryffindor += 1
            case "Hufflepuff":
                Hufflepuff += 1
            case "Slytherin":
                Slytherin += 1
            case "Ravenclaw":
                Ravenclaw += 1

# Muestra los puntajes
print("\nResultados:")
print("    Gryffindor: ", Gryffindor)
print("    Hufflepuff: ", Hufflepuff)
print("    Slytherin: ", Slytherin)
print("    Ravenclaw: ", Ravenclaw)

# Determina la casa con el mayor puntaje
max_points = max(Gryffindor, Hufflepuff, Slytherin, Ravenclaw)

# Almacena las casas con el puntaje máximo
houses_with_max_points = []
if Gryffindor == max_points:
    houses_with_max_points.append("Gryffindor")
if Hufflepuff == max_points:
    houses_with_max_points.append("Hufflepuff")
if Slytherin == max_points:
    houses_with_max_points.append("Slytherin")
if Ravenclaw == max_points:
    houses_with_max_points.append("Ravenclaw")

# Selecciona aleatoriamente entre las casas con el mismo puntaje
chosen_house = random.choice(houses_with_max_points)

# Imprime el resultado
print(f"\n     Pertenece a la casa {chosen_house} \n")
1
