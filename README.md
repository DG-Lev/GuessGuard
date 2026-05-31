# GuessGuard

GuessGuard is a password strength analyzer built with machine learning.

Most password checkers grade strength based on arbitrary rules — has an uppercase letter, has a number, has a symbol, longer than 8 characters. The problem is that `P@ssw0rd` passes every one of those checks while being trivially guessable, and `fdtfhiurhwrt` fails most of them while being genuinely hard to crack.

GuessGuard approaches strength differently: instead of rules, it asks how many guesses an attacker would need. It's trained on `rockyou-75.txt` — a dataset of real leaked passwords sorted by frequency — and uses zxcvbn, a library developed by Dropbox security researchers, to generate realistic guessability scores as training labels.

---

## How it works

GuessGuard is trained to predict the guessability of passwords. It analyzes 5 features: amount of uppercase letters, lowercase letters, digits, symbols, and total length. Based on these factors it predicts a `guesses_log10` score — a measure of how many guesses an attacker would need to crack the password.

---

## How to run

1. `git clone https://github.com/DG-Lev/GuessGuard.git`
2. `cd GuessGuard`
3. `python -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. Download `rockyou-75.txt` from [SecLists](https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Leaked-Databases/rockyou-75.txt) and place it in the project folder
7. `python build_dataset.py` — generates `dataset.csv`
8. `python train.py` — trains the model, prints MAE, saves `model.pkl`

---

## Current results

MAE (Mean Absolute Error) represents how far off the model's predictions are on average. An MAE of 0.774 means the model might predict 5.2 when the real answer is 6.0.

**Current MAE: 0.774** on the `guesses_log10` scale.

---

## Known limitations

- **No dictionary detection** — the model does not differentiate between random characters and actual words
- **No pattern detection** — commonly used patterns like `qwerty`, `abcde`, `123456` are invisible to the model
- **No leet-speak detection** — `P@ssw0rd` looks the same to the model as `G8aof$d`, which inflates its score


## Next steps: 

1. run sanity_check.py with a predefined set of confirmed weak passwords and a set of confirmed strong passwords and check for onconsistencies in MAE
2.  train model on english and german dictionaries for differentiation between random strings and actual words
3. expand the training data from rockyou-75.txt to the full rockyou file


## Tech Stack:

Python, venv, scikit-learn, pandas, zxcvbn, joblib