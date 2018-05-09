# Banco Nacional de Mandados de Prisão

Conjunto de scripts para listar e pegar detalhes dos mandados de prisão
contidos no BNMP.

**ATENÇÃO**:

- Mandados entram e saem o tempo todo, então você precisará rodar esse script
  com alguma frequência para ter os dados atualizados;
- [Esse banco de dados contém dados sigilosos](https://www1.folha.uol.com.br/cotidiano/2018/04/sistema-da-justica-viola-sigilo-e-expoe-criancas-vitimas-de-estupro.shtml),
  **não publique** os dados baixados sem antes ter certeza de que você não
  estará comprometendo o sigilo de algumas pessoas (e cometendo um crime).

## Rodando

Depende de Python 3.6+.

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Rode os spiders com:

```bash
./run.sh
```
