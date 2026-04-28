# 스팸 메일 분류기 - spam 자료를 파일에서 읽기
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import koreanize_matplotlib

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/mydata.csv")
print(df)
df['label'] = df['label'].str.strip().str.lower()
texts = df['text'].tolist()
labels = df['label'].tolist()

print(texts[:3])
print(labels[:3])

x_train, x_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42, stratify=labels)

# 벡터화
vectorizer = CountVectorizer()
x_train_vec = vectorizer.fit_transform(x_train) # 단어 사전을 만듦
x_test_vec = vectorizer.transform(x_test) # test 데이터는 fit_transform이 아닌, transform만 해야함!!

print('x_train_vec : ', x_train_vec)

model = MultinomialNB()
model.fit(x_train_vec, y_train)

y_pred = model.predict(x_test_vec)

acc = accuracy_score(y_test, y_pred)
print('분류 정확도 : ', acc) # 분류 정확도 :  0.8

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=['ham', 'spam'])
print(cm)
# [[2 1]
#  [0 2]]

# Confusion Matrix 시각화
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['ham', 'spam'])
disp.plot(cmap='Blues')
plt.title('Confusion Matrix(혼동 행렬)')
plt.show()

# 사용자 입력 메일 내용 분류
while True:
    userInput = input("이메일 내용 입력(종료는 q) : ")
    if userInput.lower() == 'q':
        break
    x_new = vectorizer.transform([userInput])
    proba = model.predict_proba(x_new)[0]
    spam_prob = proba[model.classes_.tolist().index('spam')]

    result = 'spam임' if spam_prob >= 0.7 else "ham임"
    print(f'spam 확률은 {spam_prob:.2f}, {result}.')