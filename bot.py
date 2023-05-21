import csv
import matplotlib
import matplotlib.pyplot as plt
import telebot
import io
from IPython.display import display, Math
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly
import sympy as sp
matplotlib.use('Agg')

input_file = 'constellations/stars.txt'  # Relative path to the input .txt file
output_file = 'constellations/stars.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
        data = [line.replace(';', '') for line in file]

with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows([row.split() for row in data])

# Replace whitespaces with commas
with open(output_file, 'r') as file:
        content = file.read()
        content = content.replace(' ', ',')

with open(output_file, 'w') as file:
        file.write(content)

print(f"{input_file} has been successfully converted to {output_file}.")


input_file = 'constellations/OsaMenor.txt'  # Relative path to the input .txt file
output_file = 'constellations/OsaMenor.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")


input_file = 'constellations/OsaMayor.txt'  # Relative path to the input .txt file
output_file = 'constellations/OsaMayor.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

input_file = 'constellations/Hydra.txt'  # Relative path to the input .txt file
output_file = 'constellations/Hydra.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

input_file = 'constellations/Geminis.txt'  # Relative path to the input .txt file
output_file = 'constellations/Geminis.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

input_file = 'constellations/Cygnet.txt'  # Relative path to the input .txt file
output_file = 'constellations/Cygnet.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

input_file = 'constellations/Cazo.txt'  # Relative path to the input .txt file
output_file = 'constellations/Cazo.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

input_file = 'constellations/Casiopea.txt'  # Relative path to the input .txt file
output_file = 'constellations/Casiopea.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

input_file = 'constellations/Boyero.txt'  # Relative path to the input .txt file
output_file = 'constellations/Boyero.csv'  # Relative path to the output .csv file

with open(input_file, 'r') as file:
    data = [line.strip().split() for line in file]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{input_file} has been successfully converted to {output_file}.")

OsaMenor = 'constellations/OsaMenor.csv'
OsaMayor = 'constellations/OsaMayor.csv'
Hydra = 'constellations/Hydra.csv'
Geminis = 'constellations/Geminis.csv'
Cygnet = 'constellations/Cygnet.csv'
Cazo = 'constellations/Cazo.csv'
Casiopea = 'constellations/Casiopea.csv'
Boyero = 'constellations/Boyero.csv'

def show_FGO(f, chat_id):
    n=15
    z = parse_expr('z')
    f =  parse_expr(f)
    print(display(Math(sp.latex(f))))
    Fz=Poly(f.series(x=z, x0=0, n=15).removeO())
    fn=Fz.all_coeffs()
    bot.send_message(chat_id, 'Sucesión, o secuencia, generada por la FGO, F(z) \n'+str(fn[::-1]))

def show_stars(chat_id):
    input_file = 'constellations/stars.csv'
    x_coordinates = []
    y_coordinates = []
    brightness = []
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            x_coordinates.append(float(row[0]))
            y_coordinates.append(float(row[1]))
            brightness.append(float(row[4]))

    # Set the background color to black
    plt.figure(facecolor='black')
    plt.gca().set_facecolor('black')  # Set background color within the plot area
    # Add grid to the graph
    plt.grid(True, color='gray', linestyle='--', linewidth=0.2)
    # Generate a random color for each point
    plt.scatter(x_coordinates, y_coordinates, s=brightness, c='white', zorder=10)

    plt.xlabel('X', color='white')  # Set x-axis label color to white
    plt.ylabel('Y', color='white')  # Set y-axis label color to white
    plt.title('Estrellas', color='white')  # Set title color to white
    plt.xticks(color='white')  # Set x-axis tick labels color to white
    plt.yticks(color='white')  # Set y-axis tick labels color to white

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)


    bot.send_photo(chat_id, buf)


    buf.truncate(0)
    buf.seek(0)
    plt.clf()

