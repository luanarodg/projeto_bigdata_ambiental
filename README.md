# Projeto Final de Big Data no Databricks


### Estrutura
```
├── extract_raw.py -> Transforma o arquivo csv em parquet
├── projeto_final_bigdata.dbc -> Todo o código da arquitetura de dados no Databricks.
└── README.md
```

### Overview
O objetivo deste trabalho é explorar as capacidades de arquiteturas de bancos de dados distribuídos para lidar com conjuntos de dados "grandes", em particular, o "Cadastro Ambiental Rural".

O "Cadastro Ambiental Rural" é um conjunto de dados que contém informações sobre propriedades rurais no Brasil. Os dados estão dispníveis no link https://dados.gov.br/dados/conjuntos-dados/cadastro-ambiental-rural1.

O desafio é projetar uma arquitetura que possibilite o gerenciamento eficiente desses dados, permitindo consultas e análises rápidas, mesmo diante do tamanho considerável da base de dados.


Para esse projeto foram utilizadas as seguintes ferramentas:

Python e Spark -> para processamento dos dados;

Hive -> Data Warehouse utilizada para consulta de grande conjunto de dados;

Databricks -> Plataforma utilizada para toda a construção da arquitetura de dados.

-----------

O conjunto de dados foi extraído em ```csv``` da origem, por causa do tamanho do arquivo, o mesmo foi transformado em ```parquet``` para melhor processamento.

Com os dados extraídos, a arquitetura do Data Lake foi feita aplicando o conceito de **"Arquitetura Medalhão"**, onde se adota camadas de transformação até a disponibilidade final dos dados para consulta. Neste trabalho foram utilizadas as camadas ```bronze```, ```silver``` e ```gold```.

Na ```camada bronze``` é onde os dados estão exatamente do jeito que foram extraídos, no formato **raw**, sem nenhuma transformação.

Já na ```camada silver``` é onde ocorre toda a transformação dos dados. Nos dados foram feitas algumas transformações como tratamento dos dados nulos, tipagem adequada dos dados, etc.

E por fim, na ```camada gold``` os dados já estão disponíveis de forma adequada para consulta.

Os dados foram armazenados com partições de *ano*, *mês* e *uf* para melhor organização. Foi criado banco de dados para armazenar as tabelas dos dados nas três camadas, no diretório __*dbfs:/user/hive/warehouse/*__. Além disso, a base de dados extraída também se encontra no dbfs, __*dbfs:/FileStore/tables/temas_ambientais.parquet*__