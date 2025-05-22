import json
import pprint
import time
from LexTable import LexTable

ltable = LexTable()


def read():
    rules_list = []

    with open("exemple.txt", "r") as file:
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

def make():
    productions = read()
    ltable.productions = productions
    i0 = [["."] + productions["S'"][0]]


    marcados = []
    for temp in i0:
        if temp == ['.']:
            ltable.complete.append('I0')
            continue
        pos = 1
        if temp[pos] in productions and temp[pos] not in marcados:
            for p in productions[temp[pos]]:
                i0.append(['.']+p)
            marcados.append(temp[pos])

    closure = {
        'I0': i0
    }
 

    tratados = []
    i = j = 0
    while j < len(closure):
        for p in closure[f'I{j}']:
            cpos = p.index(".") + 1
            if  cpos != len(p) and p[cpos] != '$' and p not in tratados:
                i += 1
                closure[f'I{i}'], res = goto(closure[f'I{j}'], p[cpos], productions, tratados)
                if res == 'a':
                    ltable.accept = f'I{i}'
                elif res == 'c':
                    ltable.complete.append(f'I{i}')
                else:
                    if f'I{j}' not in ltable.transactions:
                        ltable.transactions[f'I{j}'] = {}
                    ltable.transactions[f'I{j}'][p[cpos]] = f'I{i}'
        j += 1
        
    ltable.closure = closure
    print_colored_closure(ltable.closure)
    # print(f'completos: {ltable.complete}')
    # print(f'Aceita: {ltable.accept}')

def goto(I,X, productions, tratados):
    res = 'n'
    i = []
    for prod in I:
        dot_pos = prod.index(".")
        if dot_pos + 1 != len(prod) and prod[dot_pos + 1] == X:
            s_list = prod[:]
            s_list[dot_pos], s_list[dot_pos + 1] = s_list[dot_pos + 1], s_list[dot_pos]
            i.append(s_list)
            tratados.append(prod)


    marcados = []
    for temp in i:
        pos = temp.index('.') + 1
        if pos == len(temp):
            res = 'c'
            continue
        if temp[pos] == '$':
            res = 'a'
            continue
        if temp[pos] in productions and temp[pos] not in marcados:
            for p in productions[temp[pos]]:
                i.append(["."] + p)

            marcados.append(temp[pos])

    return i, res

def print_colored_closure(closure):
    RED = "\033[91m"
    RESET = "\033[0m"
    PURPLE = "\033[95m"
    BLUE = '\033[94m'
    GREEN = '\033[92m'

    for chave, producoes in closure.items():
        if chave in ltable.complete:
            print(f"{GREEN + chave + RESET}: [", end="")
        elif chave == ltable.accept:
            print(f"{BLUE + chave + RESET}: [", end="")
        else:
            print(f"{chave}: [", end="")

        linhas = []
        for prod in producoes:
            linha = []
            for token in prod:
                if token == ".":
                    linha.append(f"{RED}.{RESET}")
                else:
                    linha.append(token)
            linhas.append(" ".join(linha))
        print(F",".join(f"{PURPLE}[{RESET}{linha}{PURPLE}]{RESET}" for linha in linhas), end="")
        print("]")


make()
