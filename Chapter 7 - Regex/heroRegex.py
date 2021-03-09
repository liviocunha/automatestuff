import re

# Fazendo correspondência de vários grupos com pipe |
heroRegex = re.compile(r'Batman|Tina Fey')

if __name__ == '__main__':
    # Fazendo correspondência de vários grupos com pipe |
    moHero1 = heroRegex.search('Batman and Tina Fey.')
    print(moHero1.group())

    moHero2 = heroRegex.search('Tina Fey and Batman')
    print(moHero2.group())