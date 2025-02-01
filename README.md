
# Password Strength Checker

## Overview

This project implements a **Password Strength Checker** that evaluates the strength of a given password by calculating its **entropy** and estimating the time it would take for a hacker to crack it. The checker also verifies if the password has been exposed in known data breaches by querying the **Pwned Passwords API**.

### Key Features:
- **Entropy Calculation**: Measures the strength of a password based on its length and the variety of characters used.
- **Cracking Time Estimate**: Provides an estimate of how long it would take for a hacker to crack the password, using common password cracking techniques.
- **Pwned Passwords Check**: Verifies if the password has been leaked in previous data breaches using the **Pwned Passwords API**.

---

## Installation

To run this project, ensure you have Python 3.x installed. Additionally, you will need the `requests` module to interact with the API.

1. **Clone the repository**:

```bash
git clone https://github.com/JeanVerissimo/password-strength-checker.git
cd password-strength-checker
```

2. **Install dependencies**:

```bash
pip install requests
```

---

## Usage

Run the `main.py` script to start checking password strength. The script will prompt you to enter a password, calculate its entropy, estimate the time to crack, and check if it has been exposed in a data breach.

```bash
python main.py
```

You will be prompted to type a password. The output will look like the following:

```
#**************************************************
Checking entropy value... 
Entropy value: 56 bits.
Estimated time to crack password: less than 1 second.

Checking if this password has been found in data breaches...
This password was NOT found in data breaches
#**************************************************
```

If the password is found in the Pwned Passwords database, you will receive a notification.

---

## Disclaimer

This project is for educational purposes only. The password strength checker is not intended to be a comprehensive security tool and should not be relied upon for securing sensitive systems. Always follow best practices for password management and use additional security measures such as multi-factor authentication (MFA).
