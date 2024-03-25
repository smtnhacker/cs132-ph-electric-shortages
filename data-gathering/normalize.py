import os
import sys
import traceback
import unicodedata
import ast
import emoji

def normalize_line(line: str):
    try:
        string = ast.literal_eval(line).decode()
    except Exception:
        string = ''
    no_endline = string.replace('\n', ' ')
    no_unicode_letters = unicodedata.normalize('NFKC', no_endline)
    no_emoji = emoji.replace_emoji(no_unicode_letters, replace='')

    return no_emoji

def normalize(inp):
    lines = inp.split('\n')
    return '\n'.join([normalize_line(line) for line in lines])

def main(index):
    try:
        print(f'Opening {index}')
        with open(os.path.join('data', 'raw', f'{index}.txt')) as f:
            content = f.read()
        normalized = normalize(content)
        print('--normalized')
        with open(os.path.join('data', 'normalized', f'{index}.txt'), 'w+', encoding='utf-8') as f:
            f.write(normalized)
        print('--saved')
    except Exception as e:
        print(e)
        print(traceback.format_exc())

if __name__ == '__main__':
    # main('batelec2.lipa')
    for file in os.listdir(os.path.join('data', 'raw')):
        try:
            main(file[:-4])
        except Exception:
            pass