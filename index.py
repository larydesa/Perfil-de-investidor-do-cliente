print ("------- INVESTIMENTOS -------")
valor_investido = float(input("Quanto você deseja investir: "))

if valor_investido <= 5.000:
  print("Seu perfil é: CONSERVADOR")
elif valor_investido <= 50.000:
  print("Seu perfil é: MODERADO")
else:
  print("Seu perfil perfil é: ARROJADO")
print("-" * 30)

atendimento = int(input('''Qual sua preferência de atendimento?
                        [1] App/Robô
                        [2] Especialista'''))
if atendimento == 1:
  print("Sua conta será direcionada para a nossa IA de investimentos recomendados")
elif atendimento == 2:
  if valor_investido <= 50.000:
    print("Você terá acesso ao nosso Chat de suporte geral")
  else:
    print("Você terá um Gerente Exclusive dedicado para montar sua carteira de ações")
