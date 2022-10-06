import os
import PySimpleGUI as sg

def cvt_webnovel(from_filename, to_filename, del_indent):
    
    with open(from_filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    with open(to_filename, 'w', encoding='utf-8') as file:
        for line in lines:
            if(line != ''):
                line = line[0].replace(' ', '　') + line[1:]
                if( line[0] == '　' and del_indent):
                    line = line[1:]
                file.write(f'{line}\n\n')
            else:
                file.write('\n')



layout = [
    [sg.Checkbox('字下げ削除', default=False, key='del_indent')],
    [sg.Text('変換元'), sg.InputText(), sg.FileBrowse(file_types=(('txtファイル', '*.txt'),), key='from')],
    [sg.Text('変換先'), sg.InputText(), sg.FileSaveAs(file_types=(('txt', '*.txt'),), key='to')],
    [sg.Submit('変換'), sg.Cancel('やめる')],
]


window = sg.Window('ウェブ小説用の改行挿入と字下げ削除', layout)
while True:
    event, values = window.read()

    if event in [None, 'やめる']:
        break

    if(values['from'] != '' and values['to'] != '' and event == '変換'):
        cvt_webnovel(values['from'], values['to'], values['del_indent'])
        sg.popup_ok('変換しました')

window.close()