from sys import argv

def main():

    script = argv[0]
    args = argv[1:]

    print("The script is called", script)
    
    for i in range(len(args)):
        print(f"Argument number {str(i+1)} is:", args[i])
    
    print("Thanks for your time!")



if __name__ == '__main__':
    main()