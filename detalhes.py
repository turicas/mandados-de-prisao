import json

import scrapy


class BNMPDetailSpider(scrapy.Spider):
    name = 'detalhes-mandados'

    def _make_request(self, id):
        payload = {'id': id,}
        return scrapy.FormRequest(
            'http://www.cnj.jus.br/bnmp/rest/detalhar',
            body=json.dumps(payload),
            headers={'Content-Type': 'application/json'},
            method='POST',
        )

    def start_requests(self):
        with open('listagem.jl', mode='r', encoding='utf-8') as fobj:
            for line in fobj:
                data = json.loads(line)
                yield self._make_request(data['id'])

    def parse(self, response):
        data = json.loads(response.body)
        yield data
