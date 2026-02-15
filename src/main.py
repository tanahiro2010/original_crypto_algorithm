import sys
from crypto.index import encode, decode



def main():
    content = sys.argv[1] if len(sys.argv) > 1 else "Default Content"
    print(f"Content: {content}")
    encoded = encode(content)

    return

if __name__ == "__main__":
    main()