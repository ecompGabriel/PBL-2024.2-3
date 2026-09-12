# Autor: Gabriel Oliveira de Freitas
# Componente Curricular: MI Algoritmos
# Concluído em: 07/12/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
import json
import random
import threading
import time

#Questões
questoes = [
    #Entretenimento (10 perguntas)
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Qual é o nome do personagem que é um brinquedo astronauta em \"Toy Story\"?", "opcoes": ["Woody", "Buzz Lightyear", "Rex", "Slinky", "Jessie"], "resposta": 1, "explicacao": "Buzz Lightyear é o brinquedo astronauta em \"Toy Story\".", "dica": "Seu famoso bordão é \"Ao infinito e além!\"."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Quem é o autor de \"Harry Potter\"?", "opcoes": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Rick Riordan", "Stephen King"], "resposta": 1, "explicacao": "J.K. Rowling é a autora de \"Harry Potter\".", "dica": "A autora é britânica e escreveu sob o pseudônimo Robert Galbraith."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Qual banda lançou \"The Dark Side of the Moon\"?", "opcoes": ["Led Zeppelin", "Pink Floyd", "The Beatles", "Queen", "Rolling Stones"], "resposta": 1, "explicacao": "Pink Floyd lançou o álbum \"The Dark Side of the Moon\".", "dica": "A banda é conhecida por seu estilo psicodélico e progressivo."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Qual super-herói é Clark Kent?", "opcoes": ["Homem-Aranha", "Batman", "Superman", "Flash", "Mulher-Maravilha"], "resposta": 2, "explicacao": "Clark Kent é o alter ego do Superman.", "dica": "Ele é um repórter do Planeta Diário."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "\"Winter is Coming\" é de qual série?", "opcoes": ["Breaking Bad", "Game of Thrones", "The Witcher", "Stranger Things", "Vikings"], "resposta": 1, "explicacao": "\"Winter is Coming\" é uma frase famosa de \"Game of Thrones\".", "dica": "Essa série é baseada nos livros de George R.R. Martin."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Qual é o cowboy de \"Toy Story\"?", "opcoes": ["Buzz", "Woody", "Jessie", "Rex", "Bullseye"], "resposta": 1, "explicacao": "Woody é o brinquedo cowboy em \"Toy Story\".", "dica": "Ele é amigo do Buzz Lightyear."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Quem é o Rei do Pop?", "opcoes": ["Elvis Presley", "Michael Jackson", "Prince", "David Bowie", "Freddie Mercury"], "resposta": 1, "explicacao": "Michael Jackson é conhecido como o Rei do Pop.", "dica": "Seu álbum mais vendido é \"Thriller\"."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Quem criou a Disneyland?", "opcoes": ["Walt Disney", "Steven Spielberg", "George Lucas", "Jim Henson", "Stan Lee"], "resposta": 0, "explicacao": "Disneyland foi criada por Walt Disney.", "dica": "Ele também é o criador do Mickey Mouse."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Em qual filme aparece Arendelle?", "opcoes": ["Moana", "Frozen", "Encanto", "Valente", "Pocahontas"], "resposta": 1, "explicacao": "O reino de Arendelle aparece em \"Frozen\".", "dica": "A protagonista tem poderes de gelo."},
    {"categoria": "Entretenimento", "valor": 10, "pergunta": "Mario, Luigi e Bowser são de qual jogo?", "opcoes": ["Zelda", "Pokémon", "Super Mario", "Donkey Kong", "Kirby"], "resposta": 2, "explicacao": "Os personagens Mario, Luigi e Bowser pertencem à série \"Super Mario\".", "dica": "O jogo envolve coletar moedas e salvar a princesa Peach."},

    #História (10 perguntas)
    {"categoria": "História", "valor": 10, "pergunta": "Quem foi o primeiro presidente do Brasil?", "opcoes": ["Dom Pedro I", "Getúlio Vargas", "Juscelino Kubitschek", "Marechal Deodoro da Fonseca", "Floriano Peixoto"], "resposta": 3, "explicacao": "Marechal Deodoro da Fonseca foi o primeiro presidente do Brasil.", "dica": "Ele proclamou a República do Brasil."},
    {"categoria": "História", "valor": 10, "pergunta": "Qual evento marcou o início da Segunda Guerra Mundial?", "opcoes": ["Ataque a Pearl Harbor", "Invasão da Polônia", "Queda da Bastilha", "Revolução Russa", "Bombardeio de Hiroshima"], "resposta": 1, "explicacao": "A Segunda Guerra Mundial começou com a invasão da Polônia em 1939.", "dica": "Foi uma invasão liderada por Hitler."},
    {"categoria": "História", "valor": 10, "pergunta": "Quem foi o principal líder da Revolução Russa de 1917?", "opcoes": ["Stalin", "Lenin", "Trotsky", "Kerensky", "Gorbachev"], "resposta": 1, "explicacao": "Lenin foi o principal líder da Revolução Russa de 1917.", "dica": "Ele era o líder do partido bolchevique."},
    {"categoria": "História", "valor": 10, "pergunta": "Qual foi o nome do tratado que encerrou a Primeira Guerra Mundial?", "opcoes": ["Tratado de Paris", "Tratado de Versalhes", "Tratado de Potsdam", "Tratado de Munique", "Tratado de Utrecht"], "resposta": 1, "explicacao": "O Tratado de Versalhes encerrou a Primeira Guerra Mundial.", "dica": "Foi assinado em 1919 e incluiu penalidades para a Alemanha."},
    {"categoria": "História", "valor": 10, "pergunta": "Qual civilização antiga construiu Machu Picchu?", "opcoes": ["Astecas", "Maias", "Incas", "Egípcios", "Romanos"], "resposta": 2, "explicacao": "Machu Picchu foi construída pelos Incas.", "dica": "Esta civilização habitava os Andes."},
    {"categoria": "História", "valor": 10, "pergunta": "Qual evento deu início à Idade Média?", "opcoes": ["Queda do Império Romano", "Descobrimento da América", "Revolução Industrial", "Primeira Cruzada", "Peste Negra"], "resposta": 0, "explicacao": "A Idade Média começou com a queda do Império Romano.", "dica": "O evento ocorreu em 476 d.C."},
    {"categoria": "História", "valor": 10, "pergunta": "Quem foi conhecido como o pai da democracia ateniense?", "opcoes": ["Sócrates", "Péricles", "Platão", "Clístenes", "Aristóteles"], "resposta": 3, "explicacao": "Clístenes é conhecido como o pai da democracia ateniense.", "dica": "Ele implementou reformas políticas em Atenas."},
    {"categoria": "História", "valor": 10, "pergunta": "Qual foi o principal propósito das Cruzadas?", "opcoes": ["Expansão territorial", "Propagar o cristianismo", "Recuperar Jerusalém", "Defender Constantinopla", "Proteger rotas comerciais"], "resposta": 2, "explicacao": "O principal propósito das Cruzadas era recuperar Jerusalém.", "dica": "Foram expedições religiosas na Idade Média."},
    {"categoria": "História", "valor": 10, "pergunta": "Quem unificou a Alemanha em 1871?", "opcoes": ["Bismarck", "Kaiser Wilhelm II", "Napoleão", "Frederico II", "Hitler"], "resposta": 0, "explicacao": "Otto von Bismarck unificou a Alemanha em 1871.", "dica": "Ele era conhecido como o \"Chanceler de Ferro\"."},
    {"categoria": "História", "valor": 10, "pergunta": "Qual país foi o primeiro a abolir a escravidão?", "opcoes": ["Brasil", "Inglaterra", "Haiti", "Estados Unidos", "França"], "resposta": 2, "explicacao": "O Haiti foi o primeiro país a abolir a escravidão.", "dica": "Foi a primeira república negra do mundo."},

    #Geografia (10 perguntas)
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual é a montanha mais alta do mundo?", "opcoes": ["Monte Everest", "K2", "Kangchenjunga", "Annapurna", "Makalu"], "resposta": 0, "explicacao": "O Monte Everest é a montanha mais alta do mundo.", "dica": "A montanha está localizada na cordilheira do Himalaia."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual país é conhecido como o Reino dos Cangurus?", "opcoes": ["Nova Zelândia", "Austrália", "África do Sul", "Canadá", "Papua-Nova Guiné"], "resposta": 1, "explicacao": "A Austrália é conhecida como o Reino dos Cangurus.", "dica": "Este país é uma ilha e também um continente."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual é o maior deserto do mundo?", "opcoes": ["Saara", "Antártida", "Gobi", "Kalahari", "Atacama"], "resposta": 1, "explicacao": "A Antártida é o maior deserto do mundo.", "dica": "É um deserto gelado, localizado no Polo Sul."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual é o menor continente em área?", "opcoes": ["Europa", "Oceania", "América do Norte", "África", "Antártida"], "resposta": 1, "explicacao": "A Oceania é o menor continente em área.", "dica": "É composto por várias ilhas no Pacífico."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual rio atravessa a cidade de Londres?", "opcoes": ["Tâmisa", "Seine", "Danúbio", "Reno", "Tigre"], "resposta": 0, "explicacao": "O rio Tâmisa atravessa Londres.", "dica": "É um dos rios mais famosos da Inglaterra."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual é a capital da Espanha?", "opcoes": ["Barcelona", "Madrid", "Sevilha", "Valência", "Bilbao"], "resposta": 1, "explicacao": "Madrid é a capital da Espanha.", "dica": "É uma cidade localizada no centro do país."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual país tem a maior extensão territorial do mundo?", "opcoes": ["Canadá", "China", "Rússia", "Estados Unidos", "Brasil"], "resposta": 2, "explicacao": "A Rússia tem a maior extensão territorial do mundo.", "dica": "Este país se estende pela Europa e Ásia."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual é o maior lago do mundo?", "opcoes": ["Lago Michigan", "Lago Superior", "Mar Cáspio", "Lago Baikal", "Lago Vitória"], "resposta": 2, "explicacao": "O Mar Cáspio é o maior lago do mundo.", "dica": "É chamado de \"mar\" devido ao seu tamanho e salinidade."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual é o nome da linha imaginária que divide a Terra em Hemisfério Norte e Sul?", "opcoes": ["Trópico de Câncer", "Meridiano de Greenwich", "Equador", "Trópico de Capricórnio", "Linha Internacional de Data"], "resposta": 2, "explicacao": "O Equador divide a Terra em Hemisfério Norte e Sul.", "dica": "É uma linha imaginária que está a 0° de latitude."},
    {"categoria": "Geografia", "valor": 10, "pergunta": "Qual país possui a maior quantidade de ilhas no mundo?", "opcoes": ["Indonésia", "Canadá", "Filipinas", "Suécia", "Noruega"], "resposta": 3, "explicacao": "A Suécia possui a maior quantidade de ilhas no mundo.", "dica": "É um país escandinavo localizado no norte da Europa."},

    #Ciência (10 perguntas)
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual é o planeta mais próximo do Sol?", "opcoes": ["Vênus", "Terra", "Marte", "Mercúrio", "Júpiter"], "resposta": 3, "explicacao": "Mercúrio é o planeta mais próximo do Sol.", "dica": "É o menor planeta do Sistema Solar."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual é o maior órgão do corpo humano?", "opcoes": ["Coração", "Cérebro", "Fígado", "Pele", "Pulmão"], "resposta": 3, "explicacao": "A pele é o maior órgão do corpo humano.", "dica": "É um órgão externo que protege o corpo."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual é o símbolo químico da água?", "opcoes": ["O2", "H2O", "CO2", "NaCl", "NH3"], "resposta": 1, "explicacao": "H2O é o símbolo químico da água.", "dica": "É composta por dois átomos de hidrogênio e um de oxigênio."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Quantos planetas existem no Sistema Solar?", "opcoes": ["7", "8", "9", "10", "6"], "resposta": 1, "explicacao": "O Sistema Solar possui 8 planetas.", "dica": "O planeta mais distante é Netuno."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual é a unidade básica da vida?", "opcoes": ["Átomo", "Molécula", "Célula", "Tecido", "Órgão"], "resposta": 2, "explicacao": "A célula é a unidade básica da vida.", "dica": "É a menor unidade funcional de um organismo vivo."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual gás é essencial para a respiração humana?", "opcoes": ["Nitrogênio", "Oxigênio", "Hidrogênio", "Dióxido de carbono", "Hélio"], "resposta": 1, "explicacao": "O oxigênio é essencial para a respiração humana.", "dica": "É absorvido pelos pulmões."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual é a principal fonte de energia para a Terra?", "opcoes": ["Vento", "Água", "Sol", "Calor Geotérmico", "Combustíveis Fósseis"], "resposta": 2, "explicacao": "O Sol é a principal fonte de energia para a Terra.", "dica": "Ele é responsável pela fotossíntese."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual é o metal líquido em temperatura ambiente?", "opcoes": ["Mercúrio", "Chumbo", "Ferro", "Prata", "Césio"], "resposta": 0, "explicacao": "O mercúrio é um metal líquido em temperatura ambiente.", "dica": "É usado em termômetros antigos."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual órgão do corpo humano é responsável por bombear o sangue?", "opcoes": ["Cérebro", "Fígado", "Pulmões", "Coração", "Rins"], "resposta": 3, "explicacao": "O coração é responsável por bombear o sangue.", "dica": "É um músculo localizado no tórax."},
    {"categoria": "Ciência", "valor": 10, "pergunta": "Qual cientista formulou a Teoria da Relatividade?", "opcoes": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Marie Curie", "Nikola Tesla"], "resposta": 1, "explicacao": "Albert Einstein formulou a Teoria da Relatividade.", "dica": "Seu famoso artigo foi publicado em 1905."},
     
    #Esportes (10 perguntas)
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Quantos jogadores há em um time de futebol?', 'opcoes': ['9', '10', '11', '12', '13'], 'resposta': 2, 'explicacao': 'Um time de futebol tem 11 jogadores.', 'dica': 'Esse número é formado por goleiro, zagueiros, meio-campistas e atacantes.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Qual país sediou a Copa do Mundo de 2014?', 'opcoes': ['Alemanha', 'Brasil', 'África do Sul', 'Espanha', 'Itália'], 'resposta': 1, 'explicacao': 'O Brasil sediou a Copa do Mundo de 2014.', 'dica': 'Esse país é famoso por suas praias e pelo samba.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Quantos pontos vale um touchdown no futebol americano?', 'opcoes': ['3', '6', '7', '9', '10'], 'resposta': 1, 'explicacao': 'Um touchdown vale 6 pontos.', 'dica': 'É mais do que metade de 10, mas não chega a 7.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Qual é o esporte mais popular do mundo?', 'opcoes': ['Basquete', 'Críquete', 'Tênis', 'Futebol', 'Rugby'], 'resposta': 3, 'explicacao': 'O futebol é o esporte mais popular do mundo.', 'dica': 'Ele é jogado com uma bola e os pés.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Em qual país foram realizados os Jogos Olímpicos de 2008?', 'opcoes': ['Grécia', 'Brasil', 'China', 'Austrália', 'Reino Unido'], 'resposta': 2, 'explicacao': 'Os Jogos Olímpicos de 2008 foram realizados na China.', 'dica': 'Esse país é conhecido por sua Grande Muralha.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Quantos jogadores compõem uma equipe de vôlei?', 'opcoes': ['5', '6', '7', '8', '9'], 'resposta': 1, 'explicacao': 'Uma equipe de vôlei tem 6 jogadores.', 'dica': 'Esse número é par e menor que 7.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Qual país venceu a primeira Copa do Mundo de futebol em 1930?', 'opcoes': ['Brasil', 'Alemanha', 'Uruguai', 'Itália', 'Argentina'], 'resposta': 2, 'explicacao': 'O Uruguai venceu a primeira Copa do Mundo em 1930.', 'dica': 'Esse país está localizado na América do Sul, entre Brasil e Argentina.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Qual é o nome do maior torneio de tênis realizado na Inglaterra?', 'opcoes': ['Roland Garros', 'US Open', 'Wimbledon', 'Australian Open', 'Davis Cup'], 'resposta': 2, 'explicacao': 'Wimbledon é o maior torneio de tênis realizado na Inglaterra.', 'dica': 'Esse torneio é conhecido por seu tradicional gramado verde.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Quantas medalhas de ouro ganhou Michael Phelps em sua carreira olímpica?', 'opcoes': ['18', '22', '23', '28', '20'], 'resposta': 2, 'explicacao': 'Michael Phelps ganhou 23 medalhas de ouro em sua carreira olímpica.', 'dica': 'Esse número é maior que 20, mas menor que 25.'},
    {'categoria': 'Esportes', 'valor': 10, 'pergunta': 'Em que esporte Pelé é considerado um dos maiores atletas da história?', 'opcoes': ['Basquete', 'Tênis', 'Futebol', 'Vôlei', 'Natação'], 'resposta': 2, 'explicacao': 'Pelé é considerado um dos maiores atletas da história do futebol.', 'dica': 'Esse esporte é chamado de “o jogo bonito”.'}
]

