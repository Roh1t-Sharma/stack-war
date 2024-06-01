import logging

# Configure the logging
def setup_logging():
    # Create a logger object
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)  # Set the minimum log level to DEBUG

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler('game.log')
    file_handler.setLevel(logging.INFO)  # Set the file handler log level to INFO

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Console handler log level

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instantiating the logger
game_logger = setup_logging()

def get_logger():
    return game_logger
