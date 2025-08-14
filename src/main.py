from textnode import *
print("hello world")
def main():
    new_text = TextNode("Hello, world!", TextType.TEXT, "https://www.chat.com")
    text = new_text.__repr__()
    print(text)
main()