import pygame
import sys
from methodClass import *
import math


def connect(i, j, point_list, color, thickness):
    a, b = point_list[i], point_list[j]
    pygame.draw.line(screen, color, [a.x + size_x // 2, a.y + size_y // 2],cd 
                     [b.x + size_x // 2, b.y + size_y // 2], thickness)


def connect_rect(i, j, k, g, point_list, color):
    a, b, c, d = point_list[i], point_list[j], point_list[k], point_list[g]
    points_rect = [(a.x + size_x // 2, a.y + size_y // 2), (b.x + size_x // 2, b.y + size_y // 2),
                   (c.x + size_x // 2, c.y + size_y // 2), (d.x + size_x // 2, d.y + size_y // 2)]
    pygame.draw.polygon(screen, color, points_rect)

pygame.init()
clock = pygame.time.Clock()

size_x, size_y = 1000, 600
screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption('Projection 3D')

points = [
    Point3D(50, -50, 50), Point3D(50, 50, 50), Point3D(-50, -50, 50), Point3D(-50, 50, 50),
    Point3D(50, -50, -50), Point3D(50, 50, -50), Point3D(-50, -50, -50), Point3D(-50, 50, -50),

    Point3D(35, -35, 35), Point3D(35, 35, 35), Point3D(-35, -35, 35), Point3D(-35, 35, 35),
    Point3D(35, -35, -35), Point3D(35, 35, -35), Point3D(-35, -35, -35), Point3D(-35, 35, -35),

    Point3D(20, -20, 20), Point3D(20, 20, 20), Point3D(-20, -20, 20), Point3D(-20, 20, 20),
    Point3D(20, -20, -20), Point3D(20, 20, -20), Point3D(-20, -20, -20), Point3D(-20, 20, -20)
]

angle, scale, running = 0, 3, True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    rotation_x = [
        [1, 0, 0],
        [0, math.cos(angle), -1 * math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    rotation_y = [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-1 * math.sin(angle), 0, math.cos(angle)]
    ]

    rotation_z = [
        [math.cos(angle), -1 * math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]

    projection = [
        [1, 0, 0],
        [0, 1, 0]
    ]

    projected = []
    for point in points:
        rotated = matmul2(rotation_x, point)
        rotated = matmul1(rotation_y, rotated)
        rotated = matmul1(rotation_z, rotated)

        projected.append(matrixToVec(multiply_matrix_by_scalar((matmul1(projection, rotated)), scale)))

    angle += .007

    for projected_point in projected:
        pygame.draw.circle(screen, (255, 255, 255), (projected_point.x + size_x // 2, projected_point.y + size_y // 2), 0)

    connect_square_outer = [
        (8, 9, 0, 1), (8, 0, 9, 1), (8, 10, 0, 2), (8, 0, 10, 2),
        (8, 12, 0, 4), (8, 0, 12, 4), (9, 11, 1, 3), (9, 1, 11, 3),
        (9, 13, 1, 5), (9, 1, 13, 5), (10, 11, 2, 3), (10, 2, 11, 3),
        (10, 14, 2, 6), (10, 2, 14, 6), (10, 16, 2, 8), (10, 2, 16, 8),
        (11, 15, 3, 7), (11, 3, 15, 7), (12, 13, 4, 5), (12, 4, 13, 5),
        (12, 14, 6, 4), (12, 6, 14, 4), (13, 15, 5, 7), (13, 5, 15, 7),
        (14, 15, 6, 7), (14, 6, 15, 7),
    ]

    for point in connect_square_outer:
        connect_rect(point[0], point[1], point[2], point[3], projected, (105, 105, 105))

    connect_square_middle = [
        (16, 17, 8, 9), (16, 8, 17, 9), (16, 18, 8, 10), (16, 8, 18, 10),
        (16, 20, 8, 12), (16, 8, 20, 12), (17, 19, 9, 11), (17, 9, 19, 11),
        (17, 21, 9, 13), (17, 9, 21, 13), (18, 19, 10, 11), (18, 10, 19, 11),
        (18, 22, 10, 14), (18, 10, 22, 14), (19, 23, 11, 15), (19, 11, 23, 15),
        (20, 21, 12, 13), (20, 12, 21, 13), (20, 22, 12, 14), (20, 12, 22, 14),
        (21, 23, 13, 15), (21, 13, 23, 15), (22, 23, 14, 15), (22, 14, 23, 15),
    ]
    for point in connect_square_middle:
        connect_rect(point[0], point[1], point[2], point[3], projected, (180, 180, 180))

    connect_square_inner = [
        (16, 20, 18, 22), (16, 18, 20, 22), (16, 17, 18, 19), (16, 18, 17, 19),
        (16, 17, 21, 20), (17, 18, 22, 21), (17, 19, 21, 23), (17, 21, 19, 23),
        (18, 19, 23, 22), (16, 19, 23, 20), (20, 21, 22, 23), (20, 22, 21, 23),
    ]
    for point in connect_square_inner:
        connect_rect(point[0], point[1], point[2], point[3], projected, (255, 255, 255))

    connect_lines = [
        (0, 1), (2, 3), (4, 5), (6, 7),
        (1, 5), (3, 7), (0, 4), (2, 6),
        (0, 2), (4, 6), (1, 3), (5, 7),

        (8, 9), (10, 11), (12, 13), (14, 15),
        (9, 13), (11, 15), (8, 12), (10, 14),
        (8, 10), (12, 14), (9, 11), (13, 15),

        (16, 17), (18, 19), (20, 21), (22, 23),
        (17, 21), (19, 23), (16, 20), (18, 22),
        (16, 18), (20, 22), (17, 19), (21, 23),

        (0, 8), (1, 9), (2, 10), (3, 11),
        (4, 12), (5, 13), (6, 14), (7, 15),

        (16, 8), (17, 9), (18, 10), (19, 11),
        (20, 12), (21, 13), (22, 14), (23, 15),
    ]
    for point in connect_lines:
        connect(point[0], point[1], projected, (255, 255, 255), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
