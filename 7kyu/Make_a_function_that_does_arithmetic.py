def arithmetic(a, b, operator):
    match operator:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            return a / b
        case _:
            raise ValueError(f'Unknown type of operator: {operator}')