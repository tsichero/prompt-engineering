# Prompt Engineering Lab — Systematic Prompt Evaluation

> **Portfolio project · Prompt Engineering · Generative AI · Evaluation**

Laboratório prático para demonstrar **Engenharia de Prompt como processo técnico**, indo além de uma coleção de prompts.

O projeto organiza experimentos de **hipótese → prompt → execução → avaliação → comparação → melhoria**, com foco em qualidade, consistência, formato de saída, grounding e análise de falhas.

## 🎯 Objetivo

Investigar como diferentes estratégias de prompting alteram o comportamento de um modelo e documentar os resultados de forma reproduzível.

O laboratório trata prompts como **artefatos de engenharia versionáveis**, conectando cada alteração a uma hipótese e a critérios de avaliação.

## 🔬 Estratégias estudadas

- Zero-shot prompting
- Few-shot prompting
- Role prompting
- Contextual prompting
- Structured output
- Prompt chaining
- RAG-oriented prompting
- Grounded generation
- Instruções de restrição
- Guardrails e validação de saída
- Comparação entre versões de prompt
- Análise de casos de falha

## 🧪 Método experimental

Cada experimento segue, sempre que aplicável:

**Problema → baseline → hipótese → prompt → execução → avaliação → análise → iteração**

Os experimentos devem registrar:

1. problema;
2. hipótese;
3. prompt utilizado;
4. casos de teste;
5. contexto disponível;
6. critérios de avaliação;
7. resultado observado;
8. falhas e limitações;
9. próxima iteração.

## 📊 Critérios de avaliação

| Critério | O que é observado |
|---|---|
| Aderência | Cumprimento das instruções |
| Relevância | Relação com o objetivo da tarefa |
| Precisão | Correção em relação às evidências disponíveis |
| Completude | Cobertura do que foi solicitado |
| Consistência | Estabilidade do comportamento |
| Estrutura | Conformidade com o formato esperado |
| Grounding | Fundamentação no contexto fornecido |
| Robustez | Comportamento diante de entradas diferentes |
| Falhas | Respostas inadequadas ou não fundamentadas |

> **Importante:** métricas e resultados só devem ser apresentados como evidência experimental quando tiverem sido realmente executados e registrados.

## 🏗️ Arquitetura conceitual

```text
Entrada
   │
   ▼
Prompt Template
   │
   ├── Instruções
   ├── Contexto
   └── Exemplos
   │
   ▼
LLM / Model
   │
   ▼
Resposta estruturada
   │
   ▼
Validação
   │
   ▼
Avaliação
   ├── Qualidade
   ├── Relevância
   ├── Grounding
   └── Casos de falha
```

## 📁 Estrutura

```text
prompt-engineering-lab/
├── README.md
├── prompts/
│   ├── baseline/
│   ├── few-shot/
│   ├── structured/
│   └── rag/
├── experiments/
├── datasets/
├── evaluations/
├── outputs/
├── tests/
└── requirements.txt
```

A estrutura será expandida conforme os experimentos forem implementados.

## 🧠 Decisões de engenharia

### Prompt como artefato versionável

Prompts relevantes devem ser versionados para permitir comparação entre alterações e resultados.

### Geração ≠ avaliação

Uma resposta gerada não é automaticamente uma resposta de qualidade. Por isso, o fluxo separa:

**geração → validação → avaliação**.

### Casos de falha também são evidências

O laboratório registra comportamentos inadequados para identificar limites, regressões e oportunidades de melhoria.

## 🛠️ Tecnologias

**Python · LLMs · Generative AI · Prompt Engineering · Evaluation · Structured Outputs · RAG · JSON · Automated Testing**

## 🔐 Limitações

Os resultados de prompting podem variar conforme:

- modelo e versão;
- parâmetros de geração;
- dataset;
- contexto;
- idioma;
- critérios de avaliação;
- complexidade da tarefa.

Este projeto não pretende afirmar que uma estratégia é universalmente superior. A proposta é comparar comportamentos sob condições documentadas.

## 🚀 Roadmap

- [ ] adicionar conjunto de casos de teste;
- [ ] versionar prompts;
- [ ] implementar experimentos reproduzíveis;
- [ ] automatizar avaliações;
- [ ] comparar modelos;
- [ ] incluir métricas quantitativas;
- [ ] integrar APIs de LLM;
- [ ] adicionar testes de regressão de prompts;
- [ ] integrar CI.

## 💼 Competências demonstradas

**Prompt Engineering · Generative AI · LLM Applications · Evaluation · Experiment Design · Structured Outputs · RAG Prompting · Python · Testing · Technical Documentation**

## 🔗 Portfólio

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)

## 📌 Status

**Em desenvolvimento.**

Este README documenta a metodologia e a arquitetura do laboratório. Resultados experimentais serão adicionados conforme forem efetivamente implementados e validados.

---

**Tainã Sichero Dulcetti · AI & Data Developer | AI Specialist | Generative AI & Machine Learning**
