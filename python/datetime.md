# datetime

```
import datetime

start_time = datetime.datetime.now()
print(start_time)
```
## replace

자기 자신 바꾸려면 별도 지정해주어야함
```
ellie_birthday = start_time.replace(year = 2022, month = 2, day = 9)
print(ellie_birthday)
```


# 시간이 얼마나 남았는지?
```
how_long = ellie_birthday - datetime.datetime.now()
print(type(how_long))

print(how_long.days)

print(how_long.seconds)


print("2월 9일까지는 {}일 {}시간이 남았습니다".format(how_long.days, how_long.seconds//3600))
```