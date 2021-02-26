import execjs

with open('translate.js', 'r') as f:
    jscode = f.read()
jsobj = execjs.compile(jscode)  # 根据jscode创建编译对象
sign = jsobj.eval('e("girl")')  # eval是把一个字符串当作表达式来执行

print(sign)
