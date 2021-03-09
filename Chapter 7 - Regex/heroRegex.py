import re

# Fazendo correspondência de vários grupos com pipe |
heroRegex = re.compile(r'Batman|Tina Fey')

# Fazendo correspondência com vários prefixos
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

# Correspondência opcional usando ponto de interrogação ?
# Correspondendo a zero ou uma ocorrência do grupo que antecede o ponto de interrogação
batRegex2 = re.compile(r'Bat(wo)?man')

# Exemplo usando número de telefone
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

# Correspondendo a zero ou mais ocorrências usando asterisco *
batRegex3 = re.compile(r'Bat(wo)*man')

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

    # Correspondência opcional usando ponto de interrogação ?
    # Correspondendo a zero ou uma ocorrência do grupo que antecede o ponto de interrogação
    moBat2 = batRegex2.search('The Adventures of Batman')
    print(moBat2.group())
    mo2Bat2 = batRegex2.search('The Adventures of Batwoman')
    print(mo2Bat2.group())

    # Exemplo usando número de telefone
    moPhone = phoneRegex.search('My number is 415-555-4242')
    print(moPhone.group())
    mo2Phone = phoneRegex.search('My number is 555-4242')
    print(mo2Phone.group())

    # Correspondendo a zero ou mais ocorrências usando asterisco *
    moBat3 = batRegex3.search('The Adventures of Batman')
    print(moBat3.group())
    mo2Bat3 = batRegex3.search('The Adventures of Batwoman')
    print(mo2Bat3.group())
    mo3Bat3 = batRegex3.search('The Adventures of Batwowowowoman')
    print(mo3Bat3.group())