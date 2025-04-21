import numpy as np

def create_table(tokens):
    alphabet = make_alphabet(tokens)
    transitions = [
        {symbol: -1 for symbol in alphabet} 
        for _ in range(len(alphabet))
    ]

    last_state = 0

    for token in tokens:
        last_state = make_token_table(token, transitions, last_state, alphabet)
    
    transitions.append(make_empty_transition(alphabet))

    print_transitions(transitions, alphabet)
    return 1


def make_alphabet(tokens) -> set[str]:
    return {char for token in tokens for char in token}
    
def make_token_table(token, transitions, last_state, alphabet) -> int:
    i = last_state + 1
    transitions[0][token[0]] = i 

    for char in token[1:]:
        if i == len(transitions):
            transitions.append(make_empty_transition(alphabet))

        transitions[i][char] = i + 1
        i += 1
    
    return i


def make_empty_transition(alphabet: set[str]) -> dict[str, int]:
    return {char: -1 for char in alphabet}

def print_transitions(transitions, alphabet, show_errors=False):
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
    tokens = ["ao", "e", "iua", "xw", "trz"]
    create_table(tokens)

if __name__ == "__main__":
    main()
