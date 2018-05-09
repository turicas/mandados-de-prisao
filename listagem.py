import json

import scrapy


states = 'AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO'.split()

class BNMPListSpider(scrapy.Spider):
    name = 'listagem-mandados'

    def _make_request(self, state, page):
        search_payload = {
            'criterio': {
                'orgaoJulgador': {
                    'uf': '',
                    'municipio': '',
                    'descricao': '',
                },
                'orgaoJTR': {},
                'parte': {},
            },
            'paginador': {
                'paginaAtual': page,
            },
            'fonetica': 'true',
            'ordenacao': {
                'porNome': 'false',
                'porData': 'false',
            },
        }
        payload = search_payload.copy()
        payload['criterio']['orgaoJulgador']['uf'] = state
        return scrapy.FormRequest(
            'http://www.cnj.jus.br/bnmp/rest/pesquisar',
            body=json.dumps(payload),
            headers={'Content-Type': 'application/json'},
            meta={'state': state},
            method='POST',
        )

    def start_requests(self):
        for state in states:
            yield self._make_request(state=state, page=1)

    def parse(self, response):
        data = json.loads(response.body)
        pagination = data['paginador']
        current_page = pagination['paginaAtual']
        state = response.request.meta['state']

        for row in data['mandados']:
            row['uf'] = state
            yield row

        if pagination['totalPaginas'] > current_page:
            yield self._make_request(state=state, page=current_page + 1)
