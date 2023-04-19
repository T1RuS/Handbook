from xlsxtpl.writerx import BookWriter


def creating_excel_from_template(data, template_path):
    writer = BookWriter(template_path)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)
    payload = {'tpl_idx': 1, 'sheet_name': u'Лист1', 'ctx': data}
    writer.render_book2(payloads=[payload])
    writer.save('resaul.xlsx')


data = {'name': 'Текст',
        'loop': [{'id': 1, 'name': 'first'},
                 {'id': 2, 'name': 'second'},
                 {'id': 3, 'name': 'third'},
                 {'id': 4, 'name': 'fourth'},
                 {'id': 5, 'name': 'fifth'}]}
creating_excel_from_template(data=data, template_path='template.xlsx')
