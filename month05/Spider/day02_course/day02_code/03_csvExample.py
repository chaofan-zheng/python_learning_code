"""
csv模块示例
"""
import csv

with open('fengyun.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([('聂风', '血饮狂刀', '梦'), ('步惊云', '绝世好剑', '楚楚')])

f = open('fengyun.csv', 'a')
writer = csv.writer(f)
writer.writerow(['秦霜', '天霜泉', '孔慈'])
f.close()
