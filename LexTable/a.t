S -> A | B
A -> var id : TYPE ;
B -> function id ( C ) : TYPE ; F
C -> E D | 
D -> ; E D | 
E -> id : TYPE
F -> begin G end
G -> H G | 
H -> id : = EXPR ; | if EXPR then H else H ; | while EXPR do H ;
TYPE -> integer | boolean
EXPR -> id | num | EXPR + EXPR | EXPR * EXPR