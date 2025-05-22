from LexTable import LexTable

ltable = LexTable()

def read():
    rules_list = []

    with open("example.txt", "r") as file:
        for line_index, line in enumerate(file):
            head, body = line.strip().split("->")
            head = head.strip()
            rule_bodies = [alt.strip().split() for alt in body.strip().split("|")]

            if line_index == 0:
                first_head = head
                rules_list.insert(0, ("S'", [[first_head, "$"]]))

            rules_list.append((head, rule_bodies))

    # Agora converte em dicionário
    return dict(rules_list)

def fist(productions):
    fist = {}
    for nt in productions:
        fist[nt] = set()

    mudanca = True
    while mudanca:
        mudanca = False
        # não terminal
        for nt in productions:
            for p in productions[nt]:
                i = 0
                find_epsilon = True

                while i < len(p) and find_epsilon:
                    simbolo = p[i]
                    find_epsilon = False

                    if simbolo in productions:
                        # Simbolo é não terminal, pega FIRST dele
                        for fp in fist[simbolo]:
                            if fp != '' and fp not in fist[nt]:
                                fist[nt].add(fp)
                                mudanca = True
                        if '' in fist[simbolo]:
                            find_epsilon = True
                    else:
                        # Simbolo terminal
                        if simbolo not in fist[nt]:
                            fist[nt].add(simbolo)
                            mudanca = True
                        break  
                    i += 1

                # caso tenha epsilon no final
                if find_epsilon and '' not in fist[nt]:
                    fist[nt].add('')
                    mudanca = True

    print_first(fist)
    return fist


def make():
    productions = read()
    fist(productions)
    return 1

def print_first(first):
    print("First sets:")
    for nt in first.keys():
        values = ', '.join('ε' if v == '' else v for v in sorted(first[nt]))
        print(f"  First({nt}) = {{ {values} }}")


make()