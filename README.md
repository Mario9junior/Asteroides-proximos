<p align="center">
  <img  src="img/asteroids_in_orbit.gif" alt="Descrição da imagem para acessibilidade"  width="800"/>
</p> 

 <h1 align="center"> 🚀 Asteroides proximos ao planeta terra </h1>

> 🌌 Explore dados reais sobre asteroides e objetos próximos da Terra em tempo real.

---

## 🧠 Sobre o Projeto

Objetos próximos da Terra são asteroides e cometas cujas órbitas os trazem para a vizinhança do planeta. O monitoramento desses corpos é essencial para avaliar riscos de impacto e compreender a dinâmica do Sistema Solar.

O NEO WS foi criado como parte das iniciativas abertas da NASA para democratizar o acesso a dados espaciais, permitindo que pesquisadores, desenvolvedores e instituições integrem essas informações em aplicações científicas e educacionais.

Esses dados incluem:
- ☄️ Asteroides
- 🌍 Aproximações da Terra
- ⚠️ Objetos potencialmente perigosos

Ideal para:
- 👨‍🔬 Pesquisa científica  
- 📊 Análise de dados  
- 💻 Desenvolvimento de aplicações  
- 🎓 Projetos educacionais  
---

## 1. 🛰️ Introdução

temos como objetivo analisar quantitativamente e qualitativamente a relação entre duas variáveis fundamentais no monitoramento de objetos próximos à Terra (NEOs – *Near Earth Objects*):

- **Número total de asteroides detectados**
- **Número de asteroides classificados como potencialmente perigosos (PHA – Potentially Hazardous Asteroids)**

Os dados utilizados são inspirados no sistema oficial da NASA para monitoramento de objetos próximos da Terra, com foco em análise estatística, interpretação de risco e implicações para defesa planetária.

<p align="center">
  <img  src="img/figure_1.png" alt="Descrição da imagem para acessibilidade"  width="800"/>
</p> 
A análise evidencia que:

- Apenas uma **fração minoritária (~7%)** dos asteroides apresenta potencial de risco
- A distribuição é fortemente assimétrica, indicando predominância de objetos não perigosos

### 6.2 Implicações Científicas

- O baixo percentual de PHAs sugere que o sistema solar interno é relativamente estável
- No entanto, o risco não pode ser negligenciado devido ao potencial destrutivo desses objetos

### 6.3 Monitoramento e Modelagem Orbital

Asteroides classificados como PHA são submetidos a:

- Modelagem orbital de alta precisão
- Simulações de impacto
- Atualizações constantes com base em observações telescópicas e radar

---

## 7. ⚠️ Avaliação de Risco

### 7.1 Parâmetros Críticos

Os fatores determinantes para risco de colisão incluem:

- Velocidade relativa
- Ângulo de aproximação
- Massa estimada
- Incerteza orbital

### 7.2 Escalas de Classificação

A NASA utiliza escalas como:

- **Escala de Torino** (0 a 10)
- **Escala de Palermo** (logarítmica)

Atualmente, a maioria dos PHAs possui classificação **0 ou próximo de 0**, indicando risco insignificante a curto prazo.

## ✨ Funcionalidades de resultado estudado

- 📅 Consultar asteroides por data  
---
```json
  "near_earth_objects": {
    "2026-04-25": [
      {
        "name": "Asteroid 2026 AB",
        "is_potentially_hazardous_asteroid": false,
        "estimated_diameter": {
          "meters": {
            "estimated_diameter_min": 120,
            "estimated_diameter_max": 300
          }
        }
      }
    ]
  }
}
```

 

