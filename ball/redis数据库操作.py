import redis
import time


'''
一 、对数据库和键进行操作
'''
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
# r.lpush('one_list','a','b','c')
# r.lpush('two_list','a','b','c')
# r.lpush('three_list','a','b','c')
# r.lpush('four_list','a','b','c')
# r.lpush('five_list','a','b','c')


#1、查询0号数据库里面所有的key值，以列表型式返回
# all_key = r.keys('*')
# print(all_key)

#2、按照条件查询数据库里面的key值,*类似于正则里面的通配符
# key_01 = r.keys('*''list')#所有以list结尾的key
# key_02 = r.keys('one''*')#所有以one开头的key
# print(key_01,'\n',key_02)

# 3、判断key键名是否存在，存在返回1，不存在返回0
# an = r.exists('two_list')
# print(an)

# 4、删除一个指定键
# r.delete('three_list')
# print(r.keys("*"))

# 5、设置键名为one_list的过期时间为10秒,就是10秒之后删除
# r.expire('two_list',3600)
# time.sleep(11)
# print(r.keys("*"))

# 6、查看键名为0为one_list 的过期时间
# 当 key 不存在时，返回 -2 。
# 当 key 存在但没有设置剩余生存时间时，返回 -1 。
# 否则，以秒为单位，返回 key 的剩余生存时间。
# an = r.ttl('two_list')
# print(an)

# 7、将0号数据库的key转移到1号库中
r_01=redis.Redis(host='127.0.0.1',port=6379,db=1)
# r.move('four_list',1)
# print(r_01.keys('*'))

# 8、移除过期时间
# r.persist('two_list')
# an = r.ttl('two_list')
# print(an)

# 9、删除所有数据，清空当前库
# r.flushdb()
# print(r.keys("*"))

# 10、清空所有数据 ，所有库
# r.flushall()
# print(r_01.keys('*'))

r_02 = redis.Redis(host='127.0.0.1',port=6379,db=2)

'''
二、字符串类型命令操作
'''

# （1）redis子串类型，key存在则覆盖，不存在则创建
# 1、增
# r_02.set('姓名','张三')
# r_02.set('姓名','李四')

# 2、查  获取一个键
# an = r_02.get('姓名').decode('utf-8')
# print(an)

# 3、设置一个不存在的键和值，防止覆盖，存在则返回False，表示创建失败
# anan = r_02.setnx('年龄',18)
# print(anan)

# 4、设置指定键和值的有效时间，单位时间秒,定时10秒后自动删除
# 不写间的时间相当于set
# r_02.setex('姓名',10,'李四')

# 5、替换子字符串，（替换长度由子字符串决定）
#中间数字表示开始替换的字符串的所以位置，
# 意思是从第几个开始，后面的66表示换成的数字多出来的按照起始点依次往后替换
# 超过原有长度的新增加
# r_02.setrange('年龄',0,66)

# 6、批量设置键和值，成功返回Ture
# ok_01 = r_02.mset({'姓名':'anan', '年龄': '22' ,'性别': '男'})
# print(ok_01)

# 7、批量设置不存在的值，成功返回Ture
# ok_02 =r_02.msetnx({'姓名_01':'张三', '年龄_01': 22 ,'身高': 180})
# print(ok_02)

# 8、获取原来的值，并设置新值
# ok_03 = r_02.getset('姓名','安可爱')
# print(ok_03.decode('utf-8'))
# print(r_02.get('姓名').decode('utf-8'))

# 9、获取指定范围的值,一个汉字占3个索引值，一个英文字母和数字各占1个索引值，
# 范围少了报错，超出字符串长度不报错，并且包含开头和结尾
# ok_03 =r_02.getrange('姓名',0,1)
# print(ok_03.decode('utf-8'))

# 10、批量获取键值,指定键值
# ok_04 = r_02.mget('姓名','年龄','性别')
# for i in ok_04:
#     print(i.decode('utf-8'))

# 11、对指定键值做加加操作，返回加后的结果
# 仅限于数字，默认每次加1个单位，可设置,但只能是整型
# ok_05 = r_02.incr('年龄',amount=2)
# print(ok_05)

# 12、对指定键值做减减操作，返回减后的结果
# 跟加加一样，都是一个道理
# ok_06 = r_02.decr('年龄',amount=3)
# print(ok_06)

# 13、在某个键上减上指定值，可以是正整数，也可以是负整数
# ok_07 = r_02.decrby('年龄',-5)
# print(ok_07)

