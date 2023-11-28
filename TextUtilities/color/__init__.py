"""Provides color text utilities like:
    - `rgbtext(text, red, green, blue, reset)`
"""


def rgbtext(text: str, red: int, green: int, blue: int, reset: bool) -> str:
    """
    The function `rgbtext` takes a text string and RGB color values as input, and returns the text with
    the specified color applied.

    Args:
      text (str): The text parameter is a string that represents the text that you want to format with RGB color.
      red (int): The "red" parameter is an integer representing the amount of red color in the RGB color model. It should be a value between 0 and 255.
      green (int): The "green" parameter in the function `rgbtext` represents the intensity of the green color component in the RGB color model. It is an integer value ranging from 0 to 255, where 0 represents no green and 255 represents maximum intensity of green.
      blue (int): The `blue` parameter in the `rgbtext` function represents the intensity of the blue color component in the RGB color model. It is an integer value ranging from 0 to 255, where 0 represents no blue and 255 represents maximum intensity blue.
      reset (bool): A boolean parameter that determines whether to reset the text color back to the default after applying the RGB color. If reset is True, the text color will be reset to the default color. If reset is False, the text color will remain as the RGB color.

    Returns:
      a string with the specified text formatted with the specified RGB color values. If the "reset"
    parameter is set to True, the string will also include a reset code to revert the text color back to
    the default.
    """
    textretrun = "[38;2;{0};{1};{2}m{3}".format(
        red, green, blue, text)
    if reset:
        textretrun = textretrun + "[37m"
    return textretrun
