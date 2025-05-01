import requests
from bs4 import BeautifulSoup

def get_word_definition(word):
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Không thể truy cập từ điển cho từ '{word}'."

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        definition = soup.find("div", class_="def ddef_d db").text.strip()
        pronunciation = soup.find("span", class_="ipa").text.strip()
        return f"{word} /{pronunciation}/: {definition}"
    except:
        return f"Không tìm thấy định nghĩa cho từ '{word}'."

if __name__ == "__main__":
    word = input("Nhập từ cần tra cứu: ")
    print(get_word_definition(word))