#Função para carregar o Hall da Fama.
#Tenta abrir o arquivo JSON com os dados salvos. Caso não exista, retorna um padrão vazio.
def carregar_hall_da_fama():
    try:
        with open('hall_da_fama.json', 'r') as arquivo:  #Abre o arquivo hall_da_fama.json em modo de leitura.
            return json.load(arquivo)  #Carrega os dados do arquivo e retorna.
    except FileNotFoundError:  #Caso o arquivo não exista, retorna um padrão vazio.
        return {'modo1': [], 'modo2': [], 'modo3': []}

#Função para salvar o Hall da Fama.
#Grava os dados atualizados no arquivo JSON.
def salvar_hall_da_fama(hall_da_fama):
    with open('hall_da_fama.json', 'w') as arquivo:  #Abre o arquivo hall_da_fama.json em modo de escrita.
        json.dump(hall_da_fama, arquivo, indent=4)  #Escreve os dados no arquivo de forma formatada.

#Função para atualizar o Hall da Fama.
#Adiciona a pontuação e ordena os registros, mantendo no máximo os 10 melhores.
def atualizar_hall_da_fama(modo, nome, pontuacao):
    hall_da_fama = carregar_hall_da_fama()  #Carrega os dados existentes.
    hall = hall_da_fama[modo]  #Seleciona o modo do jogo (modo1, modo2 ou modo3).
    hall.append({'nome': nome, 'pontuacao': pontuacao})  #Adiciona o novo registro.
    hall.sort(key=lambda x: x['pontuacao'], reverse=True)  #Ordena em ordem decrescente de pontuação.
    hall_da_fama[modo] = hall[:10]  #Mantém apenas os 10 melhores registros.
    salvar_hall_da_fama(hall_da_fama)  #Salva os dados atualizados no arquivo.

