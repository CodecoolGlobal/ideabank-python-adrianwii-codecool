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


def save_ideas(ideas, file_name):
    with open (file_name, "w") as file:
        for idea in ideas:
            file.write(f" {idea}\n")

def delete_idea(index, ideas):
    ideas.remove(ideas[index-1])
    save_ideas(ideas, "ideas.txt")
    show_ideas(ideas)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--list':
        show_ideas(read_ideas())
    elif len(sys.argv) > 2 and sys.argv[1] == '--delete':
        try:
            index = int(sys.argv[2])
        except ValueError:
            print("Please provide a number value")
        else:
            ideas = read_ideas()
            delete_idea(int(sys.argv[2]), ideas)
    else:
        while True:
            idea = input("Whats your new idea? ")
            ideas = read_ideas()
            ideas.append(idea)
            save_ideas (ideas, "ideas.txt")
            show_ideas(ideas) 