#!/usr/bin/env python
# coding: utf-8

# # Exercício - Mini Projeto de Análise de Dados
# BEATRIZ CARELLI DIAS
# 
# Vamos fazer um exercício completo de pandas para um miniprojeto de análise de dados.
# 
# Esse exercício vai obrigar a gente a usar boa parte dos conhecimento de pandas e até de outros módulos que já aprendemos ao longo do curso.
# 
# O que temos?
# Temos os dados de 2019 de uma empresa de prestação de serviços.
# 
# CadastroFuncionarios
# CadastroClientes
# BaseServiçosPrestados
# Obs1: Para ler arquivos csv, temos o read_csv
# Obs2: Para ler arquivos xlsx (arquivos em excel normais, que não são padrão csv), temos o read_excel
# 
# O que queremos saber/fazer?
# Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa?
# Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários
# Qual foi o faturamento da empresa?
# Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos
# Qual o % de funcionários que já fechou algum contrato?
# Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.
# . Na base de funcionários temos uma lista com todos os funcionários
# . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais
# . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.
# 
# Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.
# Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA
# Calcule o total de contratos que cada área da empresa já fechou
# Calcule o total de funcionários por área
# Qual o ticket médio mensal (faturamento médio mensal) dos contratos?
# Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()
# Obs: Lembrando as opções mais usuais de encoding:
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
# 
# Observação Importante: Se o seu código der um erro na hora de importar os arquivos:
# 
# CadastroClientes.csv
# CadastroFuncionarios.csv
# Use separador ";" (ponto e vírgula) para resolver
# 

# ### IMPORTAÇÃO DE MÓDULOS E ARQUIVOS

# In[3]:


import pandas as pd


# In[15]:


funcionarios_df = pd.read_csv(r'CadastroFuncionarios.csv', sep = ';', decimal = ',')
##retirar colunas que não farão diferença no código
funcionarios_df = funcionarios_df.drop([r'Estado Civil', 'Cargo'], axis = 1)
print(funcionarios_df)  


# In[13]:


clientes_df = pd.read_csv(r'CadastroClientes.csv', sep = ';', decimal = ',')
print(clientes_df)


# In[7]:


base_df = pd.read_excel(r'BaseServiçosPrestados.xlsx')
print(base_df)


# ### SOLUÇÃO 1- FOLHA SALARIAL

# In[8]:


funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios']
print('A soma de todos os salarios foi igual à R${:,}'.format(funcionarios_df['Salario Total'].sum()))


# ### SOLUÇÃO 2- FATURAMENTO DA EMPRESA

# In[9]:


faturamentos_df = base_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']])
faturamentos_df['Faturamento Total'] = clientes_df['Valor Contrato Mensal'] * base_df['Tempo Total de Contrato (Meses)']
print('O faturamento total da empresa foi de R${:,}'.format(faturamentos_df['Faturamento Total'].sum()))


# ### SOLUÇÃO 3- PORCENTAGEM DE FUNCIONÁRIOS QUE FECHARAM CONTRATO

# In[10]:


qtd_funcionarios_fecharam_contrato = len(base_df['ID Funcionário'].unique())
qtd_funcionarios_total = len(funcionarios_df['ID Funcionário'])
print('A porcentagem de funcionários que fecharam contrato foi de {:.2%}'.format(qtd_funcionarios_fecharam_contrato / qtd_funcionarios_total))


# ### SOLUÇÃO 4- QUANTIDADE DE CONTRATOS QUE CADA ÁREA JA FECHOU

# In[11]:


contratos_por_area = base_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on = 'ID Funcionário')
contratos_por_area_qtd = contratos_por_area['Area'].value_counts()
print(contratos_por_area_qtd)
contratos_por_area_qtd.plot(kind='bar')


# ### SOLUÇÃO 5- TOTAL DE FUNCIONÁRIOS POR ÁREA

# In[22]:


funcionario_por_area = funcionarios_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on = 'ID Funcionário')
funcionario_por_area_qtd = funcionario_por_area['Area'].value_counts()
print(funcionario_por_area_qtd)
funcionario_por_area_qtd.plot(kind='bar')


# In[12]:


ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio é igual R$ {:,}'.format(ticket_medio))


# In[ ]:




