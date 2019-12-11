import pygame
import pytmx

from pytmx.util_pygame import load_pygame

# Initiation de pygame

pygame.init()




# class LoadMap:
#
#     def __init__(self, mymap):
#         self.tmxdata = pytmx.TiledMap(mymap)
#         self.gameMap = load_pygame(mymap)
#
#     def update(self):
#         for layer in gameMap.visible_layers:
#             if isinstance(layer, pytmx.TiledTileLayer):
#                 for x, y, gid in layer:
#                     tile = gameMap.get_tile_image_by_gid(gid)
#                     if tile:
#                         window.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))


class Tuile(pygame.sprite.Sprite):
	def __init__(self,x,y,gid):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(x*16,y*16,16,16)
		self.gid = gid

class BlockTest(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
       pygame.sprite.Sprite.__init__(self)
       IMAGE = pygame.image.load('sprite/bite.png').convert_alpha()

       self.image = pygame.Surface([width, height])
       self.image=IMAGE
       self.rect = self.image.get_rect()
       self.speed=8;

       self.movement_dict = {'left': (-self.speed,0),
                             'right': (self.speed,0),
                             'down': (0,self.speed),
                             'up': (0,-self.speed),
                             'left-up': (-self.speed,-self.speed),
                             'right-up': (self.speed,-self.speed),
                             'left-down': (-self.speed,self.speed),
                             'right-down': (self.speed,self.speed),
                             'rest': (0,0)}
       self.movement = 'rest'
       self.rect.x=64
       self.rect.y=64

    def update(self, event, obstacle):

        keys = pygame.key.get_pressed()

        if event != None:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif (keys[pygame.K_UP] and keys[pygame.K_LEFT]):
                    self.movement = 'left-up'
                    print(self.movement)
                elif (keys[pygame.K_UP] and keys[pygame.K_RIGHT]):
                    self.movement = 'right-up'
                    print(self.movement)
                elif (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]):
                    self.movement = 'left-down'
                    print(self.movement)
                elif (keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]):
                    self.movement = 'right-down'
                    print(self.movement)
                elif event.key == pygame.K_LEFT:
                    self.movement = 'left'
                    print(self.movement)
                elif event.key == pygame.K_RIGHT:
                    self.movement = 'right'
                    print(self.movement)
                elif event.key == pygame.K_DOWN:
                    self.movement = 'down'
                    print(self.movement)
                elif event.key == pygame.K_UP:
                    self.movement = 'up'
                    print(self.movement)
            elif event.type == pygame.KEYUP:
                self.movement = 'rest'

            self.rect.x += self.movement_dict[self.movement][0]
            self.rect.y += self.movement_dict[self.movement][1]


        if pygame.sprite.spritecollideany(self,obstacle) is not None:
            self.rect.x -= self.movement_dict[self.movement][0]
            self.rect.y -= self.movement_dict[self.movement][1]


    def draw(self, display):
        if (self.rect.x<400):
            display.blit(self.image, self.rect)
        else:
            display.blit(self.image, [400, self.rect.y])


class Display:

    def __init__(self):

        self.displayRunning = True
        self.displayWindow = pygame.display.set_mode((800, 400))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Super Mario")
        red = pygame.Color(153,0,0)
        self.block = BlockTest(red, 16, 16)

    def load_newmap(self,mymap):
        self.tmxdata = pytmx.TiledMap(mymap)
        self.gameMap = load_pygame(mymap, pixelalpha=True)
        self.obstacles = pygame.sprite.Group()

        layer2 = self.gameMap.get_layer_by_name("collision")

        for x, y, gid in layer2:
            a=True
            if (gid!=0):
                self.obstacles.add(Tuile(x,y,gid))

    def updateRender(self):
        while self.displayRunning:
            for event in pygame.event.get():
                pass

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.displayRunning = False
                    pygame.display.update()

            # Si event detecter update du block
            self.block.update(event, self.obstacles)

            # rendu de la maps
            for layer in self.gameMap.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid in layer:
                        tile = self.gameMap.get_tile_image_by_gid(gid)
                        if tile:

                            # Gestion scrolling ici
                            if (self.block.rect.x>400):
                                self.displayWindow.blit(tile, (x * self.gameMap.tilewidth-self.block.rect.x+400, y * self.gameMap.tileheight))
                            else:
                                self.displayWindow.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))


            # rendu block
            self.block.draw(self.displayWindow)

            self.clock.tick(150)





#block = Block(red, 16, 16)

go=Display()
go.load_newmap("map/mapp.tmx")
go.updateRender()



pygame.quit()
