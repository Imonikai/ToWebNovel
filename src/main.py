import os
import PySimpleGUI as sg

def to_webnovel_text(from_filename, to_filename):
    file = open(from_filename, 'r', encoding='utf-8')
    lines = file.read().splitlines()
    file.close()

    file = open(to_filename, 'w', encoding='utf-8')
    for line in lines:
        if( line != '' ):
            line = line[0].replace(' ', '　') + line[1:]
            if( line[0] == '　' ):
                line = line[1:]
            print(line)
            print()
            file.write(f'{line}\n\n')
    file.close()


layout = [
    [sg.Text('変換元'), sg.InputText(), sg.FileBrowse(file_types=(('txtファイル', '*.txt'),), key='from')],
    [sg.Text('変換先'), sg.InputText(), sg.FolderBrowse(key='to')],
    [sg.Submit('変換'), sg.Cancel('やめる')],
]


window = sg.Window('ウェブ小説用の改行挿入と字下げ削除', layout)
while True:
    event, values = window.read()

    if( values['from'] != '' and values['to'] != '' and event == '変換'):
        from_filename = values['from']
        to_path = values['to']
        basename = os.path.basename(from_filename)
        to_filename = f'{to_path}/webConv-{basename}'
        print(basename)
        to_webnovel_text(from_filename, to_filename)
        break

    if event in [None, 'やめる']:
        break

window.close()


