# React Roadmap

> Guia de aprendizado React, do básico ao avançado, com foco em projetos práticos e boas práticas.

---

# 🟦 **Nível 0 — Nivelamento e Setup**

## 🎯 Objetivo: Entender o que é React e preparar o ambiente

Baseado no curso introdutório do Mosh.

Conteúdos deste nível:

- O que é React e por que usar
- SPA vs MPA
- Conceito de Componentes
- JSX
- Props
- Estado básico
- Eventos
- Introdução ao React moderno
- Setup com Vite
- Uso de TypeScript no React
- Estrutura inicial de projeto
- Uso de **Bootstrap** no React
  - Instalação via npm
  - Importação de CSS
  - Uso de classes utilitárias
  - Componentes básicos (buttons, alerts, cards)

Ferramentas:

- Node.js
- npm / pnpm
- Vite
- React
- TypeScript
- Mini-exercícios sugeridos (sem projeto formal):
- Componente HelloWorld
- Componente Button com props
- Contador simples
- Renderização condicional básica
- O que dominar antes de avançar:
- Criar projeto com Vite
- Entender JSX
- Criar e usar componentes
- Passar props
- Estado simples com useState
- Estrutura básica de pastas

---

# 🟩 **Nível 1 — Fundamentos (Iniciante)**

## 🎯 Objetivo: Entender como React funciona

Projetos deste nível:

- **Projeto 1: TaskList**

  - Conceitos aprendidos:

    - Componentes
    - Props
    - Estado (useState)
    - Ciclo de vida (useEffect)
    - Renderização de listas
    - Fetch em API fake

### ✔ O que dominar antes de avançar

- JSX
- Componentização
- Estados locais
- useEffect
- Eventos

---

# 🟨 **Nível 2 — Estrutura e Navegação (Intermediário)**

## 🎯 Objetivo: Criar aplicações estruturadas com múltiplas páginas

Projetos sugeridos:

### **Projeto 2: Mini Portfolio com Rotas**

- Usar **react-router-dom**
- Páginas:

  - Home
  - Sobre
  - Contato

- Navbar fixa

### **Projeto 3: ToDo Pro (evolução do TaskList)**

- Adicionar rotas:

  - /tarefas
  - /tarefas/:id

- Salvar tarefas no localStorage
- Criar componentes reutilizáveis (Button, Input)

### Conceitos aprendidos:

- Rotas
- Navegação
- Organização de pastas
- Componentes reutilizáveis
- Persistência simples

---

# 🟧 **Nível 3 — Estado Global e Boas Práticas (Intermediário+)**

## 🎯 Objetivo: Preparar para apps complexos

Projetos sugeridos:

### **Projeto 4: App de Notas com Context API**

- Criar contexto global
- UseReducer para lógica
- CRUD completo

### **Projeto 5: Dashboard de Estatísticas**

- Cálculos simples
- Cards com valores
- Barra lateral
- Tema claro/escuro

### Conceitos aprendidos:

- Estado global (Context + Reducer)
- Hooks customizados
- Patterns de organização
- Dark mode

---

# 🟥 **Nível 4 — Integração com Backend e Dados Reais (Avançado)**

## 🎯 Objetivo: Integrar React com Python usando FastAPI

Projetos sugeridos:

### **Projeto 6: Frontend consumindo FastAPI**

- Criar uma API em Python com:

  - /status
  - /previsao
  - /dados

- React consome essas rotas
- Loading states e tratamento de erro

### **Projeto 7: Login + Autenticação JWT**

- Formulário de login
- FastAPI retorna token
- React armazena token
- Rotas protegidas com Context

### Conceitos aprendidos:

- Axios
- Autenticação
- Estados assíncronos
- Loading e erros reais

---

# 🟦 **Nível 5 — Gráficos e Componentes para Mercado Financeiro**

## 🎯 Objetivo: Explorar UI usada em plataformas financeiras

Projetos sugeridos:

### **Projeto 8: Dashboard com Gráficos**

- Usar **Recharts** ou **ApexCharts**
- Gráfico de linha
- Gráfico de volume
- Atualização via polling (1s)

### **Projeto 9: Dashboard Real-time com WebSockets**

- Backend envia dados em tempo real
- React atualiza automaticamente
- Candlestick + indicadores simples

### Conceitos aprendidos:

- WebSockets
- Gráficos de alto desempenho
- Hooks avançados
- Otimização de renderização

---

# 🟪 **Nível 6 — Arquitetura Profissional**

## 🎯 Objetivo: Criar aplicações avançadas e escaláveis

Projetos sugeridos:

### **Projeto 10: Dashboard Completo**

Componentes:

- Card de métricas
- Painéis dinâmicos
- Gráficos avançados
- Logs em tempo real
- Layout responsivo

### Conceitos aprendidos:

- Estrutura de projeto profissional
- Divisão de domínio
- Reutilização de componentes em larga escala
- Layout avançado

---

# 📌 Resumo do Roadmap

1. **Fundamentos — TaskList**
2. **Rotas e estrutura**
3. **Estado global + hooks customizados**
4. **Integração com FastAPI + JWT**
5. **Gráficos, WebSockets, componentes complexos**
6. **Dashboard profissional**
