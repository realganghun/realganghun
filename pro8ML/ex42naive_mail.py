# 스팸 메일 분류기
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Multinomial Naive Bayes(다항 나이브 베이즈)

# 주로 텍스트 분류와 같은 다중 클래스 문제에 사용
# 단어의 존재 유무가 아닌 단어의 출현횟수를 Feature로 사용
# 아래의 가정을 기반으로 한다.
# 각 특성(단어 등)은 독립적으로 기여한다.
# 각 특성의 값은 다항 분포를 따른다.

# 학습용 데이터
texts = [
    "무료 쿠폰 지금 무료 클릭",
    "한번만 클릭하면 무료",
    "오늘 회의는 2시",
    "지금 할인 행사 진행 중",
    "회의 자료는 메일로 보내셈",
    "지금 바로 쿠폰 확인"
]

labels = ["spam", "spam", "ham", "spam", "ham", "spam"]

# 단어 등장 횟수 기반 벡터
vect = CountVectorizer() # 문서들로부터 단어의 단어 순서 정보는 버리고, 단어 빈도수 정보를 추출
x = vect.fit_transform(texts)
print(vect.get_feature_names_out())
print(x) #  (0, 2) : 문서 번호 / 2 : 등장 횟수
print(x.toarray())
# [[0 0 2 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0]
#  [0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0]
#  [1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1]
#  [0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0]
#  [0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 1 0]
#  [0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 0]]
print(vect.vocabulary_)
# {'무료': 2, '쿠폰': 9, '지금': 7, '클릭': 10, '한번만': 12, '클릭하면': 11,
# '오늘': 5, '회의는': 17, '2시': 0, '할인': 13, '행사': 14, '진행': 8,
# '회의': 16, '자료는': 6, '메일로': 1, '보내셈': 4, '바로': 3, '확인': 15}

# 모델
from sklearn.metrics import accuracy_score
model = MultinomialNB()
model.fit(x, labels)

pred = model.predict(x)
print('accuracy_score : ', accuracy_score(labels, pred)) # accuracy_score :  1.0

# 새로운 문장 테스트
test_text = ["무료 쿠폰 지금 선착순", "간부 회의는 언제 시작하나요?"]
x_test = vect.transform(test_text)
print(x_test)
#   Coords        Values
#   (0, 2)        1
#   (0, 7)        1
#   (0, 9)        1
#   (1, 17)       1

# 예측 + 확률 출력
preds = model.predict(x_test)
probs = model.predict_proba(x_test)
class_names = model.classes_ # ["spam", "ham"]

for text, pred, prob in zip(test_text, preds, probs):
    prob_str = ", ".join([f"{cls}:{p:.4f}" for cls, p in zip(class_names, prob)])
    print((f"'{text}' -> 예측 : {pred} / 확률 : [{prob_str}]"))