# 14、在指定键的值上追加字串，返回的是字符串的长度
# r_02.append('年龄','年轻')


# 15、求指定键的值的长度,数字字母占1个位，汉字占3个位
# ok_08 = r_02.strlen('年龄')
# print(ok_08)

'''
三、redis哈希类型Hash  相关操作
redis hash 是一个string类型的filed 和 value 的映射表，
hash特别适用存储对象
'''
r_03 = redis.Redis(port=6379,host='localhost',db=3)
# 1、设置一个哈希表的键和值
# r_03.hset('哈希','年龄',18)
# r_03.hset('哈希','姓名','安丽娇')
# r_03.hset('哈希','性别','女')

# 2、获取hash表里面的键对应的值，
# 返回的是bytes类型，所以要转下码
# ok_01 = r_03.hget('哈希','年龄').decode('utf-8')
# print(ok_01)

# 3、设置一个哈希表中不存在的键和值，
# 存在返回0，表示创建失败，成功返回1
# ok_02= r_03.hsetnx('哈希','爱吃','巧乐兹')
# print(ok_02)

# 4、批量设置键和值
# r_03.hmset('哈希',{'发型':'漂亮短发','相貌':'明眸皓齿'})

# 5、批量获取哈希表中键对应的值
# ok_03 = r_03.hmget('哈希','姓名','年龄','相貌')
# for i in ok_03:
#     print(i.decode('utf-8'))

# 6、判断键值是否存在，存在返回True,不存在返回False
# ok_04 = r_03.hexists('哈希','姓名_01')
# print(ok_04)

# 7、获取哈希表中键的数量
# ok_05 = r_03.hlen('哈希')
# print(ok_05)

# 8、删除哈希表中的指定键
# r_03.hdel('哈希','爱吃')

# 9、查询哈希表中的所有键
# ok_06 = r_03.hkeys('哈希')
# for i in ok_06:
#     print(i.decode('utf-8'))
# 10、查询哈希表中的所有值
# ok_07 = r_03.hvals('哈希')
# for i in ok_07:
#     print(i.decode('utf-8'))
# 11、查询哈希表中的所有键和对应的值
# ok_08 = r_03.hgetall('哈希')
# for i in ok_08:
#     print(i.decode('utf-8'),ok_08[i].decode('utf-8'))

'''
list列表类型(双向链表结构)操作
redis列表是一个简单的字符串列表，按照插入顺序排序，
你可以添加一个元素到列表的头部（左边）或者尾部（右边）
'''

r_04 = redis.Redis(host='localhost',port=6379,db=4)
# 1、在左边添加一个字符串lpush,右边rpush
# r_04.lpush('爱吃','布丁')
# r_04.rpush('爱吃','辣条')

# 2、获取列表中的内容，利用索引
# ok_01 = r_04.lrange('爱吃',0,-1)#从头到尾,都包含
# for i in ok_01:
#     print(i.decode('utf-8'))

# 3、在指定位置插入数据
# 从左边找，在出现的第一个辣条前面加上火锅
# r_04.linsert('爱吃', 'before', '巧乐兹','火锅')#前面
# r_04.linsert('爱吃','after','小蛋糕','烧烤')#后面

# 4、修改指定索引位置上的值
# r_04.lset('爱吃',2,'大蛋糕')

# 5、删除值，可指定前几个 ，后几个
# 从左往右找，删除前两个火锅，-2表示从右往左找
# r_04.lrem('爱吃',2,'火锅')
# r_04.lrem('爱吃',-2,'火锅')

# 6、删除值中的全部火锅
# r_04.lrem('爱吃',0,'火锅')

# 7、删除指定范围以外的所有数据
# r_04.ltrim('爱吃',1,3)

# 8、删除头部或者尾部元素
# r_04.lpop('爱吃')#删除头部
# r_04.rpop('爱吃')#尾部

# 9、根据索引位置获取元素
# ok_03 = r_04.lindex('爱吃',2).decode('utf-8')
# print(ok_03)

# 10、查看对应值的个数
# ok_04 = r_04.llen('爱吃')
# print(ok_04)

# 11、将表1的尾部元素移出到表2头部位置
# r_04.rpoplpush('爱吃','爱吃_01')

'''
# 五、集合类型操作
redis的set是string类型的无序集合，集合成员
是唯一的，这就意味着集合中不能出现重复数据
'''

