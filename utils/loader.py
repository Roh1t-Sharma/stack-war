import pygame

class ResourceLoader:
    """Class to load and cache game resources."""
    _cache = {}  # Cache to store loaded resources to avoid reloading

    @staticmethod
    def load_image(path):
        """Load an image from the specified path."""
        image = ResourceLoader._cache.get(path)
        if image is None:
            try:
                image = pygame.image.load(path).convert_alpha()
                ResourceLoader._cache[path] = image
            except pygame.error as e:
                print(f"Error loading image at {path}: {e}")
                return None
        return image

    @staticmethod
    def load_sound(path):
        """Load a sound from the specified path."""
        sound = ResourceLoader._cache.get(path)
        if sound is None:
            try:
                sound = pygame.mixer.Sound(path)
                ResourceLoader._cache[path] = sound
            except pygame.error as e:
                print(f"Error loading sound at {path}: {e}")
                return None
        return sound
