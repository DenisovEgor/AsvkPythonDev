import random
from argparse import ArgumentParser
import urllib

def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        word = input(prompt)
        if word in valid or valid is None:
            return word
        print('Ivalid word. Try again.')

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def bullcows(guess: str, answer: str) -> tuple[int, int]:
    word_len = len(guess)
    bulls, cows = 0, 0
    for i in range(word_len):
        if guess[i] == answer[i]:
            bulls += 1
        else:
            for j in range(word_len):
                if guess[i] == answer[j]:
                    cows += 1
    return bulls, cows

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    answer = random.choice(words)
    attempts = 0
    while True:
        attempts += 1
        word = ask('Введите слово: ', words)
        bulls, cows = bullcows(word, answer)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if word == answer:
            return attempts
        
def is_valid_url(url: str) -> bool:
    return url.startswith("http")


parser = ArgumentParser()
parser.add_argument('dict')
parser.add_argument('len', type=int, default=5)
args = parser.parse_args()

if is_valid_url(args.dict):
    with urllib.request.urlopen(args.dictionary) as f:
        words = [word.decode('utf-8').strip() for word in f]
else:
    with open(args.dict) as f:
        words = [word.strip() for word in f]
words = [word for word in words if len(word) == args.len]

attempts = gameplay(ask, inform, words)
print(f'Ваше количество попыток: {attempts}.')