#Função para mostrar o Hall da Fama.
#Mostra os registros de cada modo em formato de lista ordenada.
def mostrar_hall_da_fama():
    hall_da_fama = carregar_hall_da_fama()  #Carrega os dados do Hall da Fama.
    print('\nHALL DA FAMA')  #Título da seção.
    for modo, jogadores in hall_da_fama.items():  #Itera sobre os modos de jogo.
        print(f'\n{modo.upper()}:')  #Mostra o nome do modo em letras maiúsculas.
        if jogadores:  #Verifica se há jogadores registrados.
            for i, jogador in enumerate(jogadores, start=1):  #Enumera os registros.
                print(f'{i}. {jogador["nome"]} - {jogador["pontuacao"]} pontos')  #Mostra nome e pontuação.
        else:
            print('Ainda não há registros.')  #Mensagem caso não existam registros.

#Função para usar ajudas.
#Gerencia as ajudas disponíveis: eliminar opções, pular questões ou fornecer dicas.
def usar_ajuda(ajudas, pergunta):
    print('\nEscolha uma ajuda:')  #Menu de ajudas.
    print('1 - Eliminar duas opções incorretas.')
    print('2 - Pular a questão.')
    print('3 - Obter uma dica sobre a resposta.')
    tipo_ajuda = input('Digite o número da ajuda que deseja usar: ')  #Pede o tipo de ajuda.
    while tipo_ajuda not in ['1', '2', '3']:  #Valida a entrada do usuário.
        print('Escolha uma opção válida!')
        tipo_ajuda = input('Digite o número da ajuda que deseja usar: ')
    if tipo_ajuda == '1':  #Elimina duas opções incorretas.
        opcoes = list(enumerate(pergunta['opcoes']))  #Lista as opções com índices.
        opcoes_erradas = [i for i, _ in opcoes if i != pergunta['resposta']]  #Filtra as opções incorretas.
        eliminadas = random.sample(opcoes_erradas, 2)  #Seleciona aleatoriamente duas para eliminar.
        print('\nOpções restantes:')  #Mostra as opções restantes.
        for i, opcao in opcoes:
            if i not in eliminadas:
                print(f'{i + 1}: {opcao}')
    elif tipo_ajuda == '2':  #Permite pular a questão.
        print('\nVocê escolheu pular esta questão.')
        ajudas -= 1  #Diminui o número de ajudas.
        return -1, ajudas  #Retorna código para pular e o número de ajudas.
    elif tipo_ajuda == '3':  #Fornece uma dica da resposta.
        print(f'\nDica: {pergunta["dica"]}')
    ajudas -= 1  #Diminui o número de ajudas.
    return ajudas

