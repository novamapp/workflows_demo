import sys

def main():
    print(f'Hello world! From Python: {sys.version_info}')
    if sys.version_info >= (3, 7) and sys.version_info < (3, 8):
        raise Exception('Python version 3.7.x is unsupported!')

if __name__ == "__main__":
    main()
