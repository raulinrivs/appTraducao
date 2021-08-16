arquivo = open('modelo_arquivo.txt', 'r')
documento = arquivo.readlines()
relatorio = {
    'headerArquivo': '',
    'lotes': [],
    'trailerArquivo': '',
}

def lerHeaderArquivo(linha):
    headerArquivo = {
        'banco' : linha[0:3],
        'lote': linha[3:7],
        'registro': linha[7],
        'filler': linha[8:17],
        'tipo': linha[17],
        #'numero': linha[18:32],
        'numero': linha[18:20] + '.' + linha[20:23] + '.' + linha[23:26] + '/' + linha[26:30] + '-' + linha[30:32],
        'convenio': linha[32:52],
        'agenciaCod': linha[52:57],
        'agenciaDv': linha[57],
        'contaCod': linha[58:70],
        'contaDv': linha[70],
        'dv': linha[71],
        'nomeEmpresa': linha[72:102],
        'nomeBanco': linha[102:132],
        'nomeDaVan': linha[132:142],
        'arquivoCodigo': linha[142],
        #'arquivoDataDeGeracao': linha[143:151],
        'arquivoDataDeGeracao': linha[143:145] + '/' + linha[145:147] + '/' + linha[147:151],
        'arquivoHoraDeGeracao': linha[151:157],
        'arquivoSequencia': linha[157:164],
        'arquivoLayout': linha[164:167],
        'arquivoDesidade': linha[167:172],
        'reservadoBanco': linha[172:191],
        'reservadoEmpresa': linha[191:211],
        'cnab': linha[211:240]
    }
    print('Leitura Header arquivo')
    return headerArquivo

def lerHeaderLote(linha):
    headerLote = {
        #CONTROLE
        'banco' : linha[0:3],
        'lote': linha[3:7],
        'registro': linha[7],
        #SERVIÇO
        'operacao': linha[8],
        'servico': linha[9:11],
        'formaLancamento': linha[11:13],
        'layoutDoLote': linha[13:16],
        'filler': linha[16],
        #EMPRESA
        'iscricaoTipo': linha[17],
        'inscricaoNumero': linha[18:20] + '.' + linha[20:23] + '.' + linha[23:26] + '/' + linha[26:30] + '-' + linha[30:32],
        'convenio': linha[32:52],
        #EMPRESA/CONTA CORRENTE
        'agenciaCod': linha[52:57],
        'agenciaDv': linha[57],
        'contaCod': linha[58:70],
        'contaDv': linha[70],
        'dv': linha[71],
        'nomeEmpresa': linha[72:102],
        'mensagem': linha[102:142],
        #ENDERECO DA EMPRESA
        'enderecoLogradouro': linha[142:172],
        'enderecoNumero': linha[172:177],
        'enderecoComplemento': linha[177:192],
        'enderecoCidade': linha[192:212],
        'enderecoCep': linha[212:217],
        'enderecoComplementoCep': linha[217:220],
        'enderecoEstado': linha[220:222],
        'filler2': linha[222:230],
        'ocorrecia': linha[230:240]
    }
    print('Leitura Header lote')
    return headerLote

def lerRegistroDetalhes(linha):
    registroDetalhes = {
        #CONTROLE
        'banco' : linha[0:3],
        'lote': linha[3:7],
        'registro': linha[7],
        #SERVIÇO
        'numDoRegistro': linha[8:13],
        'seguimento': linha[13],
        'movimentoTipo': linha[14],
        'movimentoCodigo': linha[15:17],
        #FAVORECIDO
        'camara': linha[17:20],
        'banco': linha[20:23],
        #FAVORECIDO/CONTA CORRENTE
        'agenciaCod': linha[23:28],
        'agenciaDv': linha[28],
        'contaCod': linha[29:41],
        'contaDv': linha[41],
        'dv': linha[42],
        'nome': linha[43:73],
        #CREDITO
        'numero': linha[73:93],
        'dataPagamento': linha[93:95] + '/' + linha[95:97] + '/' + linha[97:101],
        'moedaTipo': linha[101:104],
        'moedaQuantidade': linha[104:119],
        'valorPagamento': linha[119:132] + '.' + linha[132:134],
        #'valorPagamento': linha[119] + '.' + linha[120:123] + '.' + linha[123:126] + '.' + linha[126:129] + '.' + linha[129:132] + ',' + linha[132:134],
        'nossoNumero': linha[134:154],
        'dataReal': linha[154:162],
        'valorReal': linha[162:177],
        'informacao2': linha[177:217],
        'codigoDoc': linha[217:219],
        'codigoFinalidadeDoc': linha[219:224],
        'codigoLancamento': linha[224:229],
        'aviso': linha[229],
        'ocorrencias': linha[230:240]
    }

    valorPagamento = float(registroDetalhes['valorPagamento'])
    valorPagamento = '{:_.2f}'.format(valorPagamento)
    registroDetalhes['valorPagamento'] = valorPagamento.replace('.',',').replace('_', '.')
    if registroDetalhes['moedaTipo'] == 'BRL':
        registroDetalhes['valorPagamento'] = 'R$ ' + registroDetalhes['valorPagamento']
    print('Leitura Registro detalhes')
    return registroDetalhes

