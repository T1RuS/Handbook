import os
from pathlib import Path
import re
import sys
import argparse
from progress.bar import IncrementalBar

BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    path_name: str = input('Путь к файлу с моделями:')

    with open(path_name, 'r', encoding='utf8') as f:
        models_list: list[str] = re.findall(r'(?<=class )(.+?)(?=\(Base)', f.read())

    bar = IncrementalBar('Создание папок и файлов', max=len(models_list))

    for model in models_list:
        path = os.path.join(BASE_DIR, model)
        try:
            os.mkdir(path)
            with open(f'{path}/{model}.sql', 'w') as f:
                pass

            with open(f'{path}/{model}.xlsx', 'w') as f:
                pass
        except:
            pass

        bar.next()

    bar.finish()
    path_name: str = input('Нажмите любую кнопку...')
