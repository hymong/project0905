from minus import Minus
from multiply import Multiply
from divide import Divide
from sum import add
a = int(input("첫번째 숫자를 입력하세요: "))
b = int(input("두번째 숫자를 입력하세요: "))

print("덧셈값:", add(a,b))
print("뺼셈값:", Minus(a,b))
print("곱셈값:", Multiply(a,b))    
print("나눗셈값:", Divide(a,b)) 