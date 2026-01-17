def ChkVovel(ch):
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

def main():
    Result = False
    print("Enter the Character : ")
    ch = input()

    Result = ChkVovel(ch)
    if Result == True:
        print("Character is Vovel")
    else:
        print("Character is consonant")

if __name__ == "__main__":
    main()