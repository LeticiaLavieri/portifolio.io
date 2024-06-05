from fpdf import FPDF


# Função para obter entradas do usuário:
def get_input(prompt):
    return input(prompt).strip()


#Obtenção dos dados do projeto
projeto = get_input('Digite a descrição do projeto: ')
horas_previstas = get_input('Digite a quantidade de horas previstas: ')
valor_hora = get_input('Digite o valor da hora trabalhada: ')
prazo = get_input('Digite o prazo estimado: ')
valor_total = int(horas_previstas) * int(valor_hora)


# Criação do PDF
pdf = FPDF()
pdf.add_page() #Adiciona uma pagina ao PDF
pdf.set_font('Arial', '', 12) # Escolhe a fonte do arquivo


# Adiciona a imagem de fundo
template_path = 'template.png'
pdf.image(template_path, x=0, y=0) #Insere o template no pdf, colocar coordenadas no parametro


# Adiciona os detalhes do projeto
pdf.text(120, 170, projeto) 
pdf.text(120, 185, horas_previstas)
pdf.text(120, 200, valor_hora)
pdf.text(120, 215, prazo)
pdf.text(120, 230, str(valor_total)) #PDF não aceita valores do tipo int


# Salva em PDF
pdf.output('Orçamento.pdf') #Nome do arquivo e extensão

print('Orçamento gerado com sucesso')
