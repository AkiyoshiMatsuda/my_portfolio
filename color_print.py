colorlist=["black","red","green","yellow","blue","purple","cyan","white","gray"]
colordict=[
    {"name":"black","code1":"\033[30m","code2":"\033[0m"},
    {"name":"red","code1":"\033[31m","code2":"\033[0m"},
    {"name":"green","code1":"\033[32m","code2":"\033[0m"},
    {"name":"yellow","code1":"\033[33m","code2":"\033[0m"},
    {"name":"blue","code1":"\033[34m","code2":"\033[0m"},
    {"name":"purple","code1":"\033[35m","code2":"\033[0m"},
    {"name":"cyan","code1":"\033[36m","code2":"\033[0m"},
    {"name":"white","code1":"\033[37m","code2":"\033[0m"},
    {"name":"gray","code1":"\033[90m","code2":"\033[0m"},
]
def color_print(text,colorname):
    for color in colordict:
        if color["name"]==colorname:
            if color["name"]=="black":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="red":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="green":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="yellow":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="blue":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="purple":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="cyan":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="white":
                text=color["code1"]+text+color["code2"]
                return text
            elif color["name"]=="gray":
                text=color["code1"]+text+color["code2"]
                return text
    return print(f"{colorname}はありません")

#color_print("色を付けたいテキスト", "つけたい色の名前")とすると