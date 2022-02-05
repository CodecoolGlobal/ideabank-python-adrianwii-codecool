import sys

def read_ideas():
    ideas = []
    with open("ideas.txt") as file:
        for line in file:
            print(line.strip())
    return ideas

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--list':
        print(sys.argv[1])

    if len(sys.argv) > 2 and sys.argv[1] == '--delete':
        print(sys.argv[2])
        
    print("Hello in Ideabank")
    print(read_ideas())