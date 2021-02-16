import re

html = """<div class="animal">
    <p class="name">
			<a title="Tiger"></a>
    </p>
    <p class="content">
			Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
			<a title="Rabbit"></a>
    </p>

    <p class="content">
			Small white rabbit white and white
    </p>
</div>
"""
# 方法一
re_list = re.findall('<div class="animal">.*?<a title="(.*?)">.*?<p class="content">(.*?)</p>', html,re.S )
print(re_list)
for r in re_list:
    print("动物名称",r[0])
    print("动物描述",r[1].strip())
# 方法二
# 正则复制下来改

