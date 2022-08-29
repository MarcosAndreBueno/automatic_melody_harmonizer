'''
canoa virou: 
notas ['G', 'E', 'C', 'A', 'R', 'H', 'G', 'C', 'C', 'R', 'H', 'C', 'C']
originalAcordes = ['D', 'T', 'T', 'S', 'S', 'D', 'D', 'T', 'T', 'G', 'G', 'T', 'T']
alecrim dourado: 
notas = ['G','E','F','F','E','G','E','F','F','E','C','C','C','G','F','E','C','C','C','G','F','E']
originalAcordes = ['D','T','D','T','D','D','D','D','T','T','S','S','T','D','T','T','S','S','T','D','D','T']
'''

# Transition Probabilities
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.Tonalidade.Escala2 import Escala2
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.compasso.PrimeiroCompasso import PrimeiroCompasso


class Viterbi:
    def __init__(self):
        # Matriz de transição
        self.p_tt = 0.3333  # tônica para tônica
        self.p_ts = 0.1515  # tônica para subdominante (sempre 0, mas tê-lo ajuda a compreensão do código)
        self.p_td = 0.5152  # tônica para dominante
        self.p_st = 0.0
        self.p_ss = 0.8
        self.p_sd = 0.2
        self.p_dt = 0.3636
        self.p_ds = 0.0
        self.p_dd = 0.6364
        
        # Probabilidade inicial
        self.p_t = 0.8
        self.p_s = 0.0
        self.p_d = 0.2
        
        # Matriz de Emissão
        self.p_tc = 0.9260  # dó estar na tônica (dó = degrau 1 da tonalidade inserida)
        self.p_tr = 0.3530  # ré estar na tônica (ré = degrau 1 da tonalidade inserida)
        self.p_te = 0.7021  # mi estar na tônica (mi = degrau 1 da tonalidade inserida)
        self.p_tf = 0.0145  # fá estar na tônica (fá = degrau 1 da tonalidade inserida)
        self.p_tg = 0.5357  # sol estar na tônica (sol = degrau 1 da tonalidade inserida)
        self.p_ta = 0.2727  # la estar na tônica (lá = degrau 1 da tonalidade inserida)
        self.p_th = 0.0555  # si estar na tônica (si = degrau 1 da tonalidade inserida)
        self.p_sc = 0.0
        self.p_sr = 0.0
        self.p_se = 0.0
        self.p_sf = 0.0
        self.p_sg = 0.0
        self.p_sa = 0.5455
        self.p_sh = 0.2778
        self.p_dc = 0.0740
        self.p_dr = 0.6470
        self.p_de = 0.2979
        self.p_df = 0.9855
        self.p_dg = 0.4643
        self.p_da = 0.1818
        self.p_dh = 0.6667

        edp = ExtrairDadosPartitura()
        bho = BeatsHarmonizarObtidos2()
        self.notas = edp.getNome()
        self.degrau = ''
        self.beatHarm = bho.get_beat_harm()
        self.observado = []
        self.probabilities = []
        self.prob_anterior_ton = []
        self.prob_anterior_sub = []
        self.prob_anterior_dom = []
        self.ton_anterior = 0
        self.sub_anterior = 0
        self.dom_anterior = 0

        pc = PrimeiroCompasso()
        self.incomplete_compass = pc.get_compasso_status()
        self.incomplete_tamanho = pc.get_compass_tamanho()

    # set melodia que será harmonizada
    def estados_observaveis(self):
        for x in range(len(self.notas)):
            beatAt = self.beatHarm[x]
            ec = Escala2()
            self.degrau = ec.get_degrau_from_another()

            # se não
            if beatAt == 1:
                self.observado.append(self.degrau[x])
            else:
                # manter tamanho da lista igual às demais listas
                self.observado.append(0)

        # em caso de anácruse/acéfalo, ignora compasso inicial inteiro
        if self.incomplete_compass == True:
            for x in range(0, self.incomplete_tamanho):
                resultado.append(0)

    def start_probabilities(self):
        match self.observado[self.incomplete_tamanho]:
            case 0: # beat não aceito para harmonizar
                resultado.append(0) # mantém a lista do mesmo tamanho das outras listas extraídas
            case 1:
                self.ton_anterior = self.p_t * self.p_tc
                self.sub_anterior = self.p_s * self.p_tc
                self.dom_anterior = self.p_d * self.p_tc
            case 2:
                self.ton_anterior = self.p_t * self.p_tr
                self.sub_anterior = self.p_s * self.p_sr
                self.dom_anterior = self.p_d * self.p_dr
            case 3:
                self.ton_anterior = self.p_t * self.p_te
                self.sub_anterior = self.p_s * self.p_se
                self.dom_anterior = self.p_d * self.p_de
            case 4:
                self.ton_anterior = self.p_t * self.p_tf
                self.sub_anterior = self.p_s * self.p_sf
                self.dom_anterior = self.p_d * self.p_df
            case 5:
                self.ton_anterior = self.p_t * self.p_tg
                self.sub_anterior = self.p_s * self.p_sg
                self.dom_anterior = self.p_d * self.p_dg
            case 6:
                self.ton_anterior = self.p_t * self.p_ta
                self.sub_anterior = self.p_s * self.p_sa
                self.dom_anterior = self.p_d * self.p_da
            case 7: # 'H'
                self.ton_anterior = self.p_t * self.p_th
                self.sub_anterior = self.p_s * self.p_sh
                self.dom_anterior = self.p_d * self.p_dh

        self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
        if self.ton_anterior > self.sub_anterior and self.ton_anterior > self.dom_anterior:
            resultado.append('T')
        elif self.sub_anterior > self.dom_anterior:
            resultado.append('S')
        else:
            resultado.append('D')

    def method_hidden(self):
        hiddenT = hiddenS = hiddenD = ''
        ton1 = self.prob_anterior_ton[0][0]
        ton2 = self.prob_anterior_ton[0][1]
        ton3 = self.prob_anterior_ton[0][2]
        sub1 = self.prob_anterior_sub[0][0]
        sub2 = self.prob_anterior_sub[0][1]
        sub3 = self.prob_anterior_sub[0][2]
        dom1 = self.prob_anterior_dom[0][0]
        dom2 = self.prob_anterior_dom[0][1]
        dom3 = self.prob_anterior_dom[0][2]
        self.prob_anterior_ton.clear()
        self.prob_anterior_sub.clear()
        self.prob_anterior_dom.clear()

        if ton1 > ton2 and ton1 > ton3:
            dterFinal = ton1  # dd->dd
            hiddenT = 'T'
        elif ton2 > ton3:
            dterFinal = ton2  # nn->dd
            hiddenT = 'S'
        else:
            dterFinal = ton3  # vb->dd
            hiddenT = 'D'
    
        if sub1 > sub2 and sub1 > sub3:
            nounFinal = sub1  # dd->nn
            hiddenS = 'T'
        elif sub2 > sub3:
            nounFinal = sub2  # nn->nn
            hiddenS = 'S'
        else:
            nounFinal = sub3  # vb->nn
            hiddenS = 'D'
    
        if dom1 > dom2 and dom1 > dom3:
            verbFinal = dom1  # dd->vb
            hiddenD = 'T'
        elif dom2 > dom3:
            verbFinal = dom2  # nn->vb
            hiddenD = 'S'
        else:
            verbFinal = dom3  # vb->vb
            hiddenD = 'D'

        if dterFinal > nounFinal and dterFinal > verbFinal:
            resultado.append(hiddenT)
        elif nounFinal > verbFinal:
            resultado.append(hiddenS)
        else:
            resultado.append(hiddenD)
    
    def interface_viterbi(self):
        global resultado
        resultado = []
        self.estados_observaveis()
        self.start_probabilities()
        # inicia 1 posição após primeiro hidden_state
        for x in range(self.incomplete_tamanho+1, len(self.observado)):
            self.ton_anterior, self.sub_anterior, self.dom_anterior = self.probabilities[-1]
            match self.observado[x]:
                case 0: # beat não aceito para harmonizar
                    resultado.append(0) # mantém a lista do mesmo tamanho das outras listas extraídas
                case 1:
                    ton1 = self.ton_anterior * self.p_tt * self.p_tc  # probabilidade de ser tônica * continuar tônica * "dó" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_tc  # probabilidade de ser subdom * continuar subdom * "dó" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_tc  # probabilidade de ser domina * continuar domina * "dó" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_sc  # probabilidade de ser subdom * continuar subdom * "dó" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_sc
                    sub3 = self.dom_anterior * self.p_ds * self.p_sc
                    dom1 = self.ton_anterior * self.p_td * self.p_dc
                    dom2 = self.sub_anterior * self.p_sd * self.p_dc
                    dom3 = self.dom_anterior * self.p_dd * self.p_dc
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()
                case 2:
                    ton1 = self.ton_anterior * self.p_tt * self.p_tr  # probabilidade de ser tônica * continuar tônica * "ré" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_tr  # probabilidade de ser subdom * continuar subdom * "ré" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_tr  # probabilidade de ser domina * continuar domina * "ré" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_sr  # probabilidade de ser subdom * continuar subdom * "ré" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_sr
                    sub3 = self.dom_anterior * self.p_ds * self.p_sr
                    dom1 = self.ton_anterior * self.p_td * self.p_dr
                    dom2 = self.sub_anterior * self.p_sd * self.p_dr
                    dom3 = self.dom_anterior * self.p_dd * self.p_dr
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()
                case 3:
                    ton1 = self.ton_anterior * self.p_tt * self.p_te  # probabilidade de ser tônica * continuar tônica * "mi" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_te  # probabilidade de ser subdom * continuar subdom * "mi" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_te  # probabilidade de ser domina * continuar domina * "mi" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_se  # probabilidade de ser subdom * continuar subdom * "mi" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_se
                    sub3 = self.dom_anterior * self.p_ds * self.p_se
                    dom1 = self.ton_anterior * self.p_td * self.p_de
                    dom2 = self.sub_anterior * self.p_sd * self.p_de
                    dom3 = self.dom_anterior * self.p_dd * self.p_de
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()
                case 4:
                    ton1 = self.ton_anterior * self.p_tt * self.p_tf  # probabilidade de ser tônica * continuar tônica * "fá" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_tf  # probabilidade de ser subdom * continuar subdom * "fá" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_tf  # probabilidade de ser domina * continuar domina * "fá" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_sf  # probabilidade de ser subdom * continuar subdom * "fá" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_sf
                    sub3 = self.dom_anterior * self.p_ds * self.p_sf
                    dom1 = self.ton_anterior * self.p_td * self.p_df
                    dom2 = self.sub_anterior * self.p_sd * self.p_df
                    dom3 = self.dom_anterior * self.p_dd * self.p_df
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()
                case 5:
                    ton1 = self.ton_anterior * self.p_tt * self.p_tg  # probabilidade de ser tônica * continuar tônica * "sol" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_tg  # probabilidade de ser subdom * continuar subdom * "sol" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_tg  # probabilidade de ser domina * continuar domina * "sol" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_sg  # probabilidade de ser subdom * continuar subdom * "sol" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_sg
                    sub3 = self.dom_anterior * self.p_ds * self.p_sg
                    dom1 = self.ton_anterior * self.p_td * self.p_dg
                    dom2 = self.sub_anterior * self.p_sd * self.p_dg
                    dom3 = self.dom_anterior * self.p_dd * self.p_dg
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()
                case 6:
                    ton1 = self.ton_anterior * self.p_tt * self.p_ta  # probabilidade de ser tônica * continuar tônica * "lá" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_ta  # probabilidade de ser subdom * continuar subdom * "lá" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_ta  # probabilidade de ser domina * continuar domina * "lá" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_sa  # probabilidade de ser subdom * continuar subdom * "lá" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_sa
                    sub3 = self.dom_anterior * self.p_ds * self.p_sa
                    dom1 = self.ton_anterior * self.p_td * self.p_da
                    dom2 = self.sub_anterior * self.p_sd * self.p_da
                    dom3 = self.dom_anterior * self.p_dd * self.p_da
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()
                case 7:
                    ton1 = self.ton_anterior * self.p_tt * self.p_th  # probabilidade de ser tônica * continuar tônica * "si" estar na tônica
                    ton2 = self.sub_anterior * self.p_st * self.p_th  # probabilidade de ser subdom * continuar subdom * "si" estar na subdom
                    ton3 = self.dom_anterior * self.p_dt * self.p_th  # probabilidade de ser domina * continuar domina * "si" estar na domina
                    sub1 = self.ton_anterior * self.p_ts * self.p_sh  # probabilidade de ser subdom * continuar subdom * "si" estar na subdom
                    sub2 = self.sub_anterior * self.p_ss * self.p_sh
                    sub3 = self.dom_anterior * self.p_ds * self.p_sh
                    dom1 = self.ton_anterior * self.p_td * self.p_dh
                    dom2 = self.sub_anterior * self.p_sd * self.p_dh
                    dom3 = self.dom_anterior * self.p_dd * self.p_dh
                    self.prob_anterior_ton.append((ton1, ton2, ton3))
                    self.prob_anterior_sub.append((sub1, sub2, sub3))
                    self.prob_anterior_dom.append((dom1, dom2, dom3))
                    self.ton_anterior = max(ton1, ton2, ton3)
                    self.sub_anterior = max(sub1, sub2, sub3)
                    self.dom_anterior = max(dom1, dom2, dom3)
                    self.probabilities.append((self.ton_anterior, self.sub_anterior, self.dom_anterior))
                    self.method_hidden()

        # set ultimo hidden state
        if self.ton_anterior > self.sub_anterior and self.ton_anterior > self.dom_anterior:
            resultado.append('T')
        elif self.sub_anterior > self.dom_anterior:
            resultado.append('S')
        else:
            resultado.append('D')

        self.set_observated_states()

    def get_hidden_state(self, contador=None):
        if contador == None:
            return resultado
        else:
            return resultado[contador]

    def set_observated_states(self):
        global observated_states
        observated_states = self.observado

    def get_observated_states(self):
        return observated_states

    
    # def print_results(self):
    #     count = 0
    #     for p in self.probabilities:
    #         print("Notas:", self.notas[count],
    #               "Posição:", count,
    #               "\n"
    #               "Tônica:", p[0],
    #               "\n"
    #               "Subdom:", p[1],
    #               "\n"
    #               "Domina: ", p[2],
    #               "\n")
    #         count += 1
    #
    #     print("Notas:    ", self.notas)
    #     print("Ocultos:  ", resultado)
    #     print("Notas em degraus:", self.observado)
