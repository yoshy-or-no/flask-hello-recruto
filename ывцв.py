from graphviz import Digraph


def generate_as_is_diagram(output_file="as_is_econ_diagram"):
    dot = Digraph(format='png')
    dot.attr(rankdir='TB', size='10')

    # Узлы процесса
    dot.node("Start", "Начало", shape="ellipse", style="filled", fillcolor="lightgreen")
    dot.node("DataCollection", "Сбор данных вручную\n(Excel, ERP, отчеты)", shape="box")
    dot.node("Processing", "Обработка данных вручную\n(аналитики сводят данные, расчеты)", shape="box")
    dot.node("Reporting", "Формирование отчетов вручную\n(Excel, BI-системы)", shape="box")
    dot.node("Decision", "Принятие решений\n(руководство анализирует отчеты)", shape="diamond")
    dot.node("End", "Конец", shape="ellipse", style="filled", fillcolor="lightcoral")

    # Связи между узлами
    dot.edge("Start", "DataCollection")
    dot.edge("DataCollection", "Processing")
    dot.edge("Processing", "Reporting")
    dot.edge("Reporting", "Decision")
    dot.edge("Decision", "End", label="Принято")
    dot.edge("Decision", "Processing", label="Требуется уточнение")

    # Сохранение и рендеринг
    dot.render(output_file, format="png", cleanup=False)
    print(f"Диаграмма сохранена в {output_file}.png")


# Генерация диаграммы
if __name__ == "__main__":
    generate_as_is_diagram()