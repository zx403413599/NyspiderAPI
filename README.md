# NyspiderApi

#####1.IT桔子
```python
from spider.itjuzi import *

inves=investevents(page=1)#国内投资信息
mergerdata=merger(pahe=1)#国内并购信息
foreign_inves=foreign_investevents(page=1)#国外投资信息
foreign_mergerdata=foreign_merger(page=1)#国外并购信息

```

#####2.拉勾网职位信息
```python
from spider.lagou import *

jobs=lagouJobs(page=1,keyword='')
```

#####3.猫眼电影
```python

from spider.maoyan import *

data=boxoffice(day='2016-05-03')#电影票房
movie=movieinfor(url='http://piaofang.maoyan.com/movie/247575?_v_=yes')#电影具体信息

```

#####4.人人贷散标信息
```python

from spider.renrendai import *

username='Your username'
passwd='xxx'#加密后的密码
work=Renrendai(username,passwd)
loaninfor=work.getLoan(loanid=80000)

```
