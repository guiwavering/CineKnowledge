# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

**Nome:**

> CineKnowledge

## 2. Integrantes do grupo

- Nome: Guilherme Henrique Ribeiro Silva

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Conhecimentos Cinematográficos (Filmes, Diretores, Premiações e Cultura Pop).

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> O tema cinematográfico fundamenta a lógica central do jogo, estruturando o banco de perguntas e desafios intelectuais. O objetivo do jogador é demonstrar repertório sobre a sétima arte para superar as rodadas, respondendo corretamente a enunciados sobre obras e diretores para acumular pontos e manter suas vidas.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Perguntas e respostas (Quiz Arcade).

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> O jogo apresenta uma interface gráfica em 2D inspirada em fliperamas retrô. Na tela, são exibidos o painel de status (pontuação e vidas), o enunciado da pergunta de cinema e quatro botões de alternativas de múltipla escolha. O jogador utiliza o mouse para interagir e selecionar as respostas corretas, enfrentando o desafio de acumular pontos antes de esgotar suas vidas.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Responder corretamente ao maior número possível de perguntas sobre cinema para acumular pontos e concluir com sucesso o quiz sem perder todas as vidas.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: O jogador inicia a partida com um total de 3 vidas.
- Regra 2: Cada resposta correta selecionada soma 10 pontos ao placar.
- Regra 3: Cada resposta incorreta reduz o número de vidas em uma unidade.
- Regra 4: O jogo avança automaticamente para a próxima pergunta após o clique em uma alternativa.
- Regra 5: A partida é encerrada imediatamente caso o contador de vidas chegue a zero ou todas as perguntas do banco sejam respondidas.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> Responder com sucesso a todas as perguntas estruturadas no banco de dados do jogo, mantendo ao menos uma vida restante ao final do percurso.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> Ocorre quando o jogador esgota todas as suas vidas (`vidas == 0`) devido a erros nas alternativas, acionando a tela de fim de jogo (*Game Over*).

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** Sistema de menus e botões interativos de múltipla escolha.
- **Obstáculos ou desafios:** Alternativas falsas (distratores) criadas para testar o conhecimento cinematográfico.
- **Itens ou objetos de interação (se houver):** Botões gráficos clicáveis na tela correspondentes às opções A, B, C e D.
- **Pontuação, vidas, tempo ou progresso:** Painel de status (HUD) atualizado em tempo real exibindo a pontuação acumulada e as vidas restantes.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> O jogador utilizará o mouse para navegar pelo menu e clicar diretamente nos botões de alternativa de resposta, além da tecla `ESC` para sair da aplicação.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Gerenciamento do estado das telas e transições no loop principal do Pygame.
- Dificuldade 2: Posicionamento e renderização correta de textos e enunciados dinâmicos na tela.
- Dificuldade 3: Sincronização do fluxo de cliques do mouse (`debounce`) para evitar múltiplos registros acidentais.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> Uma aplicação funcional em Pygame contendo tela de menu, um loop de jogo com um banco fixo de perguntas de cinema estruturado em dicionários e listas em Python, sistema básico de pontuação, contagem de 3 vidas e uma tela de fim de jogo (*Game Over*).

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Adição de efeitos sonoros e trilha sonora imersiva com o `pygame.mixer`.
- Melhoria 2: Implementação de um cronômetro regressivo (temporizador) para cada questão.
- Melhoria 3: Carregamento dinâmico das perguntas a partir de um arquivo externo (`.json`).