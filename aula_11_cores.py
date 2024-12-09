#como trabalhar com cores - padrão ANSI
#\033 é padrão
#primeiro valor (no exemplo é 7): style 0 (nada), 1 (negrito), 4 (sublinhado), 7(negativo)
#segundo valor: cor de texto de 30 a 37
#terceiro valor: cor de fundo de 40 a 47
print("\033[7;33;44mOlá,mundo\033[m")