import sys

def read_ideas():
    ideas = []
    with open("ideas.txt") as file:
        for line in file:
            ideas.append(line.strip())
    return ideas

def show_ideas(ideas):
    for count, idea in enumerate(ideas, 1):
        print(f"{count}. {idea}") 

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--list':
        show_ideas(read_ideas())

    if len(sys.argv) > 2 and sys.argv[1] == '--delete':
        print(sys.argv[2])
        
    print("Hello in Ideabank")
    ideas = read_ideas()
    # show_ideas(ideas)