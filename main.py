hora = float(input('valor da hora:  '))
mes = float(input('horas trabalhadas por mês:  '))
total = hora * mes
total *= 0.97
total *= 0.89
print('_________________________________________________')
print('seu salario bruto total é de: $',hora*mes)
print('descontamdo o sindicato e impostos fica: ${:.2f}'.format(total))
print('.................................................')