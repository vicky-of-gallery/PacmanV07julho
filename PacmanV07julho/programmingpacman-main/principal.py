import pygame 
import Constantes
import sprites 

class game: 
    def __init__(self):
        #criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((Constantes.LARGURA, Constantes.ALTURA))
        pygame.display.set_caption(Constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock ()
        self.esta_rodando = True

    def novo_jogo(self):
        #instancia as classes das sprintes do jogo 
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo 
        self.jogando = True
        while self.jogando:
            self.relogio.tick(Constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False 
  
    def atualizar_sprites(self):
        #atualizar sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        #desenhar sprites
        self.tela.fill(Constantes.PRETO) #limpando a tela 
        self.todas_as_sprites.draw(self.tela) # desenhando as sprites 
        pygame.display.flip()

    def mostrar_tela_start(self):
            pass
    
    def mostrar_tela_game_over(self):
            pass 
    
g = game ()
g.mostrar_tela_start()

while g.esta_rodando:
     g.novo_jogo()
     g.mostrar_tela_game_over()