#Função para atualizar o tempo no modo 2.
#Calcula e Mostra o tempo restante. Encerra o jogo quando o tempo esgota.
def atualizar_tempo(tempo_inicio, tempo_total, rodando):
    while rodando['status']:  #Enquanto o jogo estiver ativo.
        tempo_restante = tempo_total - int(time.time() - tempo_inicio)  #Calcula o tempo restante.
        if tempo_restante <= 0:  #Verifica se o tempo acabou.
            print('\nTempo esgotado! Você não pontuou.\nDigite ok para voltar ao menu principal!')  #Mensagem final.
            rodando['status'] = False  #Encerra o jogo.
            break
        print(f'\rTempo restante: {tempo_restante} segundos ', end='', flush=True)  #Mostra o tempo restante.
        time.sleep(1)  #Pausa de 1 segundo entre as atualizações.

#Modo 1: Número de Questões Fixas.
#Apresenta 10 questões e calcula a pontuação com base nas respostas corretas.
def modo1(jogo1, nome_jogador):
    s = 0  #Pontuação inicial.
    acertos = 0  #Contador de acertos.
    ajudas = 1  #Número inicial de ajudas.
    perguntas_feitas = set()  #Armazena os índices das perguntas já feitas.

    for _ in range(10):  #Loop para apresentar 10 questões.
        while True:  #Seleciona uma pergunta que ainda não foi feita.
            indice = random.randint(0, len(jogo1) - 1)
            if indice not in perguntas_feitas:  #Verifica se a pergunta já foi feita.
                perguntas_feitas.add(indice)  #Marca a pergunta como feita.
                break
        pergunta = jogo1[indice]  #Seleciona a pergunta.
        print(f'\n{pergunta["pergunta"]}')  #Mostra a pergunta.
        for i, alternativa in enumerate(pergunta['opcoes']):  #Lista as alternativas.
            print(f'{i + 1}: {alternativa}')
        if ajudas > 0:  #Informa o número de ajudas disponíveis.
            print(f'6: Você tem {ajudas} ajuda(s) disponível(is).')
        resposta = input('\nResposta: ')  #Recebe a resposta do jogador.
        if resposta == '6' and ajudas > 0:  #Ativa a ajuda, se disponível.
            resultado_ajuda = usar_ajuda(ajudas, pergunta)  #Chama a função de ajuda.
            if isinstance(resultado_ajuda, tuple) and resultado_ajuda[0] == -1:  #Pula a questão.
                ajudas = resultado_ajuda[1]
                continue
            ajudas = resultado_ajuda
            resposta = input('Escolha sua resposta novamente: ')  #Pede nova resposta
        while not resposta.isdigit() or int(resposta) not in range(1, 6):  #Valida a resposta.
            print('Escolha uma alternativa válida.')
            resposta = input()
        respostaint = int(resposta)  #Converte a resposta para inteiro.
        if respostaint == pergunta['resposta'] + 1:  #Verifica se está correta.
            print('Resposta correta!')
            s += pergunta['valor']  #Adiciona pontos.
            acertos += 1  #Incrementa o contador de acertos.
            if acertos % 3 == 0:  #Da uma ajuda extra a cada 3 acertos.
                ajudas += 1
                print('Parabéns! Você ganhou uma ajuda extra.')
        else:
            print('Resposta incorreta.')
            print(pergunta['explicacao'])  #Mostra a explicação.
    print(f'Você acertou {acertos} questões e fez {s} pontos.')  #Mostra o desempenho final.
    atualizar_hall_da_fama('modo1', nome_jogador, s)  #Atualiza o Hall da Fama.

