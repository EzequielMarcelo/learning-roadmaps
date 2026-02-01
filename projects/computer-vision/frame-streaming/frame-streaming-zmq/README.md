# Frame Streaming com ZeroMQ (Producer / Consumer)

Este módulo implementa um **pipeline de frame streaming** utilizando **ZeroMQ (ZMQ) sobre TCP**,
no padrão **Producer / Consumer**, com foco em **baixa latência**, simplicidade arquitetural
e possibilidade de escalabilidade para múltiplos consumidores.

---

## 🎯 Objetivo

Transmitir frames de vídeo entre processos utilizando ZeroMQ e medir a **latência ponta-a-ponta**
entre captura e consumo do frame.

Este experimento é utilizado para comparação com outras abordagens de IPC, como **Shared Memory**.

---

## 🧱 Arquitetura

- **Producer**
  - Captura frames via OpenCV
  - Serializa o frame (JPEG / bytes)
  - Envia timestamp de envio (`t0`) + frame
- **Consumer**
  - Recebe frame e timestamp
  - Decodifica o frame
  - Mede latência (`t1 - t0`)

---

## ▶️ Como Rodar

### 1️⃣ Criar ambiente virtual (recomendado)

```sh
python -m venv .venv
source .venv/bin/activate # Linux / Mac
.venv\Scripts\activate # Windows
```

### 2️⃣ Instalar dependências

```sh
pip install -r requirements.txt
```

### 3️⃣ Iniciar o Producer

Em um terminal:

```sh

python producer\src\main.py
```

O producer irá:

- Abrir a webcam

- Começar a enviar frames via ZMQ

### 4️⃣ Iniciar o Consumer

Em outro terminal:

```sh
python consumer\src\main.py
```

O consumer irá:

- Conectar ao socket ZMQ

- Exibir os frames

- Mostrar a latência calculada

## ⚠️ Observações Importantes

O Consumer deve iniciar após o Producer

Sockets PUB/SUB não fazem buffering para subscribers atrasados

O endereço padrão é `tcp://127.0.0.1:5555` pode ser alterado no arquivo `settings.py`

> Este módulo foi projetado para localhost, mas pode ser usado em rede

## 📊 Considerações de Performance

Há overhead de:

- Compressão JPEG

- Serialização de dados

- Stack TCP

- A latência é maior que em abordagens com Shared Memory

## 🧠 Conclusão

ZeroMQ é uma excelente opção para frame streaming distribuído,
quando simplicidade e escalabilidade são mais importantes que a latência mínima absoluta.
Este módulo serve como base para sistemas de visão computacional em tempo real.

## 🔧 Tecnologias

- Python 3.x
- OpenCV
- ZeroMQ (PyZMQ)
- NumPy