def show_constellation(input_file, input_file2,chat_id):
    constelacion = []

    with open(input_file2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion.extend(row)
    
    for i in range (0, len(constelacion)):
        print(constelacion[i])

    x_coordinates = []
    y_coordinates = []
    
    for i in range (0, len(constelacion)):   
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)     
            for row in csv_reader:
                if constelacion[i] in row:
                    x_coordinates.append(float(row[0]))
                    y_coordinates.append(float(row[1]))
                    print(row)

    x_coordinates_stars = []
    y_coordinates_stars = []
    brightness_stars = []
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            x_coordinates_stars.append(float(row[0]))
            y_coordinates_stars.append(float(row[1]))
            brightness_stars.append(float(row[4]))

    # Set the background color to black
    plt.figure(facecolor='black')

    # Add grid to the graph
    plt.grid(True, color='gray', linestyle='--', linewidth=0.2)

    plt.gca().set_facecolor('black')  # Set background color within the plot area
    # Add grid to the graph

    plt.scatter(x_coordinates_stars, y_coordinates_stars, s=brightness_stars, c='white', zorder=10)

    # Plot the points
    plt.scatter(x_coordinates, y_coordinates, color='Red',s=10, zorder =20)

    # Draw connections between points
    for i in range(0, len(x_coordinates) - 1, 2):
        plt.plot([x_coordinates[i], x_coordinates[i+1]], [y_coordinates[i], y_coordinates[i+1]], color='blue')

    # Set plot title and labels
    plt.title('Constelación', color='white')
    plt.xlabel('X Coordinate', color='white')
    plt.ylabel('Y Coordinate', color='white')

    # Set text color to white
    plt.xticks(color='white')
    plt.yticks(color='white')

    # Display the bot
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)


    bot.send_photo(chat_id, buf)


    buf.truncate(0)
    buf.seek(0)
    plt.clf()

