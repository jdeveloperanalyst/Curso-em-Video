# Desafio 4 — Informações sobre tipos primitivos

Solução do **Desafio 4** do Mundo 1 do Curso em Vídeo de Python 3: o programa lê um valor digitado pelo usuário e exibe o tipo e várias verificações sobre a string.

## Arquivo

- `informacoes_tipos_primitivos.py` — script principal

## Como executar

Na pasta deste desafio:

```bash
python3 informacoes_tipos_primitivos.py
```

Ou, se `python` apontar para Python 3:

```bash
python informacoes_tipos_primitivos.py
```

## O que o programa faz

1. Pede que você digite algo.
2. Mostra o tipo do valor (sempre `str` após `input()`, pois `input()` retorna texto).
3. Usa métodos de string para indicar se o texto:
   - contém só espaços (`isspace()`)
   - parece numérico (`isnumeric()`)
   - é só letras (`isalpha()`)
   - é letras e/ou números (`isalnum()`)
   - está em maiúsculas (`isupper()`)
   - está em minúsculas (`islower()`)
   - está “capitalizado” no estilo título (`istitle()`)

## Requisitos

- Python 3 (sem bibliotecas externas)
