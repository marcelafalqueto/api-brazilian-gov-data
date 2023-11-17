import csv
import sqlite3


conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS meus_dados (
        cadastro TEXT,
        codigo_da_sancao TEXT,
        tipo_de_pessoa TEXT,
        cpf_ou_cnpj INTEGER PRIMARY KEY,
        nome TEXT,
        nome_informado TEXT,
        razao_social TEXT,
        nome_fantasia TEXT,
        numero_processo TEXT,
        categoria TEXT,
        data_final TEXT,
        data_publicacao TEXT,
        publicacao TEXT,
        detalhamento TEXT,
        data_transito TEXT,
        abrangencia TEXT,
        orgao_sancionador TEXT,
        uf TEXT,
        fundamentacao_legal TEXT
    );
""")

with open('CEIS.csv', 'r', newline='', encoding="utf-8") as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')
    for linha in leitor_csv:
        cursor.execute('''
            INSERT OR REPLACE INTO meus_dados (cadastro,
            codigo_da_sancao,
            tipo_de_pessoa,
            cpf_ou_cnpj,
            nome,
            nome_informado,
            razao_social,
            nome_fantasia,
            numero_processo,
            categoria,
            data_final,
            data_publicacao,
            publicacao,
            detalhamento,
            data_transito,
            abrangencia,
            orgao_sancionador,
            uf,
            fundamentacao_legal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (linha["CADASTRO"], linha["C�DIGO DA SAN��O"], linha["TIPO DE PESSOA"], linha["CPF OU CNPJ DO SANCIONADO"], 
        linha["NOME DO SANCIONADO"], linha["NOME INFORMADO PELO �RG�O SANCIONADOR"], 
        linha["RAZ�O SOCIAL - CADASTRO RECEITA"], linha["NOME FANTASIA - CADASTRO RECEITA"], 
        linha["N�MERO DO PROCESSO"], linha["CATEGORIA DA SAN��O"], linha["DATA IN�CIO SAN��O"], 
        linha["DATA PUBLICA��O"], linha["PUBLICA��O"], 
        linha["DETALHAMENTO"], linha["DATA DO TR�NSITO EM JULGADO"], linha["ABRAG�NCIA DEFINIDA EM DECIS�O JUDICIAL"], 
        linha["�RG�O SANCIONADOR"], linha["UF �RG�O SANCIONADOR"], 
        linha["FUNDAMENTA��O LEGAL"]))

conexao.commit()
conexao.close()

