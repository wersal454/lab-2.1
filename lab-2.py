height = int(input("Напишите ваш рост(м): "))
mass = int(input("Напишите ваш вес(кг): "))
steps = int(input("Сколько шагов вы сегодня прошли: "))
time = int(input("Сколько заняла времени тренировка(мин): "))


def countTrainingCost(M, H, S, T):
    distance = S * (H / 4 + 0.37)
    speed = int(distance / T)
    energy = int(0.035 * M + (speed ** 2 / H) * 0.029 * M)

    if distance <= 2000:
        text = 'Молодец!'
    elif distance <= 4000:
        text = 'Двойной молодец'
    elif distance > 4000:
        text = 'Долой холодец! Тройной молодец'

    return distance, energy, text


print(f"Дистанция(м) - калории:{countTrainingCost(mass, height, steps, time)}")