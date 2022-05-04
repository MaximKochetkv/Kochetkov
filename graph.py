import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
# Чтение файлов
with open("settings.txt", "r") as s_stream:
    time_delta, discr_level = [float(i) for i in s_stream.read().split()]
s_stream.close()

d_stream = open("data.txt", "r")
res = []
for line in d_stream:
    res.append(float(line))
d_stream.close()
# Расчет выхода
data = np.array(res)
data = data * discr_level
time = np.arange(0, len(data) * time_delta, time_delta)
# построение точек
plt.plot(time, data, label="Зависимость V(t)", ds="steps")
freq = 20
ax.scatter(time[::freq], data[::freq], label="Точечное представление", color='green', marker='8')
# Сетка
ax.minorticks_on()
ax.grid(which='major',
        color='black',
        linewidth=0.3)

ax.grid(which='minor',
        color='black',
        linestyle=':',
        linewidth=0.2)
# Легенда и название
ax.legend(title="Данные о графике:")
ax.set_xlabel('Время, сек.')
ax.set_ylabel('Напряжение, В.')
ax.set(xlim=(0, 15), ylim=(0, 3.5))
plt.title("Зарядка и разрядка RC-цепи")
# Зарядка Конденсатора
max_n = np.argmax(data)
ax.annotate("Время заряда: {0:.3} сек.".format(time_delta * max_n), xy=(8, 1.5))
# Разрядка конденсатора
ax.annotate("Время разряда: {0:.3} сек.".format(time_delta * (len(time) - max_n)), xy=(8, 1.3),)
# Сохранение и показ графика
plt.savefig("8.svg", format='svg')
plt.show()