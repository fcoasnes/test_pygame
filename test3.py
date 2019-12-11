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

       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.speed=8;

       self.movement_dict = {'left': (-self.speed,0), 'right': (self.speed,0), 'down': (0,self.speed), 'up': (0,-self.speed), 'rest': (0,0)}
       self.movement = 'rest'
       self.rect.x=50
       self.rect.y=50

    def update(self, event):
        if event != None:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LEFT:
                    self.movement = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.movement = 'right'
                elif event.key == pygame.K_DOWN:
                    self.movement = 'down'
                elif event.key == pygame.K_UP:
                    self.movement = 'up'
            elif event.type == pygame.KEYUP:
                self.movement = 'rest'

        self.rect.x += self.movement_dict[self.movement][0]
        self.rect.y += self.movement_dict[self.movement][1]


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

        layer2 = self.gameMap.get_layer_by_name("colli")

        # for x, y, gid in layer2:
        #     if (gid!=0):
        #         # print(gid)
        #         self.obstacles.add(Tuile(x,y,gid))


    def updateRender(self):
        while self.displayRunning:
            for event in pygame.event.get():
                pass

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.displayRunning = False
                    pygame.display.update()


            self.block.update(event)

            # rendu de la maps
            for layer in self.gameMap.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid in layer:
                        tile = self.gameMap.get_tile_image_by_gid(gid)
                        if tile:
                            if (self.block.rect.x>400):
                                self.displayWindow.blit(tile, (x * self.gameMap.tilewidth-self.block.rect.x+400, y * self.gameMap.tileheight))
                            else:
                                self.displayWindow.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

                        if pygame.sprite.spritecollideany(self.block,self.obstacles):
                            print("lol")
                        # if layer.name == "colli":
                        #     if self.block.rect.x
                        #     if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.block.rect) == True:
                        #         print "YOU HIT THE RED BLOCK!!"
                        #         break


                    # if layer.name == "colli":
                    #     print("lol2")
                    #     for obj in layer:
                    #         if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.block.rect) == True:
                    #             print "YOU HIT THE RED BLOCK!!"
                    #             break

            # rendu block
            self.block.draw(self.displayWindow)

            self.clock.tick(150)





#block = Block(red, 16, 16)

go=Display()
go.load_newmap("map2.tmx")
go.updateRender()
# tmxdata = pytmx.TiledMap("map2.tmx")
# clock = pygame.time.Clock()
#
# # create game display
# window = pygame.display.set_mode((800,tmxdata.height*tmxdata.tileheight))
# red = pygame.Color(153,0,0)
# pygame.display.set_caption("Super Mario")
#
# #tmxdata = pytmx.TiledMap("map2.tmx")
# gameMap = load_pygame("map2.tmx")
#
#
# windowOpen = True
#
# while windowOpen:
#     pygame.display.flip() #Rafraichissement
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             windowOpen = False
#
#     for layer in gameMap.visible_layers:
#         if isinstance(layer, pytmx.TiledTileLayer):
#             for x, y, gid in layer:
#                 tile = gameMap.get_tile_image_by_gid(gid)
#                 if tile:
#                     window.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))


pygame.quit()
