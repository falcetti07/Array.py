def palindromo(p1, p2):
  """
  Verifica se duas strings são palíndromos.

  Args:
    p1: A primeira string.
    p2: A segunda string.

  Returns:
    True se ambas as strings forem palíndromos, False caso contrário.
  """

  # Remove espaços em branco e converte para minúsculas para uma comparação mais precisa
  p1 = p1.replace(" ", "").lower()
  p2 = p2.replace(" ", "").lower()

  # Verifica se as strings invertidas são iguais às originais
  if p1 == p1[::-1] and p2 == p2[::-1]:
    return True
  else:
    return False

# Strings para teste
string1 = "amor"
string2 = "casa"

# Chama a função palindromo para verificar se as strings são palíndromos
resultado = palindromo(string1, string2)

# Imprime o resultado
print(f"'{string1}' e '{string2}' são palíndromos? {resultado}")