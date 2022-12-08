import os
import PySimpleGUI as sg
import re
from chardet.universaldetector import UniversalDetector

def cvt_webnovel(from_filename, to_filename, del_indent):

    with open(from_filename, 'rb') as file:
        detector = UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break;
        detector.close()
        charcode = detector.result['encoding']
    print(charcode)

    with open(from_filename, 'r', encoding=charcode) as file:
        lines = file.readlines()

    with open(to_filename, 'w', encoding=charcode) as file:
        for line in lines:
            line = line[0].replace(' ', '　') + line[1:]
            if( line[0] == '　' and del_indent):
                line = line[1:]
            line = re.sub('[\n\r\n]', '', line)
            if line == '':
                file.write('\n')
            else:
                file.write(f'{line}\n\n')

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