r_05 = redis.Redis(host='localhost',port=6379,db=5)
# 1、向myset中添加一个元素，成功返回1，失败返回0
# ok_01 = r_05.sadd('myset_01','天生丽质','爱吃巧乐兹','爱吃辣条','勤劳','敬业','超级可爱')
# print(ok_01)

# 2、从myset中获取所有元素，结果是无序的
# ok_02 = r_05.smembers('myset')
# for i in ok_02:
#     print(i.decode('utf-8'))
# print(ok_02)

# 3、从myset中删除一个元素，成功返回1，失败返回0
# r_05.srem('myset','天生丽质')

# 4、随机删除并返回myset中的一个元素
# r_05.spop('myset')

# 5、随机获取一个数据，但是不删除
# ok_02 = r_05.srandmember('myset').decode('utf-8')
# print(ok_02)

# 6、将myset中的指定数据移到myset_01中
# r_05.smove('myset','myset_01','勤劳')

# 7、返回数据的个数
# ok_03 = r_05.scard('myset')
# print(ok_03)

# 8、判断数据是否存在于集合里,在返回Ture,不在返回Flase
# ok_04 = r_05.sismember('myset','天生丽质')
# ok_05 = r_05.sismember('myset','貌美如花')
# print(ok_04,ok_05)

# 9、返回所有集合的差集保存到新的集合dstset中
# r_05.sdiffstore('dstset','myset','myset_01')

# 10、返回N个集合中的交集
# new_set = r_05.sinter('myset','myset_01')
# print(new_set)

# 11、返回所有集合的交集保存到新的集合dstset中
# r_05.sinterstore('dstset','myset','myset_01')

# 12、返回所有集合的并集
# all_set = r_05.sunion('myset','myset_01','dstset')
# for i in all_set:
#     print(i.decode('utf-8'))

# 13、返回所有集合的并集，并存储到dstset中
# r_05.sunionstore('dstset_01','myset','myset_01')


'''
# （5）有序集合(sorted set)
Redis 有序集合和集合一样也是string类型元素的集合，且不允许重复的成员。
不同的是每个元素都会关联一个double类型的分数。
redis正是通过分数来为集合中的成员进行从小到大的排序。
有序集合的成员是唯一的，但分数(score)却可以重复。

'''
r_06 = redis.Redis(host='127.0.0.1',port=6379,db=6)

# 1、向zset中添加数据，用数字排序
# r_06.zadd('zset', {'安丽娇':1, '天生丽质':22})
# r_06.zadd('zset', {'貌美如花':11, '聪明伶俐':9})

# 2、删除指定元素
# r_06.zrem('zset','天生丽质')

# 3、如果'貌美如花'存在，则顺序增加2，
# 如果不存在，那么新添加一个，编号数字就是2
# r_06.zincrby('zset',2,'貌美如花')
# r_06.zincrby('zset',2,'貌美')

# 4、返回数据在zset集合中的排名，从小到大,从0开始排
# ok_01= r_06.zrank('zset','貌美如花')
# print(ok_01)

# 5、返回数据在集合里的排名从大到小
# ok_02 = r_06.zrevrank('zset','天生丽质')
# print(ok_02)

# 6、根据score排序（从小到大）
# ok_03 = r_06.zrange('zset',0,-1,withscores=False)
# for i in ok_03:
#     print(i.decode('utf-8'))
# print(ok_03)

# 7、根据score排序（从大到小）
# ok_04 = r_06.zrevrange('zset',0,-1,withscores=False)
# for i in ok_04:
#     print(i.decode('utf-8'))
# print(ok_04)

# 8、返回集合中score分数在给定区间内的元素包含开头和结尾
# ok_05 = r_06.zrangebyscore('zset',2,4,withscores=False)#包含2和4
# for i in ok_05:
#     print(i.decode('utf-8'))
# print(ok_05)

# 9、返回集合中给定区间的数量
# ok_06 = r_06.zcount('zset',2,15)#包含2和15
# print(ok_06)

# 10、返回集合中元素的个数
# ok_07 = r_06.zcard('zset')
# print(ok_07)

# 11、返回指定元素的分数score
# ok_08 = r_06.zscore('zset','安丽娇')
# print(ok_08)

# 12、删除集合中排名在给定区间的元素,从0开始排
# r_06.zremrangebyrank('zset',1,10)

# 13、删除zset中从小到大排序结果的score分数在9到18置间的删除
# r_06.zremrangebyscore('zset',9,18)