def lerTrailerLote(linha):
    trailerLote = {
        #CONTROLE
        'banco' : linha[0:3],
        'lote': linha[3:7],
        'registro': linha[7],
        'nexxera': linha[8:17],
        'quantidadeRegistros': linha[17:23],
        'valor': linha[23:41],
        'quantidadeMoeda': linha[41:59],
        'numeroAvisoDebito': linha[59:65],
        'nexxera': linha[65:230],
        'ocorrencias': linha[230:240],
    }
    print('Leitura Trailer lote')
    return trailerLote

def lerTrailerArquivo(linha):
    trailerArquivo = {
        #CONTROLE
        'banco' : linha[0:3],
        'lote': linha[3:7],
        'registro': linha[7],
        'filler': linha[8:17],
        #TOTAIS
        'quantidadeLotes': linha[17:23],
        'quantidadeRegistros': linha[23:29],
        'quantidadeContasConcil': linha[29:35],
        'filler2': linha[35:240]
    }
    print('Leitura Trailer arquivo')
    return trailerArquivo

def tabelaG029(codigo):
    print('Traduzindo Codigo de Lançamento: ' + codigo)
    if codigo == '01  ':
        return 'Credito em Conta Corrente'
    elif codigo == '02  ':
        return 'Cheque Pagamento / Administrativo'
    elif codigo == '03  ':
        return 'DOC/TED'
    elif codigo == '04  ':
        return 'Cartao Salario'
    elif codigo == '05  ':
        return 'Credito em Conta Poupança'
    elif codigo == '06  ':
        return 'Libertaçao de Titulos HSBC'
    elif codigo == '07  ':
        return 'Emissao de Cheque Salario'
    elif codigo == '08  ':
        return 'Liquidaçao de Parcelas de Cobrança Nao Registrada'
    elif codigo == '09  ':
        return 'Arrecadação de Tributos Federais'
    elif codigo == '10  ':
        return 'OP a Disposição'
    elif codigo == '11  ':
        return 'Pagamento de Contas e Tributos com Codigo de Barras'
    elif codigo == '12  ':
        return 'Doc Mesma Titularidades'
    elif codigo == '13  ':
        return 'Pagamentos de Guias'
    elif codigo == '14  ':
        return 'Credito em Conta Corrente Mesma Titularidade'
    elif codigo == '16  ':
        return 'Tributo - DARF Normal'
    elif codigo == '17  ':
        return 'Tributo - GPS (Guia da Previdência Social)'
    elif codigo == '18  ':
        return 'Tributo - DARF Simples'
    elif codigo == '19  ':
        return 'Tributo - IPTU - Prefeituras'
    elif codigo == '20  ':
        return 'Pagamento com Autenticaçao'
    elif codigo == '21  ':
        return 'Tributo - DARJ'
    else:
        return '    '

