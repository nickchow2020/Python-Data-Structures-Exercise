def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    stack  = [] 
    for c in parens:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) > 0 :
                stack.pop()
            else:
                stack.append(c)
    
    return not stack