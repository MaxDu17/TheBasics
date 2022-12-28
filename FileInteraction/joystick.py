import pygame

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# XYZ Dimensions
x = - joystick.get_axis(1)
y = - joystick.get_axis(0)
z = (joystick.get_axis(5) - joystick.get_axis(2)) / 2

# Orientation Dimensions
yaw = joystick.get_axis(3)
pitch = -joystick.get_axis(4)
roll = joystick.get_button(4) - joystick.get_button(5)