def show_all(chat_id):
    input_file = 'constellations/stars.csv'
    input_file2 = 'constellations/OsaMenor.csv'
    input_file3 = 'constellations/OsaMayor.csv'
    input_file4 = 'constellations/Hydra.csv'
    input_file5 = 'constellations/Geminis.csv'
    input_file6 = 'constellations/Cygnet.csv'
    input_file7 = 'constellations/Cazo.csv'
    input_file8 = 'constellations/Casiopea.csv'
    input_file9 = 'constellations/Boyero.csv'
    
    constelacion1 = []
    constelacion2 = []
    constelacion3 = []
    constelacion4 = []
    constelacion5 = []
    constelacion6 = []
    constelacion7 = []
    constelacion8 = []

    with open(input_file2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion1.extend(row)
    
    with open(input_file3, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion2.extend(row)
    
    with open(input_file4, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion3.extend(row)

    with open(input_file5, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion4.extend(row)

    with open(input_file6, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion5.extend(row)
    
    with open(input_file7, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion6.extend(row)

    with open(input_file8, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion7.extend(row)
    
    with open(input_file9, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            constelacion8.extend(row)
    
    x_coordinates1 = []
    y_coordinates1 = []

    x_coordinates2 = []
    y_coordinates2 = []

    x_coordinates3 = []
    y_coordinates3 = []

    x_coordinates4 = []
    y_coordinates4 = []

    x_coordinates5 = []
    y_coordinates5 = []

    x_coordinates6 = []
    y_coordinates6 = []

    x_coordinates7 = []
    y_coordinates7 = []

    x_coordinates8 = []
    y_coordinates8 = []

    for i in range (0, len(constelacion1)):   
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)     
            for row in csv_reader:
                if constelacion1[i] in row:
                    x_coordinates1.append(float(row[0]))
                    y_coordinates1.append(float(row[1]))
                    print(row)   

    for i in range (0, len(constelacion2)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion2[i] in row:
                    x_coordinates2.append(float(row[0]))
                    y_coordinates2.append(float(row[1]))
                    print(row)
    
    for i in range (0, len(constelacion3)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion3[i] in row:
                    x_coordinates3.append(float(row[0]))
                    y_coordinates3.append(float(row[1]))
                    print(row)
    
    for i in range (0, len(constelacion4)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion4[i] in row:
                    x_coordinates4.append(float(row[0]))
                    y_coordinates4.append(float(row[1]))
                    print(row)
    
    for i in range (0, len(constelacion5)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion5[i] in row:
                    x_coordinates5.append(float(row[0]))
                    y_coordinates5.append(float(row[1]))
                    print(row)
    
    for i in range (0, len(constelacion6)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion6[i] in row:
                    x_coordinates6.append(float(row[0]))
                    y_coordinates6.append(float(row[1]))
                    print(row)

    for i in range (0, len(constelacion7)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion7[i] in row:
                    x_coordinates7.append(float(row[0]))
                    y_coordinates7.append(float(row[1]))
                    print(row)
    
    for i in range (0, len(constelacion8)):
        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if constelacion8[i] in row:
                    x_coordinates8.append(float(row[0]))
                    y_coordinates8.append(float(row[1]))
                    print(row)

    x_coordinates_stars = []
    y_coordinates_stars = []
    brightness_stars = []
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            x_coordinates_stars.append(float(row[0]))
            y_coordinates_stars.append(float(row[1]))
            brightness_stars.append(float(row[4]))
    
    
    # Set the background color to black
    plt.figure(facecolor='black')

    # Add grid to the graph
    plt.grid(True, color='gray', linestyle='--', linewidth=0.2)

    plt.gca().set_facecolor('black')  # Set background color within the plot area
    # Add grid to the graph

    plt.scatter(x_coordinates_stars, y_coordinates_stars, s=brightness_stars, c='white', zorder=10)

    # Plot the points
    plt.scatter(x_coordinates1, y_coordinates1, color='Red',s=10, zorder =20)

    plt.scatter(x_coordinates2, y_coordinates2, color='Cyan',s=10, zorder =20)

    plt.scatter(x_coordinates3, y_coordinates3, color='Green',s=10, zorder =20)

    plt.scatter(x_coordinates4, y_coordinates4, color='Yellow',s=10, zorder =20)

    plt.scatter(x_coordinates5, y_coordinates5, color='Orange',s=10, zorder =20)

    plt.scatter(x_coordinates6, y_coordinates6, color='Purple',s=10, zorder =20)

    plt.scatter(x_coordinates7, y_coordinates7, color='Pink',s=10, zorder =20)

    plt.scatter(x_coordinates8, y_coordinates8, color='Brown',s=10, zorder =20)

    # Draw connections between points
    for i in range(0, len(x_coordinates1) - 1, 2):
        plt.plot([x_coordinates1[i], x_coordinates1[i+1]], [y_coordinates1[i], y_coordinates1[i+1]], color='blue')

    for i in range(0, len(x_coordinates2) - 1, 2):
        plt.plot([x_coordinates2[i], x_coordinates2[i+1]], [y_coordinates2[i], y_coordinates2[i+1]], color='blue')

    for i in range(0, len(x_coordinates3) - 1, 2):
        plt.plot([x_coordinates3[i], x_coordinates3[i+1]], [y_coordinates3[i], y_coordinates3[i+1]], color='blue')

    for i in range(0, len(x_coordinates4) - 1, 2):
        plt.plot([x_coordinates4[i], x_coordinates4[i+1]], [y_coordinates4[i], y_coordinates4[i+1]], color='blue')
    
    for i in range(0, len(x_coordinates5) - 1, 2):
        plt.plot([x_coordinates5[i], x_coordinates5[i+1]], [y_coordinates5[i], y_coordinates5[i+1]], color='blue')
    
    for i in range(0, len(x_coordinates6) - 1, 2):
        plt.plot([x_coordinates6[i], x_coordinates6[i+1]], [y_coordinates6[i], y_coordinates6[i+1]], color='blue')
    
    for i in range(0, len(x_coordinates7) - 1, 2):
        plt.plot([x_coordinates7[i], x_coordinates7[i+1]], [y_coordinates7[i], y_coordinates7[i+1]], color='blue')
    
    for i in range(0, len(x_coordinates8) - 1, 2):
        plt.plot([x_coordinates8[i], x_coordinates8[i+1]], [y_coordinates8[i], y_coordinates8[i+1]], color='blue')

    # Set plot title and labels
    plt.title('Constelación', color='white')
    plt.xlabel('X Coordinate', color='white')
    plt.ylabel('Y Coordinate', color='white')

    # Set text color to white
    plt.xticks(color='white')
    plt.yticks(color='white')

    # Display the plot
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)


    bot.send_photo(chat_id, buf)


    buf.truncate(0)
    buf.seek(0)
    plt.clf()

def constellation_caller(constellation, chat_id):
    if constellation == 'OsaMenor':
        show_constellation('constellations/stars.csv', OsaMenor, chat_id)
    elif constellation == 'OsaMayor':
        show_constellation('constellations/stars.csv', OsaMayor, chat_id)
    elif constellation == 'Hydra':
        show_constellation('constellations/stars.csv', Hydra, chat_id)
    elif constellation == 'Geminis':
        show_constellation('constellations/stars.csv', Geminis, chat_id)
    elif constellation == 'Cygnet':
        show_constellation('constellations/stars.csv', Cygnet, chat_id)
    elif constellation == 'Cazo':
        show_constellation('constellations/stars.csv', Cazo, chat_id)
    elif constellation == 'Casiopea':
        show_constellation('constellations/stars.csv', Casiopea, chat_id)
    elif constellation == 'Boyero':
        show_constellation('constellations/stars.csv', Boyero, chat_id)
    else:
        bot.send_message(chat_id, 'No se encontró la constelación')

def solve_recurrence(coeffs, initial_conditions, chat_id):
    n = sp.Symbol('n')
    recurrence_func = sp.Function('a')

    # # Prompt user for coefficients and initial conditions
    # coeffs = input("Enter the coefficients of the recurrence relation separated by spaces: ").split()
    # initial_conditions = input("Enter the initial conditions separated by spaces: ").split()

    # # Validate the number of coefficients and initial conditions
    # while len(coeffs) != len(initial_conditions):
    #     print("Error: The number of coefficients must match the number of initial conditions.")
    #     initial_conditions = input("Enter the initial conditions separated by spaces: ").split()

    # Convert input to integers1
    coeffs = list(map(int, coeffs))
    initial_conditions = list(map(int, initial_conditions))

    # Create the recurrence relation equation
    eq = sp.Eq(recurrence_func(n), sum(coeffs[i] * recurrence_func(n-i-1) for i in range(len(coeffs))))

    # Solve the recurrence relation
    recurrence_sol = sp.rsolve(eq, recurrence_func(n), initial_conditions)

    # Generate the non-recurrent expression
    nonrecurrent_expr = recurrence_sol.subs(recurrence_func(n), 'f(n)').simplify()

    simplified_expr = nonrecurrent_expr.expand().simplify()

    # Print the results
    bot.send_message(chat_id, "La versión no recurrente de la función ingresada es: {}".format(simplified_expr))
    return recurrence_sol, nonrecurrent_expr





bot = telebot.TeleBot("6290021120:AAHeGG0nPcD_w-X_rKfstw7Zp2Td_qtoSmE")
TOKEN = '6290021120:AAHeGG0nPcD_w-X_rKfstw7Zp2Td_qtoSmE'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """¡Hola, soy tu bot juniorista!, un bot que te ayudará aconocer las constelaciones y estrellas que se encuentran en el cielo, además de solucionar tus Relaciones de recurrencia.""")
    texto = 'Tengo varios comandos que puedes utilizar:\n\n'
    texto += '/ayuda❓: Te mostrará los comandos que puedes utilizar.\n'
    texto += '/stars🌟: Te mostrará las estrellas que se encuentran en el cielo.\n'
    texto += '/constelacion🌌: Te mostrará la constelacion que elijas el cielo.\n'
    texto += '/constelaciones🌠🌌🌠: Te mostrará todas las constelaciones que se encuentran en el cielo.\n'
    texto += '/recurrencia📚: Te mostrará la solución de la recurrencia que elijas.\n'
    texto += '/FGO#️⃣: Te mostrará la secuencia de la funcion generadora que quieras\n'
    texto += '<b>JUNIOR TU PAPA</b> ⚪️🔴🦈\n'
    bot.send_message(message.chat.id, texto, parse_mode='HTML')

@bot.message_handler(commands=['ayuda'])
def send_welcome(message):
    bot.reply_to(message, "Instrucciones del bot:")
    texto = '/stars🌟: Te mostrará las estrellas que se encuentran en el cielo.\n'
    texto += '/constelacion🌌: Te mostrará la constelacion que elijas el cielo.\n'
    texto += '/constelaciones🌠🌌🌠: Te mostrará todas las constelaciones que se encuentran en el cielo.\n'
    texto += '/recurrencia📚: Te mostrará la solución de la recurrencia que elijas.\n'
    texto += '/FGO#️⃣: Te mostrará la secuencia de la funcion generadora que quieras\n'
    texto += '<b>JUNIOR TU PAPA</b> ⚪️🔴🦈\n'
    bot.send_message(message.chat.id, texto, parse_mode='HTML')


@bot.message_handler(commands=['stars'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Aqui tienes todas las estrellas en el cielo")
    show_stars(chat_id)

@bot.message_handler(commands=['constelaciones'])
def send_welcome(message):
    chat_id =  message.chat.id
    bot.reply_to(message, "Aqui tienes todas las constelaciones en el cielo")
    show_all(chat_id)
    

@bot.message_handler(commands=['constelacion'])
def obtener_nombre(message):
    chat_id = message.chat.id
    def function_caller(m):
        nombre = m.text.strip()
        bot.send_message(chat_id, f"Aqui está la constelación de {nombre}")
        constellation_caller(nombre, chat_id)

    texto = ' ⚪️🔴 <b>Lista de constelaciones: ⚪️🔴 </b>\n'
    texto += '<b>Boyero</b>\n'
    texto += '<b>Casiopea</b>\n'
    texto += '<b>Cazo</b>\n'
    texto += '<b>Cygnet</b>\n'
    texto += '<b>Geminis</b>\n'
    texto += '<b>Hydra</b>\n'
    texto += '<b>OsaMayor</b>\n'
    texto += '<b>OsaMenor</b>\n'

    bot.send_message(chat_id, texto, parse_mode="html")
    bot.send_message(chat_id, "Por favor, ingresa un nombre:")
    bot.register_next_step_handler(message, function_caller)
     
@bot.message_handler(commands=['FGO'])
def send_welcome(message):
    chat_id = message.chat.id
    def function_caller(m):
        f = m.text.strip()
        bot.send_message(chat_id, f"'Sucesión, o secuencia, generada por la FGO, F(z) \n'{f}")
        show_FGO(f, chat_id)
    
    bot.send_message(chat_id, "Digita la FGO F(z)=")
    bot.register_next_step_handler(message, function_caller)

@bot.message_handler(commands=['recurrencia'])
def obtener_nombre(message):
    chat_id = message.chat.id

    def input_revision1(m):
        global coeffs
        coeffs = m.text.split()
        if len(coeffs) == 0:
            bot.send_message(chat_id, "Debe ingresar al menos un coeficiente.")
            bot.send_message(chat_id, "Ingrese los coeficientes de la relación de recurrencia separados por espacios: ")
            bot.register_next_step_handler(m, input_revision1)
        else:
            bot.send_message(chat_id, "Ingrese las condiciones iniciales separadas por espacios: ")
            bot.register_next_step_handler(m, input_revision2)

    def input_revision2(m):
        global initial_conditions
        initial_conditions = m.text.split()
        if len(initial_conditions) != len(coeffs):
            bot.send_message(chat_id, "El número de condiciones iniciales debe ser igual al número de coeficientes.")
            bot.send_message(chat_id, "Ingrese las condiciones iniciales separadas por espacios: ")
            bot.register_next_step_handler(m, input_revision2)
        else:
            bot.send_message(chat_id, "Calculando la versión no recurrente de la función ingresada...")
            solve_recurrence(coeffs, initial_conditions, chat_id)


    bot.send_message(chat_id, "Ingrese los coeficientes de la relación de recurrencia separados por espacios: ")
    bot.register_next_step_handler(message, input_revision1)




if __name__ == '__main__':
    print("Bot is running...")
    bot.polling()
