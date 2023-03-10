import pygame 
from settings import *
from tile import Tile 
from player import Player
from debug import debug
class Level:
    def __init__(self):
        
        #get the display surface 
        self.display_surface = pygame.display.get_surface()
       
        #Sprite group
        self.visable_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #Sprite setup 
        self.create_map() 

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                  Tile((x,y),[self.visable_sprites, self.obstacle_sprites])
                if col =='p':
                    self.player= Player((x,y),[self.visable_sprites],self.obstacle_sprites)

            

    def run(self):
        #update and draw the game
        self.visable_sprites.custom_draw(self.player)
        self.visable_sprites.update()
        

        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] //2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2(100,200)

        self.floor_surf = pygame.image.load('ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0)) 

    def custom_draw(self,player):

        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
 
       # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)