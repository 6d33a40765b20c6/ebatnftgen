import os
import random
import sys
from json import loads as jl
from secrets import token_hex
from PIL import Image
from colorama import init,Fore
F = Fore
init()
os.system('cls')
#не удаляй 

bb = f'''{F.RED}
▄▄▄ .▄▄▄▄·  ▄▄▄· ▄▄▄▄▄ ▐ ▄ ·▄▄▄▄▄▄▄▄ ▄▄ • ▄▄▄ . ▐ ▄ 
▀▄.▀·▐█ ▀█▪▐█ ▀█ •██  •█▌▐█▐▄▄·•██  ▐█ ▀ ▪▀▄.▀·•█▌▐█
▐▀▀▪▄▐█▀▀█▄▄█▀▀█  ▐█.▪▐█▐▐▌██▪  ▐█.▪▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
▐█▄▄▌██▄▪▐█▐█ ▪▐▌ ▐█▌·██▐█▌██▌. ▐█▌·▐█▄▪▐█▐█▄▄▌██▐█▌
 ▀▀▀ ·▀▀▀▀  ▀  ▀  ▀▀▀ ▀▀ █▪▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪                                                                                                                         
{F.BLUE}        by https://lolz.guru/members/2977610

'''
#не удаляй 
print(bb)#не удаляй 
#не удаляй 
if not os.path.isdir('./src'):os.mkdir('src');print(F.RED+'Исходники в папке "src" ненайдены...');sys.exit(0)
if not os.path.isdir('./output'):os.mkdir('output')
if not os.path.exists('all.gen'):open('all.gen','w')
try:_C = dict(jl(open('config.json','r+').read()))    
except:print('Ошибка при чтении файла config.json');sys.exit(0)

def _A(photo):
    if photo not in [_c.replace('\n','') for _c in open('all.gen','r+').readlines()]:return True
    return False

def get(fl):
    for root,f,file in os.walk(fl,followlinks=False):return root+'/'+random.choice(file)  
    
def gen():
    _l = 1000;_q = 0;photo = []
    while True:
        _ph = []
        for fl in _C:ph = get('src/'+_C[fl]);_ph.append(ph)
        if _A(':'.join(_ph)):print(':'.join(_ph),file=open('all.gen','a+'));photo.append(_ph)
        else:
            if _q >= _l and ( photo==[]):print(F.RED+"К сожалению, я не могу создать больше уникальных артов :(");break
            elif _q>= _l and not photo==[]:break
            _q+=1 
    if photo == []:return False
    else:return photo
    



def paste():
    photo = gen()
    if photo:
        print(F.GREEN+'Кол-во комбо:',len(photo))
        for ph in photo:
            phs = ([Image.open(p,'r') for p in ph])
            bg = Image.new('RGBA', phs[0].size, (0, 0, 0, 0))
            bg.paste(phs[0],(0,0))
            for pha in phs[1:]:
                x,y = pha.size
                bg.paste(pha,(0,0,x,y),mask=pha)
            bg.save(f'output/{token_hex(6)}.png', format="png")
            bg.close()
        os.system('explorer output')

if __name__ == '__main__':
    i = input(F.MAGENTA+'Удалить старые данные о комбо? (enter-No,other-Yes) ')
    if i != '':open('all.gen','w')
    paste()
    try:input(F.LIGHTRED_EX+'Нажмите ЭнТэР ')
    except:pass
    

