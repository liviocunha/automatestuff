import re

# Fazendo correspondência de vários grupos com pipe |
heroRegex = re.compile(r'Batman|Tina Fey')

# Fazendo correspondência com vários prefixos
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

if __name__ == '__main__':
    # Fazendo correspondência de vários grupos com pipe |
    moHero1 = heroRegex.search('Batman and Tina Fey.')
    print(moHero1.group())

    moHero2 = heroRegex.search('Tina Fey and Batman')
    print(moHero2.group())

    # Fazendo correspondência com vários prefixos
    moBat = batRegex.search('Batmobile lost a wheel')
    print(moBat.group())
    print(moBat.group(1))