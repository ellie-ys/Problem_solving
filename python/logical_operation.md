# 논리연산

코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정

- test1과 test2 왜 차이가 날까?
  test2에서 첫번째값이 false여서 그것만 보고 전체가 false라 간주
  python에서는 and or연산에서 더이상 실행할 필요가 없으면 실행안한다.

```
def return_false():
	print("함수 return_false")
	return False
def return_true():
	print("함수 return_true")
	return True


print("test1")
#함수 return_false
#함수 return_true 모두 다 출력
a = return_false()
b = return_true()

if a and b :
	print(True)
else :
	print(False)


print("test2")
#함수 return_false만 출력
if return_false() and return_true():
	print("True")
else:
	print("False")
```

### 아니네

'''
dic = {'key2':'Value1'}
if 'key1' in dic and dic['key1'] =='Value1' :
print('Key1도 있고, 그 값은 Value1이네')
else:
print('아니네')
'''

### KeyError: 'key1'

'''
dic = {'key2':'Value1'}
if dic['key1'] =='Value1' and 'key1' in dic :
print('Key1도 있고, 그 값은 Value1이네')
else:
print('아니네')
'''
