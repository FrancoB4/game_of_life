from datetime import datetime as dt
from src.plane import Plane
from src.aux_functions import create_video
from os import system, path


def run(width, height, iterations):
    directory = dt.now().strftime('%d-%m-%Y__%H_%M_%S')
    system(f'mkdir {directory}')

    plane = Plane(width, height)

    plane.awake_random()

    for i in range(1, iterations + 1):
        population = 0
        for cell in plane.cells.values():
            cell.check_environment()

        for cell in plane.cells.values():
            cell.actualize_last_state()
            if cell.live:
                population += 1

        if population == 0:
            break

        plane.plot(i, directory, width, height, color='white', background_color='black')

        print(f'La población, tras {i} iteraciones es de {population}')

        # time.sleep(1)

    if not path.exists('./Exports/'):
        system('mkdir ./Exports')
    create_video(directory, iterations)
    system(f'sudo rm -fr {directory}')


if __name__ == '__main__':
    w = int(input('Ancho del universo: '))
    h = int(input('Largo del universo: '))
    input_iterations = int(input('Cuantas iteraciones deben realizarse: '))

    run(w, h, input_iterations)
