# Prompt Engineering — Systematic Prompt Evaluation

> **Portfolio project · Prompt Engineering · Generative AI · Evaluation**

Projeto de Engenharia de Prompt que demonstra **um processo técnico e reproduzível**, indo além de uma coleção de prompts.

O projeto organiza experimentos de **hipótese → prompt → execução → avaliação → comparação → melhoria**, com foco em qualidade, consistência, formato de saída, grounding e análise de falhas.

## 🎯 Objetivo

Investigar como diferentes estratégias de prompting alteram o comportamento de um modelo e documentar os resultados de forma reproduzível.

O projeto trata prompts como **artefatos de engenharia versionáveis**, conectando cada alteração a uma hipótese e a critérios de avaliação.

## 🔬 O que já está implementado

- casos de experimento versionados em JSON;
- baseline vs. prompt estruturado;
- avaliador determinístico de sinais de qualidade estrutural;
- pesos explícitos por critério;
- testes automatizados de reprodutibilidade;
- geração de artefato JSON;
- GitHub Actions para testes e geração da avaliação.

> **Importante:** o avaliador atual é uma heurística estrutural. Ele **não mede qualidade semântica de uma resposta de LLM** e não deve ser apresentado como benchmark de modelo.

## 🧪 Método experimental

Cada experimento segue:

**Problema → baseline → hipótese → prompt → execução → avaliação → análise → iteração**

Os experimentos registram:

1. problema;
2. hipótese;
3. prompt utilizado;
4. casos de teste;
5. contexto disponível;
6. critérios de avaliação;
7. resultado observado;
8. falhas e limitações;
9. próxima iteração.

## 📊 Critérios atuais

| Critério | Peso |
|---|---:|
| Clareza da tarefa | 25% |
| Contexto | 20% |
| Restrições | 20% |
| Formato de saída | 20% |
| Exemplos | 15% |

A próxima camada de avaliação deve adicionar métricas de **aderência, relevância, precisão, completude, consistência, grounding e robustez** sobre respostas efetivamente geradas.

## 🏗️ Arquitetura

```text
Casos de teste
     │
     ▼
Baseline / Prompt estruturado
     │
     ▼
Avaliador determinístico
     │
     ├── Clareza
     ├── Contexto
     ├── Restrições
     ├── Formato
     └── Exemplos
     │
     ▼
Resultado versionado
     │
     ▼
Testes + CI
```

## 📁 Estrutura

```text
prompt-engineering-lab/
├── README.md
├── src/
│   └── evaluate.py
├── experiments/
│   └── cases.json
├── output/
│   ├── evaluation.json
│   └── README.md
├── tests/
│   └── test_evaluate.py
├── .github/workflows/
│   └── ci.yml
└── requirements.txt
```

## ▶️ Como executar

```bash
pip install -r requirements.txt
python -m pytest -q
python -m src.evaluate
```

## 🧠 Decisões de engenharia

### Prompt como artefato versionável

Prompts relevantes devem ser versionados para permitir comparação entre alterações e resultados.

### Geração ≠ avaliação

Uma resposta gerada não é automaticamente uma resposta de qualidade. O fluxo separa:

**geração → validação → avaliação**.

### Reprodutibilidade antes de benchmark

A implementação atual evita dependência de uma API externa. Isso permite testar o pipeline de avaliação de forma determinística antes de adicionar modelos reais.

## 🔐 Limitações atuais

- não há chamada a LLM externa;
- não há medição de qualidade semântica;
- a heurística depende de sinais textuais explícitos;
- não compara modelos;
- os resultados estruturais não representam qualidade final da resposta.

## 🚀 Roadmap

- [x] casos de teste versionados;
- [x] avaliação estrutural determinística;
- [x] testes automatizados;
- [x] CI;
- [ ] versionar prompts por estratégia;
- [ ] integrar um modelo real;
- [ ] criar dataset fixo de avaliação;
- [ ] avaliar respostas com métricas semânticas;
- [ ] adicionar avaliação por LLM-as-judge com protocolo documentado;
- [ ] testes de regressão de prompts;
- [ ] comparar modelos e custos/latência.

## 🛠️ Tecnologias

**Python · Prompt Engineering · Generative AI · LLM Evaluation · JSON · Pytest · GitHub Actions**

## 💼 Competências demonstradas

**Prompt Engineering · Experiment Design · Evaluation · Reproducibility · Automated Testing · Technical Documentation · Generative AI**

## 🔗 Portfólio

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)

## 📌 Status

**Fundação implementada e preparada para a próxima etapa de avaliação com modelo real.**

---

**Tainã Sichero Dulcetti · AI & Data Developer | AI Specialist | Generative AI & Machine Learning**
