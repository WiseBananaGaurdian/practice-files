def emoji_changer(text):
    words = text.split(" ")
    emoji_dict = {
        ":)": "😀",
        ":(": "🙁"
    }
    output = ""
    for word in words:
        output += emoji_dict.get(word, word) + " "
    return output

text = input(">")
print(emoji_changer(text))
