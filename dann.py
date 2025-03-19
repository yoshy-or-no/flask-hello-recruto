import pandas as pd
from scipy.stats import pearsonr

# Загружаем файл
file_path = "Данные.xlsx"
df_data = pd.read_excel(file_path, sheet_name="данные")

# Убираем колонку "Вопрос"
df_numeric = df_data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Определяем количество вопросов
num_questions = df_numeric.shape[0]

# Определяем группы
group_M = [i for i in range(0, num_questions, 3)]
group_N = [i for i in range(1, num_questions, 3)]
group_P = [i for i in range(2, num_questions, 3)]

# Рассчёт средних
mean_group_M = df_numeric.iloc[group_M].mean().mean()
mean_group_N = df_numeric.iloc[group_N].mean().mean()
mean_group_P = df_numeric.iloc[group_P].mean().mean()

# Корреляции
corr_M_N, _ = pearsonr(df_numeric.iloc[group_M].mean(axis=1), df_numeric.iloc[group_N].mean(axis=1))
corr_M_P, _ = pearsonr(df_numeric.iloc[group_M].mean(axis=1), df_numeric.iloc[group_P].mean(axis=1))
corr_N_P, _ = pearsonr(df_numeric.iloc[group_N].mean(axis=1), df_numeric.iloc[group_P].mean(axis=1))

# Альфа Кронбаха
item_variances = df_numeric.var(axis=1, ddof=1)
total_variance = df_numeric.sum(axis=0).var(ddof=1)
cronbach_alpha = (num_questions / (num_questions - 1)) * (1 - (item_variances.sum() / total_variance))

# Вывод результатов
print("Средние значения по группам:", mean_group_M, mean_group_N, mean_group_P)
print("Корреляции:", corr_M_N, corr_M_P, corr_N_P)
print("Альфа Кронбаха:", cronbach_alpha)