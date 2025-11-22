def my_print(self):
    """Print the square with the character #."""
    if self.__size == 0:
        print()
        return
    for i in range(self.__size):
        print("#" * self.__size)
