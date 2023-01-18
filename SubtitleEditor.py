import os, re

#设置默认样式和英语样式
Style = 'Style: Default,微软雅黑,22,&H00DEDEDE,&HF0000000,&H00111211,&H00000000,0,0,0,0,100,100,0,0,1,2.25,1.5,2,5,5,5,1' 
EngStyle = r'\\N{\\c&H62a8eb&\\fs13}'

#主函数
def main():
    #获取文件并逐个打开
    path = os.path.abspath('.')
    filelist = os.listdir(path)
    filelist.remove('SubtitleEditor.py')
    #print (filelist)
    #正则
    findDefault = re.compile(r'Style: Default.*')
    findEng = re.compile(r'\\N.*}')
    for filename in filelist:
        #尝试utf-8和utf-16
        try:
            with open(filename,'r+', encoding='utf-8') as file:
                text = file.read()
                #text = text.replace('}}', '>')
                #print(file.read())
                #print(re.findall(findDefault, text))
                #print(re.findall(findEng, text))
                new = re.sub(findDefault, Style, text)
                new = re.sub(findEng, EngStyle, text)
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(new)
        except:
            with open(filename,'r+', encoding='utf-16') as file:
                text = file.read()
                #print(file.read())
                #print(re.findall(findDefault, text))
                #print(re.findall(findEng, text))
                new = re.sub(findDefault, Style, text)
                new = re.sub(findEng, EngStyle, text)
            with open(filename, 'w', encoding='utf-16') as file:
                file.write(new)

main()