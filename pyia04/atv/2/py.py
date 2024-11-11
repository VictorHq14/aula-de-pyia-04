def nome_completp(nome, sobrenome):
    return f'{nome} {sobrenome}'

idade = 21

nome_idade = f'meu nome {nome_completp('augusto', 'santana')} e idade é {idade}'

print(nome_idade)