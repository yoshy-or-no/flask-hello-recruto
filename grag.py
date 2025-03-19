import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Проверяем наличие файла Excel в доступной директории
file_path = "Данные.xlsx"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Файл {file_path} не найден. Убедитесь, что он загружен в систему.")

# Загружаем данные из файла Excel
df_raw = pd.read_excel(file_path, sheet_name="Опросные данные")

# Убираем колонку "Вопрос" и переводим данные в числовой формат
df_data = df_raw.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Рассчёт статистики
mean_per_question = df_data.mean()  # Среднее по каждому вопросу
std_per_question = df_data.std()  # Стандартное отклонение

# Рассчёт средних по трём группам
group_M = [7, 13, 19, 1, 4, 16, 22, 10, 25]
group_N = [5, 11, 2, 23, 8, 20, 17, 14, 26]
group_P = [15, 3, 12, 24, 9, 21, 27, 18, 6]

mean_group_M = df_data.iloc[group_M].mean().mean()
mean_group_N = df_data.iloc[group_N].mean().mean()
mean_group_P = df_data.iloc[group_P].mean().mean()

# Проверяем соответствие количества вопросов и средних значений
num_questions_actual = len(df_raw["Вопрос"].astype(str))
num_questions_mean = len(mean_per_question)

if num_questions_actual > num_questions_mean:
    df_raw = df_raw.iloc[:num_questions_mean]
elif num_questions_actual < num_questions_mean:
    mean_per_question = mean_per_question.iloc[:num_questions_actual]

# Перестроим диаграммы
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Столбцовая диаграмма (Средние значения по группам)
axes[0, 0].bar(["Манипуляция (М)", "Нарциссизм (Н)", "Психопатия (П)"],
               [mean_group_M, mean_group_N, mean_group_P],
               color=['#ff9999', '#66b3ff', '#99ff99'])
axes[0, 0].set_title("Средние значения по группам")
axes[0, 0].set_ylabel("Средний балл")

# 2. Секторная диаграмма (Распределение средних значений по группам)
axes[0, 1].pie([mean_group_M, mean_group_N, mean_group_P],
               labels=["Манипуляция (М)", "Нарциссизм (Н)", "Психопатия (П)"],
               autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99'], startangle=140)
axes[0, 1].set_title("Доля средних значений по группам")

# 3. Столбцовая диаграмма (Средние значения по вопросам)
axes[1, 0].bar(df_raw["Вопрос"].astype(str), mean_per_question.values, color='skyblue')
axes[1, 0].set_title("Средние значения по вопросам")
axes[1, 0].set_ylabel("Средний балл")
axes[1, 0].set_xticks(range(len(df_raw["Вопрос"])))
axes[1, 0].set_xticklabels(df_raw["Вопрос"].astype(str), rotation=90, fontsize=8)

# 4. Лепестковая диаграмма (Средние значения по вопросам)
angles = np.linspace(0, 2 * np.pi, len(mean_per_question), endpoint=False).tolist()
values = list(mean_per_question.values) + [mean_per_question.values[0]]
angles += angles[:1]

ax = plt.subplot(2, 2, 4, polar=True)
ax.fill(angles, values, color="skyblue", alpha=0.4)
ax.plot(angles, values, color="blue", linewidth=2)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(df_raw["Вопрос"].astype(str), fontsize=8)
ax.set_title("Средние значения по вопросам (Лепестковая диаграмма)")

plt.tight_layout()
plt.show()
