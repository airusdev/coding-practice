def deduplicator(string: str) -> str:
    stack = []
    
    for char in string:
        if not stack or stack[-1] != char:
            stack.append(char)
    
    return ''.join(stack)

