import sys



def main():
    content = sys.argv[1] if len(sys.argv) > 1 else "Default Content"
    print(f"Content: {content}")

    return

if __name__ == "__main__":
    main()