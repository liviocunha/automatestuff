"""
1. Importe o módulo de regex usando import re
2. Crie um objeto Regex usando a função re.compile(). (usar uma string pura r raw)
3. Passe a string que você quer pesquisar ao método search() do objeto Regex
Isso fará um objeto Match ser retornado.
4. Chame o método group() do objeto Match para retornar uma string com o texto correspondente.
Nota: Para testar a expressão regular, pode ser usar http://regexpal.com
"""

import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegexUSA = re.compile(r'\d{3}-\d{3}-\d{4}')
# phoneNumRegexBRA = re.compile(r'\d{2}-\d{5}-\d{4}')

# Separando por grupos
# phoneNumRegexUSA = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegexBRA = re.compile(r'(\(\d\d\))(\d\d\d\d\d-\d\d\d\d)')

# Separando por grupos com scape no parenteses
phoneNumRegexUSA = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

if __name__ == '__main__':
    # mo = phoneNumRegexUSA.search('My number is 415-555-4242.')
    # mo = phoneNumRegexUSA.search('My number is (415) 555-4242.')
    # mo = phoneNumRegexBRA.search('Meu número é 16-99999-8888.')
    mo = phoneNumRegexBRA.search('Meu número é (16)99999-8888.')
    print(f"Phone number found: {mo.group()}")

    '''# Primeiro grupo
    print(mo.group(1))
    # Segundo grupo
    print(mo.group(2))
    # Todos grupos
    print(mo.group(0))
    # Todos grupos
    print(mo.group())

    # Obter todos os grupos de um vez
    tupleGroups = mo.groups()
    print(tupleGroups)

    # groups() retorna uma tupla podemos fazer uma atribuição multipla
    areaCode, mainNumber = tupleGroups
    print(areaCode)
    print(mainNumber)'''
    # print(mo.group(1))
    # print(mo.group(2))
