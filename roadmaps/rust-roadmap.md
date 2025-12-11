# 🦀 Rust Roadmap

> Guia de aprendizado do Rust, do básico ao avançado, com foco em projetos práticos e boas práticas.

---

## 🎯 Objetivo

Este roadmap é destinado a desenvolvedores que já têm experiência em outras linguagens (C#, C++, Python) e querem:
- Aprender Rust moderno e seguro
- Criar aplicações de backend, CLI e embarcadas
- Aplicar boas práticas e padrões idiomáticos

---

## 📚 Estrutura de Estudo

### 1️⃣ Fundamentos (1–2 semanas)
- Conceitos essenciais:
  - Ownership e Borrowing
  - Lifetimes
  - Tipos básicos e structs
  - Enums e pattern matching
  - Result / Option / Error handling
- Prática:
  - Mini programas CLI (ex.: conversor de unidades, parser de arquivos)
  - Pequenos algoritmos para fixar ownership e borrowing

---

### 2️⃣ Projetos Práticos Iniciais (2–4 semanas)
- CLI Tool com parsing de argumentos (`clap`)
- Script para manipulação de arquivos CSV ou JSON (`serde`)
- Primeiro mini-projeto em Embedded (opcional)
- Prática com crates comuns:
  - `anyhow`, `thiserror` (erros)
  - `reqwest` ou `hyper` (HTTP)
  - `tokio` (async runtime)

---

### 3️⃣ Back-end e APIs (3–5 semanas)
- Criar um servidor HTTP com **Actix** ou **Axum**
- Rotas REST simples, manipulação de JSON
- Conectar a banco de dados (SQLite ou PostgreSQL)
- Middleware de logging e autenticação simples
- Testes unitários e integração

---

### 4️⃣ Sistemas Embarcados (opcional, 3–6 semanas)
- Entender o uso do Rust em microcontroladores
- Bibliotecas e crates:
  - `ravedude`, `avr-hal` (para Arduino / AVR)
  - `esp-idf-hal` (para ESP32)
- Criar um projeto simples, como leitura de sensor e envio de dados via serial

---

### 5️⃣ Projetos Avançados e Integração (1–2 meses)
- CLI Tools complexas com múltiplas funcionalidades
- Integração com Python via FFI (opcional)
- Contribuição para crates open source
- Documentação completa com exemplos, README e comentários

---

## 🧰 Boas práticas e padrões
- Modularização de código e organização de crates
- Naming conventions idiomáticas
- Uso correto de `Result` e `Option`
- Testes unitários (`cargo test`) e integração
- Documentação com `rustdoc`

---

## 📈 Resultado Esperado
Ao final do roadmap:
- Conhecimento sólido em Rust moderno
- Projetos práticos para portfólio
- Capacidade de aplicar Rust em backend, CLI e embarcados
- Código limpo, modular e bem documentado

---

## 🔗 Recursos sugeridos
- [The Rust Programming Language (Book)](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Rustlings — Exercícios práticos](https://github.com/rust-lang/rustlings)
- [Rust Embedded Book](https://docs.rust-embedded.org/book/)
- [Crates.io — pacotes Rust](https://crates.io/)
