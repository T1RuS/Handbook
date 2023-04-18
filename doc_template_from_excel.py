from pathlib import Path
from docxtpl import DocxTemplate
import pandas as pd

base_dir = Path(__file__).parent   # Папка с расположением скрипта, данных, шаблона и папки куда сохранять
excel_path = base_dir / 'data.xlsx'  # Путь до данных
word_template_path = base_dir / 'template.docx'  # Путь до шаблона
output_dir = base_dir / 'Сертификаты'  # Путь до папки куда сохранять полученные записи

# Загрузка данных из data.xlsx и листа с название Сертификаты для 1го этапа в dataframe - df
df = pd.read_excel(excel_path, sheet_name='Сертификаты для 1го этапа')

# Проходим циклом по каждой строке
for row in df.to_dict(orient='records'):
    doc = DocxTemplate(word_template_path)  # Создаем базу для документа
    doc.render(row)  # Загружаем данные из строки в word документ
    output_path = output_dir / f'{row["ФИО"]}.docx'  # Полный путь сохранения с названием файла
    doc.save(output_path)  # Сохранение файла
