import requests


class CEP:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!!!")

    def __str__(self):
        return self.format_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])


    def acessa_via_cep(self):
        url = "https://vaicep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return(
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
