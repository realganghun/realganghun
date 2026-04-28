from bs4 import BeautifulSoup


def normalize(username):
    return username.strip().lower()


# 팔로잉
def extract_following(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    return set(
        normalize(tag.text)
        for tag in soup.find_all("h2")
        if tag.text.strip()
    )


# 팔로워
def extract_followers(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    usernames = set()

    for a in soup.find_all("a"):
        username = a.text.strip()

        if username and "instagram.com" not in username:
            usernames.add(normalize(username))

    return usernames


# 실행
followers = extract_followers("followers_1.html")
following = extract_following("following.html")


# 비교
not_following_back = sorted(following - followers)
i_dont_follow_back = sorted(followers - following)
mutual_follow = sorted(following & followers)


# =========================
# 🔥 리스트 출력
# =========================

print("\n❌ 내가 팔로우했는데 안해주는 사람:")
for user in not_following_back:
    print(user)

print("\n⚠️ 나를 팔로우했는데 내가 안한 사람:")
for user in i_dont_follow_back:
    print(user)



# =========================
# 요약
# =========================
print("\n====== 요약 ======")
print(f"안해주는 사람: {len(not_following_back)}명")
print(f"내가 안한 사람: {len(i_dont_follow_back)}명")
print(f"맞팔: {len(mutual_follow)}명")