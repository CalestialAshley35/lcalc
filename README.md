# lcalc (Linux Calculator)

**lcalc** is a versatile, feature-rich command-line calculator built with Python. This tool caters to a wide range of mathematical needs, including basic operations, advanced algebra, calculus, trigonometry, and matrix manipulation. Designed for precision and usability, lcalc is powered by libraries such as `Decimal`, `SymPy`, and `Rich`.

## Key Features

- **High-Precision Calculations**: Achieve up to 50 decimal places of accuracy using Python's `Decimal`.
- **Basic Arithmetic Operations**: Support for addition, subtraction, multiplication, division, modulo, floor division, and exponentiation.
- **Advanced Algebra**: Solve equations, simplify, expand, and factor expressions.
- **Calculus Operations**: Perform differentiation and integration of mathematical expressions.
- **Trigonometry Functions**: Calculate values for sine, cosine, tangent, and their inverses.
- **Matrix Operations**: Includes matrix addition, subtraction, multiplication, determinant calculation, inversion, and transposition.
- **Interactive Command-Line Interface**: Intuitive prompts and colored output for better user experience.

## System Requirements

- Python 3.8 or later
- Dependencies: Install using `pip`
    ```bash
    pip install sympy rich
    ```

## Installation

To download and run lcalc, use the following commands:

```bash
wget https://github.com/CalestialAshley35/lcalc/raw/main/lcalc.py
python lcalc.py
```

## Usage

Upon running the script, an interactive prompt will guide you through various operations. Below is a breakdown of the supported functionality:

### Basic Operations

Enter expressions such as `5 + 3`, `9 * 2`, or `7 ^ 3` directly at the prompt. Supported operators include:

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `^`: Exponentiation
- `%`: Modulus
- `//`: Floor Division

### Solving Equations

Solve algebraic equations with the `=` sign. Example:
```text
x^2 - 5x + 6 = 0
```
Results in the roots of the equation.

### Algebraic Expression Manipulation

1. **Expand**: Expand expressions like `(x+1)^2`.
2. **Simplify**: Simplify expressions such as `(x^2 + 2x + 1)/(x+1)`.
3. **Factor**: Factor expressions like `x^2 - 5x + 6`.

### Calculus Operations

1. **Differentiate**: Use the `diff` command. Example: `diff x^2 + 2x + 1` gives `2x + 2`.
2. **Integrate**: Use the `integrate` command. Example: `integrate x^2 + 2x + 1` computes the integral.

### Trigonometry

Directly evaluate trigonometric functions:
- `sin(pi/2)` = 1
- `tan(pi/4)` = 1

### Matrix Operations

Input matrices and perform operations:
1. Addition/Subtraction: Use `+` or `-`.
2. Multiplication: Use `*`.
3. Determinant: Specify `det`.
4. Inverse: Specify `inv`.
5. Transposition: Specify `transpose`.

Example:
```text
Matrix 1: [[1, 2], [3, 4]]
Matrix 2: [[5, 6], [7, 8]]
Operation: *
```

### Custom Formula Evaluation

For custom expressions (e.g., `sqrt(16) + log(100)`), enter them directly in the prompt.

### Exiting the Calculator

When you're done, type `no` when prompted to continue, and the application will gracefully exit.

## Example Session

```text
Welcome to lcalc (Linux Calculator)!
Supports: advanced algebra, calculus, trigonometry, matrices, and more.

Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0): 3 + 4
Result: 7

Do you want to perform another calculation? (yes/no): no
Thank you for using lcalc!
```

## License

This project is licensed under the **Apache License 2.0**. For more information, refer to the `LICENSE` file in the repository.