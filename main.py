import sys
import pygame

pygame.init()

# Configurações da janela
LARGURA, ALTURA = 900, 620
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("CineKnowledge - Parte 2")

# Paleta de cores
FUNDO_ESCURO = (24, 28, 36)
BRANCO = (245, 245, 245)
DOURADO = (244, 180, 26)
VERMELHO_CINE = (214, 48, 49)
VERDE_ACERTO = (0, 184, 148)
BOTAO_PADRAO = (45, 52, 64)
BOTAO_HOVER = (72, 84, 96)

# Fontes
FONTE_TITULO = pygame.font.SysFont("arial", 46, bold=True)
FONTE_SUBTITULO = pygame.font.SysFont("arial", 22)
FONTE_HUD = pygame.font.SysFont("arial", 22, bold=True)
FONTE_PERGUNTA = pygame.font.SysFont("arial", 25, bold=True)
FONTE_BOTAO = pygame.font.SysFont("arial", 20)


def criar_banco_perguntas():
  """Retorna uma lista de dicionários com perguntas sobre cinema."""
  return [
      {
          "pergunta": (
              "Quem dirigiu 'Pulp Fiction: Tempo de Violência' (1994)?"
          ),
          "alternativas": [
              "A) Quentin Tarantino",
              "B) Martin Scorsese",
              "C) David Fincher",
              "D) Ridley Scott",
          ],
          "correta": 0,
      },
      {
          "pergunta": (
              "Qual filme venceu o Oscar de Melhor Filme em 2020 (cerimônia de"
              " 2020)?"
          ),
          "alternativas": [
              "A) 1917",
              "B) Coringa",
              "C) Parasita",
              "D) Era Uma Vez em... Hollywood",
          ],
          "correta": 2,
      },
      {
          "pergunta": "Em 'Matrix' (1999), qual pílula Neo escolhe tomar?",
          "alternativas": [
              "A) Azul",
              "B) Vermelha",
              "C) Verde",
              "D) Dourada",
          ],
          "correta": 1,
      },
      {
          "pergunta": (
              "Qual compositor criou a trilha sonora icônica de 'Tubarão' e"
              " 'Star Wars'?"
          ),
          "alternativas": [
              "A) Hans Zimmer",
              "B) Ennio Morricone",
              "C) John Williams",
              "D) Howard Shore",
          ],
          "correta": 2,
      },
      {
          "pergunta": (
              "Qual estúdio de animação lançou 'Toy Story' (1995), o primeiro"
              " longa totalmente em CGI?"
          ),
          "alternativas": [
              "A) DreamWorks",
              "B) Pixar",
              "C) Studio Ghibli",
              "D) Illumination",
          ],
          "correta": 1,
      },
  ]


def desenhar_botao(texto, x, y, largura, altura, clique_liberado):
  """Desenha um botão e retorna True se clicado neste quadro."""
  mouse_pos = pygame.mouse.get_pos()
  retangulo = pygame.Rect(x, y, largura, altura)

  sobre_botao = retangulo.collidepoint(mouse_pos)
  cor_fundo = BOTAO_HOVER if sobre_botao else BOTAO_PADRAO

  pygame.draw.rect(TELA, cor_fundo, retangulo, border_radius=8)
  pygame.draw.rect(
      TELA, DOURADO if sobre_botao else BRANCO, retangulo, 2, border_radius=8
  )

  texto_surf = FONTE_BOTAO.render(texto, True, BRANCO)
  texto_rect = texto_surf.get_rect(center=retangulo.center)
  TELA.blit(texto_surf, texto_rect)

  return sobre_botao and clique_liberado


def desenhar_menu(clique_liberado):
  """Renderiza a tela inicial do CineKnowledge."""
  titulo = FONTE_TITULO.render("CineKnowledge", True, DOURADO)
  subtitulo = FONTE_SUBTITULO.render(
      "Quiz de Cinema • Versão de Acompanhamento (Parte 2)", True, BRANCO
  )
  instrucao = FONTE_SUBTITULO.render(
      "Clique com o mouse nas alternativas • ESC para sair", True, (180, 190, 200)
  )

  TELA.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 160)))
  TELA.blit(subtitulo, subtitulo.get_rect(center=(LARGURA // 2, 225)))
  TELA.blit(instrucao, instrucao.get_rect(center=(LARGURA // 2, 275)))

  return desenhar_botao(
      "COMEÇAR PARTIDA", LARGURA // 2 - 130, 350, 260, 55, clique_liberado
  )


def desenhar_jogo(
    pergunta_atual, indice, total, pontuacao, vidas, clique_liberado
):
  """Renderiza o HUD, a pergunta atual e os 4 botões de resposta."""
  hud = FONTE_HUD.render(
      f"Questão {indice + 1}/{total}   |   Pontos: {pontuacao}   |   Vidas:"
      f" {vidas}",
      True,
      DOURADO,
  )
  TELA.blit(hud, (40, 35))

  enunciado = FONTE_PERGUNTA.render(pergunta_atual["pergunta"], True, BRANCO)
  TELA.blit(enunciado, (40, 105))

  escolha = None
  y_inicial = 190
  for idx, alternativa in enumerate(pergunta_atual["alternativas"]):
    y_pos = y_inicial + idx * 85
    if desenhar_botao(alternativa, 40, y_pos, 820, 62, clique_liberado):
      escolha = idx

  return escolha


def desenhar_encerramento(pontuacao, vidas, clique_liberado):
  """Renderiza a tela final de vitória ou derrota."""
  venceu = vidas > 0
  titulo_texto = (
      "PARABÉNS! QUIZ CONCLUÍDO" if venceu else "GAME OVER - SEM VIDAS"
  )
  cor_titulo = VERDE_ACERTO if venceu else VERMELHO_CINE

  titulo = FONTE_TITULO.render(titulo_texto, True, cor_titulo)
  resumo = FONTE_HUD.render(
      f"Pontuação final: {pontuacao} pontos", True, BRANCO
  )

  TELA.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 180)))
  TELA.blit(resumo, resumo.get_rect(center=(LARGURA // 2, 260)))

  reiniciar = desenhar_botao(
      "JOGAR NOVAMENTE", LARGURA // 2 - 130, 350, 260, 55, clique_liberado
  )
  return reiniciar


def main():
  """Loop principal do jogo."""
  relogio = pygame.time.Clock()
  banco = criar_banco_perguntas()

  estado = "menu"
  pontuacao = 0
  vidas = 3
  indice_pergunta = 0

  while True:
    clique_liberado = False

    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
      if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        clique_liberado = True

    TELA.fill(FUNDO_ESCURO)

    if estado == "menu":
      if desenhar_menu(clique_liberado):
        pontuacao = 0
        vidas = 3
        indice_pergunta = 0
        estado = "jogando"

    elif estado == "jogando":
      pergunta_atual = banco[indice_pergunta]
      resposta = desenhar_jogo(
          pergunta_atual,
          indice_pergunta,
          len(banco),
          pontuacao,
          vidas,
          clique_liberado,
      )

      if resposta is not None:
        if resposta == pergunta_atual["correta"]:
          pontuacao += 10
        else:
          vidas -= 1

        indice_pergunta += 1
        if vidas <= 0 or indice_pergunta >= len(banco):
          estado = "encerramento"

    elif estado == "encerramento":
      if desenhar_encerramento(pontuacao, vidas, clique_liberado):
        pontuacao = 0
        vidas = 3
        indice_pergunta = 0
        estado = "jogando"

    pygame.display.flip()
    relogio.tick(60)


if __name__ == "__main__":
  main()