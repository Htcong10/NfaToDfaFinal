from io import StringIO
import xml.etree.ElementTree as ET
from ReadNfaFile import *
def inputFile():
       print('Hãy nhập vào địa chỉ file Jflag: ')
       link1 = input()
       file_object = open(link1)  # demo.jff is file'name which located in the same folder as the project
       xml = file_object.read()
       xml_file = StringIO(xml)
       tree = ET.parse(xml_file)
       root = tree.getroot()
       _tran, _state_start,_state_final= readFile(root)
       return _tran, _state_start,_state_final
#format transiton
def format(_tran):
 for x in _tran.values():
    for y in x.keys():
        for z in x.values():
           if x[y] == 'null':
              x[y] =['n']
 return _tran
def dOuble(tran):
    a=str()
    for x in tran.values():
        for y in x.keys():
            if len(x[y])>1:
                for item in x[y]:
                    if item !=x[y][-1]:
                        a=a+item+' '
                    else:
                        a=a+item
                x[y]=[a]
    return tran

def writeFile():
 _tran, _state_start,_state_final= inputFile()
 _tran= format(_tran)
 _tran = dOuble(_tran)
 _tran = format(_tran)
 with open('test.txt', "w") as t:
    t.write(str(_state_start) + '\n')
    for text in _state_final:
        if text != _state_final[-1]:
            t.write(text + ' ')
        else:
            t.write(text)
    t.write('\n')
    for x in _tran.keys():
        for item in _tran[x]['0,1']:
            if item != 'n':
                _tran[x]['0'] = item.split()
                _tran[x]['1'] = item.split()
        for item in _tran[x]['0']:
            if item == 'n':
                t.write(x + ' ' + '0' + '\n')
            else:
                t.write(x + ' ' + '0' + ' ' + item + '\n')
        for item in _tran[x]['1']:
            if item != 'n':
                t.write(x + ' ' + '1' + ' ' + item + '\n')
            else:
                t.write(x + ' ' + '1' + '\n')
        for item in _tran[x]['e']:
            if item != 'n':
                t.write(x + ' ' + 'e' + ' ' + item + '\n')