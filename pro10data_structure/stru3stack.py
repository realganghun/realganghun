stack = []
print('놀이 공원 입장')
print()

# 놀이 기구탈때의 기록남김
stack.append('T-express탑승')
print('기록 : ', stack)

stack.append('바이킹 탑승') # PUSH
print('기록 : ', stack)
# print(stack[1])

stack.append('회전목마')
print('기록 : ', stack)

# 가장 최근 기록 삭제
last_action = stack.pop() # POP
print('마지막 기록 취소 후 현재 : ', stack)

last_action = stack.pop() # POP
print('마지막 기록 취소 후 현재 : ', stack)

# LIFO를 class로 연습
class MyStack:
    def __init__(self, iterable=None):
        self._data = [] # __data : private
        if iterable is not None:
            for x in iterable:
                self.push(x)
    
    def push(self, x):
        # 맨 위(top)에 요소 추가
        self._data.append(x)
        return x
    
    def pop(self):
        # 맨 위(top)에 요소 제거
        if not self._data:
            raise IndexError('stack이 비었음')
        return self._data.pop()
    
    def __repr__(self): # 파이썬 실행 시 자동호출되는 특별 메소드
        top_to_bottom = list(reversed(self._data))
        return f'Stack(top -> bottom {top_to_bottom})'
    
    def is_empty(self):
        return not self._data       # 비었을때 True 반환.


def demo1Func():
    s = MyStack()
    for item in ['A', 'B', 'C', 'D', 'E']:
        s.push(item)
        print(f'push {item} -> ', s)
    # print(s._data)
    print('LIFO에 따라 하나씩 추출')
    while not s.is_empty():
        print(f'pop {item} -> ', s.pop(), "현재는 : ", s)

def demo2Func(text : str) -> str:
    s = MyStack(text)
    out = [] # 뒤집힌 문자 기억
    while not s.is_empty():
        out.append(s.pop())
    return ''.join(out)

if __name__ == '__main__':
    demo1Func()
    print(demo2Func('Python is good'))