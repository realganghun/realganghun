#클래스는 새로운 타입을 만들어 자원을 공유 가능

# class Singer:
#     title_song = "시스템서울 컴퓨터에 바이러스를 심어버려"

#     def sing(self):
#         msg = "대표곡"
#         print(msg, self.title_song)
from ex22singer import Singer #아니면 import ex22singer로 해도 되는데, 이때는 아래 코드의 Singer를 ex22singer.Singer로 바꿔줘야 함

kimbo = Singer() #생성자 호출해서 객체 생성 후 주소를 bts라는 변수에 치환 --> 이거 이해 안되네 좀 찾아봐야겠다
kimbo.sing()
print(type(kimbo))

kimbo.title_song = "Festival Music"
kimbo.sing()

kimbo.company = 'DirtyPlay Music'

print('레이블 : ', kimbo.company)

sikk = Singer()
sikk.sing()
print(type(sikk))

#sikk.title_song = "또다시보여줘야대"
sikk.sing()

sikk.company = 'KC'
print('소속사 : ', sikk.company)

Singer.title_song = '내 음악은 독립해'
kimbo.sing()
sikk.sing()

niceGroup = sikk
niceGroup.sing()