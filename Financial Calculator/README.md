# Finance Calculators

## Project Overview

Finance Calculators is a command-line Python application developed as part of a programming capstone project. It lets a user choose between an **investment calculator**, which estimates the future value of an investment, and a **bond calculator**, which estimates the monthly repayment on a home loan.

The project demonstrates how Python can be used to translate financial formulas into an interactive program using user input, conditional statements, numerical calculations and formatted output.

## Features

### Investment calculator

When the user enters `investment`, the program asks for:

- An initial deposit
- An annual interest rate (as a percentage)
- An investment period (in years)
- An interest type: `simple` or `compound`

It then displays an estimated future value. The simple-interest calculation uses:

```text
A = P × (1 + r × t)
```

where `P` is the deposit, `r` is the annual interest rate expressed as a decimal and `t` is the number of years.

**Important:** The current compound-interest branch contains a formula error: it uses `1 + interest_rate` instead of `1 + interest_rate / 100`. As written, it will substantially overstate results for typical percentage inputs. The intended annual compound-interest formula is:

```text
A = P × (1 + r) ** t
```

### Bond calculator

When the user enters `bond`, the program asks for:

- The purchase price / present value of the house
- An annual bond interest rate (as a percentage)
- A repayment period (in months)

It calculates the estimated monthly repayment using the standard amortising-loan formula:

```text
M = (i × P) / (1 - (1 + i) ** (-n))
```

where `P` is the loan principal, `i` is the monthly interest rate and `n` is the number of monthly repayments. The program assumes the amount borrowed equals the entered house value and a constant interest rate. It does not include deposits, fees, insurance or rate changes.

## Technologies Used

- **Python 3** — program logic, input and calculations
- **`math`** — standard-library mathematical functions
- **Terminal / command line** — user interaction

No third-party Python packages are required.

## Project Files

| File | Description |
| --- | --- |
| `finance_calculators.py` | Python script containing the investment and bond calculators. |
| `README.md` | Project overview, instructions and limitations. |

## How to Run

1. Download or clone the repository.
2. Open the project folder in a terminal or in Visual Studio Code.
3. Make sure Python 3 is installed.
4. Run:

   ```bash
   python finance_calculators.py
   ```

   On systems where `python` does not point to Python 3, use `python3 finance_calculators.py` instead.
5. At the first prompt, type **`investment`** or **`bond`** exactly in lowercase.
6. Follow the on-screen prompts and read the calculated result.

## Example: Simple Interest

For a deposit of `10000`, annual interest of `5` percent and a period of `3` years, select `investment`, then `simple`. The program returns a future value of **11,500** (in the same currency units as the deposit).

## Skills Demonstrated

- Reading and converting user input
- Applying `if` / `elif` conditional logic
- Working with variables and numeric data types
- Implementing basic financial formulas
- Using Python's standard library
- Building an interactive command-line application

## Limitations and Possible Improvements

This is an educational project, not a production-ready financial calculator. Improvements include:

- Correcting the compound-interest calculation to divide the percentage rate by 100.
- Adding validation for invalid choices, non-numeric entries and negative values.
- Handling a zero interest rate in the bond calculator to avoid division by zero.
- Supporting decimal values for deposits and consistent currency formatting.
- Providing an option to run another calculation without restarting the script.
- Adding automated tests for the financial formulas.

## Conclusion

The project illustrates how foundational Python programming skills can be applied to common personal-finance calculations. It combines financial concepts with basic program flow and provides a starting point for more robust financial tools.