def gerarRelatorioTxt(relatorio):
    arquivo = open('relatorio_gerado.txt', 'w+')
    arquivo.writelines('------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    arquivo.writelines('Nome da Empresa                | Numero de Inscricao da Empresa | Nome do Banco                  | Nome da Rua                    | Numero do Local | Nome da Cidade       | CEP       | Sigla do Estado\n')
    arquivo.writelines('------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    arquivo.writelines(relatorio['headerArquivo']['nomeEmpresa'] + ' | ' + relatorio['headerArquivo']['numero'] + '            ' + ' | ' + relatorio['headerArquivo']['nomeBanco'] + ' | ' + relatorio['lotes'][0]['enderecoLogradouro'] + ' | ' + relatorio['lotes'][0]['enderecoNumero'] + '          ' + ' | ' + relatorio['lotes'][0]['enderecoCidade'] + ' | ' + relatorio['lotes'][0]['enderecoCep'] + '-' + relatorio['lotes'][0]['enderecoComplementoCep'] + ' | ' + relatorio['lotes'][0]['enderecoEstado'] + '\n')
    arquivo.writelines('------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    arquivo.writelines('--------------------------------------------------------------------------------------------------------------------------------------\n')
    arquivo.writelines('Nome do Favorecido             | Data de Pagamento | Valor do Pagamento | Numero do Documento Atribuido pela Empresa | Forma de Lancamento\n')
    arquivo.writelines('--------------------------------------------------------------------------------------------------------------------------------------\n')
    for linha in relatorio['lotes']:
        if linha['registro'] == '3':
            if len(linha['valorPagamento']) < 18: #Adiciona espaços de forma dinâmica no valorPagamento
                linha['valorPagamento'] = linha['valorPagamento'] + ((18 - len(linha['valorPagamento'])) * (' '))
            linha['codigoLancamento'] = tabelaG029(linha['codigoLancamento']) #Traduz codigoLancamento
            arquivo.writelines(linha['nome'] + ' | ' + linha['dataPagamento'] + '       ' + ' | ' + linha['valorPagamento'] + ' | ' + linha['numero'] + '                      ' + ' | ' + linha['codigoLancamento'] + '\n')
    arquivo.writelines('--------------------------------------------------------------------------------------------------------------------------------------\n')
    print('Gerando Relatório TXT')
    arquivo.close()
    return arquivo

def gerarRelatorioCsv(relatorio):
    arquivo = open('relatorio_gerado.csv', 'w+')
    arquivo.writelines('Nome da Empresa;Numero de Inscricao da Empresa;Nome do Banco;Nome da Rua;Numero do Local;Nome da Cidade;CEP;Sigla do Estado\n')
    arquivo.writelines(relatorio['headerArquivo']['nomeEmpresa'].rstrip() + ';' + relatorio['headerArquivo']['numero'].rstrip() + ';' + relatorio['headerArquivo']['nomeBanco'].rstrip() + ';' + relatorio['lotes'][0]['enderecoLogradouro'].rstrip() + ';' + relatorio['lotes'][0]['enderecoNumero'].rstrip() + ';' + relatorio['lotes'][0]['enderecoCidade'].rstrip() + ';' + relatorio['lotes'][0]['enderecoCep'] + '-' + relatorio['lotes'][0]['enderecoComplementoCep'].rstrip() + ';' + relatorio['lotes'][0]['enderecoEstado'] + '\n')
    arquivo.writelines('Nome do Favorecido;Data de Pagamento;Valor do Pagamento;Numero do Documento Atribuido pela Empresa;Forma de Lancamento\n')
    for linha in relatorio['lotes']:
        if linha['registro'] == '3':
            arquivo.writelines(linha['nome'].rstrip() + ';' + linha['dataPagamento'].rstrip() + ';' + linha['valorPagamento'].rstrip() + ';' + linha['numero'].rstrip() + ';' + linha['codigoLancamento'].rstrip() + ';' + '\n')
    print('Gerando Relatório CSV')
    arquivo.close()
    return arquivo

def gerarRelatorioHtml(relatorio):
    arquivo = open('relatorio_gerado.html', 'w+')
    arquivo.writelines('<html>\n    <body>\n        <table border="1">\n            <tr>\n                <th>Nome da Empresa</th>\n                <th>Numero de Inscricao da Empresa</th>\n                <th>Nome do Banco</th>\n                <th>Nome da Rua</th>\n                <th>Numero do Local</th>\n                <th>Nome da Cidade</th>\n                <th>CEP</th>\n                <th>Sigla do Estado</th>\n            </tr>\n')
    arquivo.writelines('            <tr>\n                <td>'+ relatorio['headerArquivo']['nomeEmpresa'].rstrip() +'</td>\n                <td>'+ relatorio['headerArquivo']['numero'].rstrip() +'</td>\n                <td>'+ relatorio['headerArquivo']['nomeBanco'].rstrip() +'</td>\n				<td>'+ relatorio['lotes'][0]['enderecoLogradouro'].rstrip() +'</td>\n				<td>'+ relatorio['lotes'][0]['enderecoNumero'].rstrip() +'</td>\n				<td>'+ relatorio['lotes'][0]['enderecoCidade'].rstrip() +'</td>\n				<td>'+ relatorio['lotes'][0]['enderecoCep'] + '-' + relatorio['lotes'][0]['enderecoComplementoCep'].rstrip() +'</td>\n				<td>'+ relatorio['lotes'][0]['enderecoEstado'] +'</td>\n            </tr>\n')
    arquivo.writelines('        </table>\n        <br/>\n        <table border="1">\n            <tr>\n                <th>Nome do Favorecido</th>\n                <th>Data de Pagamento</th>\n                <th>Valor do Pagamento</th>\n                <th>Numero do Documento Atribuido pela Empresa</th>\n                <th>Forma de Lancamento</th>\n            </tr>\n')
    for linha in relatorio['lotes']:
        if linha['registro'] == '3':
            arquivo.writelines('            <tr>\n                <td>'+ linha['nome'].rstrip() +'</td>\n                <td>'+ linha['dataPagamento'].rstrip() +'</td>\n                <td>'+ linha['valorPagamento'].rstrip() +'</td>\n                <td>'+ linha['numero'].rstrip() +'</td>\n                <td>'+ linha['codigoLancamento'].rstrip() +'</td>\n            </tr>\n')
    arquivo.writelines('        </table>\n    </body>\n</html>')
    print('Gerando Relatório HTML')
    arquivo.close()
    return arquivo

for linha in documento:
    if linha[7] == '0':
        relatorio['headerArquivo'] = lerHeaderArquivo(linha)
    elif linha[7] == '1':
        relatorio['lotes'].append(lerHeaderLote(linha))
    elif linha[7] == '3':
        relatorio['lotes'].append(lerRegistroDetalhes(linha))
    elif linha[7] == '5':
        relatorio['lotes'].append(lerTrailerLote(linha))
    elif linha[7] == '9':
        relatorio['trailerArquivo'] = lerTrailerArquivo(linha)

gerarRelatorioTxt(relatorio)
gerarRelatorioCsv(relatorio)
gerarRelatorioHtml(relatorio)
arquivo.close()