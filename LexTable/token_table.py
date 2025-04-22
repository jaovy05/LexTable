import numpy as np

def create_table(tokens):
    alphabet = make_alphabet(tokens)
    transitions = [{symbol: -1 for symbol in alphabet}]

    for token in tokens:
        make_token_table_recursive(token, transitions, alphabet)
        transitions.append(make_empty_transition(alphabet))

    print_transitions(transitions, alphabet)
    return 1


def make_alphabet(tokens) -> set[str]:
    return {char for token in tokens for char in token}
    
# def make_token_table(token, transitions, last_state, alphabet) -> int:
#     current = last_state + 1
    
#     if transitions[0][token[0]] == -1:
#         transitions[0][token[0]] = current
#         i = 1
#     else:
#         transitions[transitions[0][token[0]]][token[1]] = current
#         i = 2

#     n = len(token)

#     while i < n:
#         char = token[i]

#         if current == len(transitions):
#             transitions.append(make_empty_transition(alphabet))

#         if transitions[current][char] == -1:
#             transitions[current][char] = current + 1
#         else:
#             transitions[transitions[current][char]][token[i + 1]] = current + 1
#             i += 1

#         current += 1
#         i += 1
#     return current

def make_token_table_recursive(token: str, transitions, alphabet) ->  tuple[int, bool]:
    if len(token) == 1:
        last_pos = len(transitions)
        if transitions[0][token] == -1:
            transitions[0][token] = last_pos
            return last_pos, False
        else:
            return 0, True
        
    i, conflito = make_token_table_recursive(token[:-1], transitions, alphabet) 

    if conflito:
        lenT = len(transitions) 
        i = transitions[i][token[-2]]
        if transitions[i][token[-1]] == -1:
            transitions[i][token[-1]] = lenT
            return lenT, False
        else:
            return i, True
        
    else:
        transitions.append(make_empty_transition(alphabet))
        if transitions[i][token[-1]] == -1:
            transitions[i][token[-1]] = i + 1
            return i + 1, False
        else:
            return transitions[i][token[-1]], True

def make_empty_transition(alphabet: set[str]) -> dict[str, int]:
    return {char: -1 for char in alphabet}

def print_transitions(transitions, alphabet, show_errors=False):
    alphabet = sorted(alphabet)   
    print("    ", end="")
    for symbol in alphabet:
        print(f"{symbol:^5}", end="") 
    print()

    for state_index, state in enumerate(transitions):
        print(f"{state_index:>3} ", end="")  
        for symbol in alphabet:
            next_state = state.get(symbol, -1)  
            if show_errors or next_state != -1:
                print(f"{next_state:^5}", end="")
            else:
                print(f"     ", end="")
        print()

def main():
    tokens = ["aete", "aeca","fogofatua", "fogofat"]
    create_table(tokens)

if __name__ == "__main__":
    main()
