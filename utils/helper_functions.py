import pygame

def blit_rotate_center(surface, image, top_left, angle):
    """Rotate an image and blit it to the given surface at the specified angle around its center."""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    surface.blit(rotated_image, new_rect.topleft)

def scale_image(image, width, height):
    """Scale an image to the given dimensions."""
    return pygame.transform.scale(image, (width, height))
