# Lógica Fuzzy — Trabalho de Inteligência Computacional

Implementação de sistemas de inferência baseados em **Lógica Fuzzy (Lógica Difusa)** em Python, aplicados à tomada de decisão sob incerteza em jogos.

## Estrutura do Repositório

* **`Fuzzy_functions.py`**: Motor matemático do sistema principal. Contém as funções de pertinência (suspeita, probabilidade de ser o Valete, nível de alianças), as regras de inferência para cálculo de risco (`Danger_Trust` e `Danger_Lie`) e a classe `Bot` que modela o comportamento dos NPCs.
* **`FuzzySys.py`**: Interface interativa em linha de comando que executa a simulação do jogo *Prisão Solitária*, permitindo observar métricas fuzzy dos oponentes e tomar decisões estratégicas.
* **`Proto_Sys21.py`**: Protótipo experimental independente aplicando conjuntos fuzzy para gestão de apostas no jogo **21 (Blackjack)** com base na soma das cartas e na presença de Ás.

---

## Sistema Principal: Prisão Solitária (Valete de Copas)

Inspirado no jogo *Prisão Solitária* (*Alice in Borderland*), cada jogador possui um naipe exibido nas costas de seu colar, invisível para si mesmo, e depende da interação com outros participantes para descobrir seu símbolo antes do fim da rodada.

### Variáveis Linguísticas e Conjuntos Fuzzy
1. **Suspeita (`Suspicious`, `Uncertain`, `Not_Suspicious`)**: Avalia o grau de desconfiança de um jogador com base em seu *karma negativo* (escala discreta de `0` a `5`, incrementada sempre que uma mentira é descoberta).
2. **Probabilidade de ser o Valete (`Very_unlikely` a `Very_likely`)**: Mede o risco estatístico e difuso conforme o número de jogadores restantes (`n`, de `2` a `19`).
3. **Nível de Alianças (`Few`, `Some`, `Many`)**: Calcula a proporção entre o número de aliados (`a`) e o total de participantes (`n`).

### Regras de Decisão do Bot (`Ippei`)
* **`Danger_Trust` (Risco de Confiar)**: Combina a suspeita sobre o jogador, a probabilidade de haver um impostor e o karma positivo para definir se o bot valida a informação recebida ou conta com o suporte de seus aliados.
* **`Danger_Lie` (Risco de Mentir)**: Avalia o total de jogadores e a rede de alianças do alvo para decidir se é seguro blefar ou se o risco de retaliação exige dizer a verdade.

---

## Como Executar

Certifique-se de ter o **Python 3** instalado (nenhuma biblioteca externa é necessária, apenas o módulo nativo `random`).

1. Clone o repositório:
   ```bash
   git clone https://github.com/Gabi444444/logica_fuzzy.git
   cd logica_fuzzy
   ```
2. Execute a simulação principal:
   ```bash
   python FuzzySys.py
   ```
3. *(Opcional)* Para rodar os testes do protótipo de Blackjack:
   ```bash
   python Proto_Sys21.py
   ```

---

## Integrantes
* **Flávia** — Organização, padronização e documentação
* **Gabi** — Modelagem fuzzy, arquitetura do `Bot` e sistema principal
* **Ana** — Revisão matemática, validação de entradas e testes