#Modo 2: Limite de Tempo.
#Apresenta perguntas enquanto o tempo não esgota e calcula a pontuação com base no tempo restante.
def modo2(questoes, nome_jogador):
    pontuacao = 0  #Inicializa a pontuação como zero.
    acertos = [0]  #Inicializa o contador de acertos como lista para ser alterado dentro da thread.
    dicas = 1  #Define a quantidade inicial de dicas disponíveis.
    tempo_total = 120 #Tempo total para responder as questões.
    inicio_jogo = time.time()  #Marca o início do jogo para controle do tempo.
    pendentes = []  #Lista para armazenar perguntas respondidas incorretamente.
    #Seleciona até 10 questões se houver mais de 10 disponíveis, caso contrário usa todas.
    if len(questoes) > 10:
        questoes_jogo = random.sample(questoes, 10)  #Seleciona 10 questões aleatórias.
    else:
        questoes_jogo = questoes.copy()  #Copia todas as questões disponíveis.
    perguntas_feitas = set()  #Conjunto para armazenar perguntas já feitas.
    rodando = {"status": True}  #Variável para controlar o estado do jogo.
    #Inicia o temporizador em uma thread separada.
    thread_tempo = threading.Thread(target=atualizar_tempo, args=(inicio_jogo, tempo_total, rodando))
    thread_tempo.start()  #Começa a contar o tempo em paralelo com o jogo.
    #Enquanto o jogo está ativo e há perguntas disponíveis.
    while rodando["status"] and (len(questoes_jogo) > 0 or len(pendentes) > 0):
        #Se as questões acabarem, adiciona as pendentes novamente no jogo.
        if len(questoes_jogo) == 0 and len(pendentes) > 0:
            questoes_jogo = pendentes[:]
            pendentes = []
        pergunta = questoes_jogo.pop(0)  #Seleciona a próxima pergunta.
        print()
        print(f"\n{pergunta['pergunta']}")  #Mostra a pergunta.
        for i, alternativa in enumerate(pergunta['opcoes']):  #Lista as opções de resposta.
            print(f"{i + 1}: {alternativa}")
        if dicas >= 1:  #Mostra a quantidade de dicas disponíveis.
            print(f"6: Você tem {dicas} dica(s) disponível(is).")
        resposta = None  #Inicializa a resposta como vazia.
        while rodando["status"]:  #Processa enquanto o tempo não esgota.
            resposta = input("\nResposta: ")  #Recebe a resposta do jogador.
            if not rodando["status"]:  #Verifica se o tempo acabou durante o input.
                break
            if resposta == '6' and dicas >= 1:  #Se o jogador escolher usar uma dica.
                print("\nEscolha a dica desejada:")
                print("1 - Eliminar duas opções incorretas.")
                print("2 - Pular a questão.")
                print("3 - Obter uma dica sobre a resposta.")
                tipo_dica = input("Digite o número da dica: ")
                #Verifica se a dica escolhida é válida.
                while tipo_dica not in ["1", "2", "3"]:
                    print("Escolha uma opção válida!")
                    tipo_dica = input("Digite o número da dica: ")
                if tipo_dica == "1":  #Caso o jogador escolha eliminar opções.
                    opcoes_erradas = [i for i in range(len(pergunta["opcoes"])) if i != pergunta["resposta"]]
                    eliminadas = random.sample(opcoes_erradas, 2)  #Remove duas opções incorretas.
                    print("\nOpções restantes:")
                    for i, alternativa in enumerate(pergunta["opcoes"]):  #Mostra as opções restantes.
                        if i not in eliminadas:
                            print(f"{i + 1}: {alternativa}")
                elif tipo_dica == "2":  #Caso o jogador escolha pular a questão.
                    print("\nVocê escolheu pular a questão.")
                    pendentes.append(pergunta)  #Adiciona a questão à lista de pendentes.
                    dicas -= 1  #Reduz o número de dicas disponíveis.
                    break
                elif tipo_dica == "3":  #Caso o jogador escolha obter uma dica.
                    print(f"\nDica: {pergunta['dica']}")  #Mostra a dica da questão.
                dicas -= 1  #Reduz o número de dicas após usar.
                continue  #Retorna ao início do loop.
            #Valida a resposta fornecida pelo jogador.
            if not resposta.isdigit() or int(resposta) not in range(1, 6):
                print('Essa alternativa não existe. Escolha entre 1 e 5.')
                continue
            #Verifica se a resposta está correta.
            resposta_inteira = int(resposta)
            if resposta_inteira == pergunta['resposta'] + 1:
                print("Resposta correta!")
                acertos[0] += 1  #Incrementa o contador de acertos.
                if acertos[0] % 3 == 0:  #Da uma dica extra a cada 3 acertos.
                    dicas += 1
                    print("Você ganhou uma dica!")
            else:
                print("Resposta incorreta!")
                pendentes.append(pergunta)  #Adiciona a questão à lista de pendentes.
            break  #Sai do loop da resposta.
        if not rodando["status"]:  #Sai do loop principal se o tempo acabar.
            break
    rodando["status"] = False  #Finaliza o jogo.
    thread_tempo.join()  #Aguarda o encerramento do temporizador.
    #Calcula o tempo restante.
    tempo_restante = tempo_total - int(time.time() - inicio_jogo)
    if tempo_restante < 0:  #Evita valores negativos no tempo restante.
        tempo_restante = 0
    if tempo_restante > 0: 
        print(f"\nTempo restante: {tempo_restante} segundos")  #Mostra o tempo restante.
        print(f"Você acertou {acertos[0]} questões.")  #Mostra o número de acertos.
        print(f"Sua pontuação final é {tempo_restante} pontos.")  #Mostra a pontuação final.
        atualizar_hall_da_fama("modo2", nome_jogador, tempo_restante)  #Atualiza o Hall da Fama.

