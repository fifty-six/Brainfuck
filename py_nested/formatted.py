(lambda: (globals().update({'cells': [0] * 30000,
    'prog_ptr': 0,
    'ptr': 0,
    'brackets': [],
    'program': open(__import__("sys").argv[1]).read().replace('\n', '')
}),
(go := lambda f, mut, replace, evaluator: (evaluator(mut, replace, program[prog_ptr]), mut('prog_ptr', lambda v: v + 1), f(f, mut, replace, evaluator) if prog_ptr < len(program) else ()))(
    go,
    lambda var, mutator: globals().update([(var, mutator(globals()[var]))]),
    lambda mutator: cells.insert(ptr, mutator(cells.pop(ptr))),
    lambda mut, replace, val: ({ 
        '<': lambda: mut('ptr', lambda v: v - 1),
        '>': lambda: mut('ptr', lambda v: v + 1),
        '-': lambda: replace(lambda v: v - 1),
        '+': lambda: replace(lambda v: v + 1),
        ',': lambda: replace(lambda v: ord(__import__("sys").stdin.read(1))), '.': lambda: print(chr(cells[ptr]), end=''),
        '[': lambda: brackets.append(prog_ptr),
        ']': [lambda: mut('prog_ptr', lambda v: brackets[-1]), lambda: brackets.pop()][cells[ptr] == 0]
    }[val]())
)))()
