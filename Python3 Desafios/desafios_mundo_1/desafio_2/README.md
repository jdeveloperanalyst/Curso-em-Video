# Desafio 2 - Data de Nascimento

Este script lê a data de nascimento do usuário como dia, mês e ano e exibe no formato `DD/MM/AAAA`.

## Como usar

1. Execute o script com Python 3:
    ```bash
    python3 "Python3 Desafios/desafios_mundo_1/desafio_2/data_nascimento_usuario.py"
    ```
2. Informe os valores solicitados:
    - Dia (número inteiro)
    - Mês (número inteiro)
    - Ano (número inteiro)

## Comportamento

- Entrada inválida (texto não numérico) causa `ValueError` em `int(input(...))`.
- O script imprime corretamente a data usando `f-string` ou conversão `str()`.

## Exemplo

```
Digite o dia do seu nascimento: 30
Digite o mês do seu nascimento: 12
Digite o ano do seu nascimento: 1992
Sua data de nascimento é: 30/12/1992
```