#Modo 3: Tente Não Errar.
#Termina ao errar uma resposta ou responder todas as perguntas.
def modo3(jogo3, nome_jogador):
    s = 0  #Pontuação inicial.
    ajudas = 1  #Número inicial de ajudas.
    acertos = 0  #Contador de acertos.
    perguntas_feitas = set()  #Armazena os índices das perguntas já feitas.

    for _ in range(10):  #Loop para até 10 perguntas ou até errar.
        while True:  #Seleciona uma pergunta que ainda não foi feita.
            indice = random.randint(0, len(jogo3) - 1)
            if indice not in perguntas_feitas:  #Verifica se a pergunta já foi feita.
                perguntas_feitas.add(indice)  #Marca a pergunta como feita.
                break
        pergunta = jogo3[indice]  #Seleciona a pergunta.
        print(f'\n{pergunta["pergunta"]}')  #Mostra a pergunta.
        for i, alternativa in enumerate(pergunta['opcoes']):  #Lista as alternativas.
            print(f'{i + 1}: {alternativa}')
        if ajudas > 0:  #Informa o número de ajudas disponíveis.
            print(f'6: Você tem {ajudas} ajuda(s) disponível(is).')
        resposta = input('\nResposta: ')  #Recebe a resposta do jogador.
        if resposta == '6' and ajudas > 0:  #Ativa a ajuda, se disponível.
            resultado_ajuda = usar_ajuda(ajudas, pergunta)  #Chama a função de ajuda.
            if isinstance(resultado_ajuda, tuple) and resultado_ajuda[0] == -1:  #Pula a questão.
                ajudas = resultado_ajuda[1]
                continue
            ajudas = resultado_ajuda
            resposta = input('Escolha sua resposta novamente: ')  #Pede nova resposta.
        while not resposta.isdigit() or int(resposta) not in range(1, 6):  #Valida a resposta.
            print('Escolha uma alternativa válida.')
            resposta = input()
        respostaint = int(resposta)  #Converte a resposta para inteiro.
        if respostaint == pergunta['resposta'] + 1:  #Verifica se está correta.
            print('Resposta correta!')
            s += pergunta['valor']  #Adiciona pontos.
            acertos += 1  #Incrementa o contador de acertos.
            if acertos % 3 == 0:  #Da uma ajuda extra a cada 3 acertos.
                ajudas += 1
                print('Parabéns! Você ganhou uma ajuda extra.')
        else:
            print('Você errou e o jogo terminou.')
            print(pergunta['explicacao'])  #Mostra a explicação.
            break
    print(f'Você acertou {acertos} questões e fez {s} pontos.')  #Mostra o desempenho final.
    atualizar_hall_da_fama('modo3', nome_jogador, s)  #Atualiza o Hall da Fama.

