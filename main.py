from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])



def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            bracket = Bracket(next_char, i+1)
            opening_brackets_stack.append(bracket)
        if next_char in ")]}":
            if not opening_brackets_stack:
                return i+1

            top_bracket = opening_brackets_stack.pop()
            if not are_matching(top_bracket.char, next_char):
                return i+1





    if opening_brackets_stack:
        top_bracket = opening_brackets_stack.pop()
        return top_bracket.position 
    return "Success"




def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
if __name__ == "__main__":
    main()
