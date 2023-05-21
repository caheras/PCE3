import csv
import matplotlib.pyplot as plt
import telebot

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


def show_stars(input_file):
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

    plt.show()

#show_stars('constellations/stars.csv')


def show_constellation(input_file, input_file2):
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

    # Display the plot
    plt.show()

#show_constellation('constellations/stars.csv', Hydra)


def show_all(input_file, input_file2, input_file3, input_file4, input_file5, input_file6, input_file7, input_file8, input_file9):
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
    plt.show()

show_all('constellations/stars.csv', OsaMenor, OsaMayor, Hydra, Geminis, Cygnet, Cazo, Casiopea, Boyero)

def constellation_caller(constellation):
    if constellation == 'OsaMenor':
        show_constellation('constellations/stars.csv', OsaMenor)
    elif constellation == 'OsaMayor':
        show_constellation('constellations/stars.csv', OsaMayor)
    elif constellation == 'Hydra':
        show_constellation('constellations/stars.csv', Hydra)
    elif constellation == 'Geminis':
        show_constellation('constellations/stars.csv', Geminis)
    elif constellation == 'Cygnet':
        show_constellation('constellations/stars.csv', Cygnet)
    elif constellation == 'Cazo':
        show_constellation('constellations/stars.csv', Cazo)
    elif constellation == 'Casiopea':
        show_constellation('constellations/stars.csv', Casiopea)
    elif constellation == 'Boyero':
        show_constellation('constellations/stars.csv', Boyero)
    else:
        print('No existe esa constelación')
