import cryptor
with open('aid20101106am-0.ts','rb') as res:
    try:
        for line in res:
            content = res.readline().decode()
    except:
        pass
    print(content)