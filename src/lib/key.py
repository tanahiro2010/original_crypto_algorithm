from .char import text_to_char_list

def generate_key(content: str) -> str:
    """
    generate_key の Docstring
    コンテンツをもとに動的にキーを生成する関数です。
    
    :param content: 説明
    :type content: str
    :return: 説明
    :rtype: str
    """

    chars = text_to_char_list(content)
    key: str = ""

    for c in chars:
        # ここでキー生成のロジックを実装します。
        # 例えば、文字のUnicode値を使用してキーを生成することができます。
        key += str(ord(c) % 10)  # 簡単な例として、文字のUnicode値の最後の数字をキーに追加


    return key

def main():
    content = "This is a sample content for key generation."
    key = generate_key(content)
    print(f"Generated Key: {key}")
    return

if __name__ == "__main__":
    main()