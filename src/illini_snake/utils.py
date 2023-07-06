import pygame

def load_logo_file( filepath, width ):
    img = pygame.image.load( filepath )
    r = img.get_rect()
    h = r.height
    w = r.width

    # Scale
    scaling = width/max(h,w)
    return pygame.transform.smoothscale_by( img, scaling )

    

