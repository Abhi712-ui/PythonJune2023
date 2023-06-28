# Logical Operators

- Logical operators in Python are used to perform logical operations on boolean values or expressions. These operators allow you to combine conditions and evaluate the truthiness or falsiness of complex expressions. Python provides three logical operators: and, or, and not. Let's explore each of them in detail

## Logical AND (`and`)

- The `and` operator returns `True` if both operands are true, and `False`` otherwise.
- If the first operand is evaluated as falsy (e.g., False, None, 0, empty string, empty list, etc.), the second operand is not evaluated, and the result is `False` since both conditions cannot be true.
- If both operands are evaluated as truthy, the second operand is evaluated and the result is the value of the second operand.
- Example: `x and y`

## Logical OR (`or`)

- The `or` operator returns `True` if at least one of the operands is true, and `False` if both operands are false.
- If the first operand is evaluated as truthy, the second operand is not evaluated, and the result is `True` since at least one condition is true.
- If both operands are evaluated as falsy, the second operand is evaluated, and the result is the value of the second operand.
- Example: x or y

## Logical NOT (`not`)

- The `not` operator negates the truth value of an expression. It returns `True` if the expression is falsy and `False` if the expression is truthy.
- The `not` operator has the highest precedence among logical operators.
- Example: not x
- Logical operators can be used to build more complex conditions by combining multiple expressions.

## Important points to remember

### Operator Precedence

- The not operator has the highest precedence, followed by and, and then or. However, it is good practice to use parentheses to clarify the order of evaluation when combining multiple logical operators in a single expression.

### Short-Circuit Evaluation

- Python uses short-circuit evaluation for logical operators. This means that when the result of an and operation is determined to be false based on the evaluation of the first operand, the second operand is not evaluated.

- Similarly, when the result of an or operation is determined to be true based on the evaluation of the first operand, the second operand is not evaluated.

### Truthiness and Falsiness

- Logical operators work with truthy and falsy values. In addition to True and False, truthy values are considered true in logical operations, while falsy values are considered false. It's important to understand the truthiness and falsiness of different types and values in Python to ensure accurate logical evaluations.