#Lógica principal do jogo.
print('\nBem-vindo ao Quiz!')  #Mensagem de boas-vindas.
nome_jogador = input('Digite seu nome: ')  #Pede o nome do jogador.
while nome_jogador == '':  #Impede nome vazio.
    nome_jogador = input('Digite seu nome: ')
print(f'Bem-vindo(a), {nome_jogador}!')

while True:  #Loop do menu principal.
    menu = input('\n1 - Jogar\n2 - Manual do jogo\n3 - Mostrar hall da fama\n4 - Sair\n\n')  #Mostrar o menu.
    if menu == '4':  #Sai do jogo.
        break
    elif menu == '2':  #Mostra o manual.
        print('''\nO quiz é composto por 3 modos, cada questão vale 10 pontos.
Modo 1 (Número de Questões Fixas) - A pontuação do jogador é determinada pela quantidade de respostas corretas em 10 questões apresentadas.
Modo 2 (Limite de Tempo) - A pontuação do jogador é determinada pelo tempo que sobrar após o jogador acertar todas as questões
apresentadas. O usuário tem 120 segundos para responder 10 questões.
Modo 3 (Tente Não Errar) - O jogo termina quando o jogador errar uma resposta ou quando todas as questões (10) forem respondidas
pelo jogador.\nO jogador começa com 1 ajuda e ganha mais após acertar 3 questões.''')
    elif menu == '3':  #Mostra o Hall da Fama.
        mostrar_hall_da_fama()
    elif menu == '1':  #Inicia o jogo.
        modo = input('\n1 - Número de Questões Fixas\n2 - Limite de Tempo\n3 - Tente Não Errar\n\n')  #Escolha do modo.
        while modo not in ['1', '2', '3']:  #Valida a escolha.
            print('Escolha um modo de jogo válido:\n')
            modo = input('\n1 - Número de Questões Fixas\n2 - Limite de Tempo\n3 - Tente Não Errar\n\n')
        if modo == '1':
            modo1(questoes, nome_jogador) #Chama a função do modo 1.
        elif modo == '2':
            modo2(questoes, nome_jogador) #Chama a função do modo 2.
        elif modo == '3':
            modo3(questoes, nome_jogador) #Chama a função do modo 3.
