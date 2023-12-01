import SparkApi

text = []


# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


if __name__ == '__main__':
    text.clear()
    while (1):
        Input = input("\n" + "我:")
        question = checklen(getText("user", Input))
        SparkApi.answer = ""
        print("星火:", end="")
        SparkApi.main(question)
        getText("assistant", SparkApi.answer)
        # print(str(text))

