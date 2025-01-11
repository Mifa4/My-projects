from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()

x, y, z = 162, 73, -1
pos = mc.player.getPos()
mc.postToChat(pos.x)
mc.postToChat(pos.y)
mc.postToChat(pos.z)

startx = x + 6
starty = y
startz = z


#mc.setBlocks(startx, starty, startz, startx + 8, starty, startz, 35, 4)
#mc.setBlocks(startx - 1, starty, startz + 1, startx + 9, starty, startz + 2, 35, 4)
#mc.setBlocks(startx - 2, starty, startz + 2, startx + 10, starty, startz + 2, 35, 4)

#for i in range(7):
#    mc.setBlocks(startx - i, starty, startz + i, startx + 8 + i, starty, startz + i, 35, 4)

#for i in range(7):
#    mc.setBlocks(startx - 6, starty, startz + 7 + i, startx + 18 - 4, starty, startz + 7 + i, 35, 4)

mc.setBlocks(168, y, -1, 175, y, -1, 35, 4)
mc.setBlocks(167, y, 0, 176, y, 0, 35, 4)
mc.setBlocks(166, y, 1, 177, y, 1, 35, 4)
mc.setBlocks(165, y, 2, 178, y, 2, 35, 4)
mc.setBlocks(164, y, 3, 179, y, 3, 35, 4)
mc.setBlocks(163, y, 4, 180, y, 4, 35, 4)
mc.setBlocks(162, y, 5, 181, y, 5, 35, 4)

mc.setBlocks(162, y, 6, 181, y, 11, 35, 4)

mc.setBlocks(162, y, 11, 163, y, 12, 35, 4)


mc.setBlocks(165, y, 11, 181, y, 12, 35, 4)


mc.setBlocks(166, y, 12, 180, y, 13, 35, 4)
mc.setBlocks(167, y, 13, 179, y, 13, 35, 4)
mc.setBlocks(168, y, 14, 179, y, 14, 35, 4)
mc.setBlocks(168, y, 15, 178, y, 15, 35, 4)
mc.setBlocks(167, y, 16, 179, y, 16, 35, 4)
mc.setBlocks(166, y, 17, 180, y, 17, 35, 4)
mc.setBlocks(165, y, 18, 181, y, 18, 35, 4)

mc.setBlocks(162, y, 20, 163, y, 18, 35, 4)

mc.setBlocks(162, y, 19, 181, y, 25, 35, 4)

mc.setBlocks(163, y, 26, 180, y, 26, 35, 4)

mc.setBlocks(164, y, 27, 179, y, 27, 35, 4)

mc.setBlocks(165, y, 28, 178, y, 28, 35, 4)

mc.setBlocks(166, y, 29, 177, y, 29, 35, 4)

mc.setBlocks(167, y, 30, 176, y, 30, 35, 4)

mc.setBlocks(168, y, 31, 175, y, 31, 35, 4)





mc.setBlocks(169, y, 2, 174, y, 2, 35, 15)

mc.setBlock(168, y, 3, 35, 15)

mc.setBlock(167, y, 4, 35, 15)
mc.setBlock(166, y, 5, 35, 15)
mc.setBlock(165, y, 6, 35, 15)

mc.setBlocks(165, y, 6, 165, y, 11, 35, 15)

mc.setBlock(166, y, 12, 35, 15)
mc.setBlock(167, y, 13, 35, 15)
mc.setBlock(168, y, 14, 35, 15)

mc.setBlocks(169, y, 15, 174, y, 15, 35, 15)

mc.setBlock(175, y, 3, 35, 15)
mc.setBlock(176, y, 4, 35, 15)
mc.setBlock(177, y, 5, 35, 15)


mc.setBlocks(178, y, 6, 178, y, 11, 35, 15)

mc.setBlock(177, y, 12, 35, 15)
mc.setBlock(176, y, 13, 35, 15)
mc.setBlock(175, y, 14, 35, 15)



mc.setBlocks(170, y, 4, 173, y, 4, 35, 15)

mc.setBlock(174, y, 5, 35, 15)
mc.setBlock(175, y, 6, 35, 15)

mc.setBlocks(176, y, 7, 176, y, 10, 35, 15)

mc.setBlock(175, y, 11, 35, 15)
mc.setBlock(174, y, 12, 35, 15)

mc.setBlocks(173, y, 13, 170, y, 13, 35, 15)

mc.setBlock(169, y, 12, 35, 15)
mc.setBlock(168, y, 11, 35, 15)

mc.setBlocks(167, y, 7, 167, y, 10, 35, 15)

mc.setBlock(169, y, 5, 35, 15)
mc.setBlock(168, y, 6, 35, 15)





mc.setBlocks(171, y, 6, 172, y, 6, 35, 15)

mc.setBlock(173, y, 7, 35, 15)

mc.setBlocks(174, y, 8, 174, y, 9, 35, 15)

mc.setBlock(173, y, 10, 35, 15)

mc.setBlocks(172, y, 11, 171, y, 11, 35, 15)

mc.setBlock(170, y, 10, 35, 15)

mc.setBlocks(169, y, 8, 169, y, 9, 35, 15)

mc.setBlock(170, y, 7, 35, 15)




mc.setBlock(175, y, 16, 35, 15)
mc.setBlock(176, y, 17, 35, 15)
mc.setBlock(177, y, 18, 35, 15)


mc.setBlocks(178, y, 19, 178, y, 24, 35, 15)


mc.setBlock(177, y, 25, 35, 15)
mc.setBlock(176, y, 26, 35, 15)
mc.setBlock(175, y, 27, 35, 15)


mc.setBlocks(174, y, 28, 169, y, 28, 35, 15)


mc.setBlock(168, y, 27, 35, 15)
mc.setBlock(167, y, 26, 35, 15)
mc.setBlock(166, y, 25, 35, 15)


mc.setBlocks(165, y, 19, 165, y, 24, 35, 15)


mc.setBlock(166, y, 18, 35, 15)
mc.setBlock(167, y, 17, 35, 15)
mc.setBlock(168, y, 16, 35, 15)


mc.setBlocks(170, y, 17, 173, y, 17, 35, 15)

mc.setBlock(174, y, 18, 35, 15)
mc.setBlock(175, y, 19, 35, 15)

mc.setBlocks(176, y, 20, 176, y, 23, 35, 15)

mc.setBlock(175, y, 24, 35, 15)
mc.setBlock(174, y, 25, 35, 15)

mc.setBlocks(170, y, 26, 173, y, 26, 35, 15)

mc.setBlock(169, y, 25, 35, 15)
mc.setBlock(168, y, 24, 35, 15)

mc.setBlocks(167, y, 20, 167, y, 23, 35, 15)

mc.setBlock(168, y, 19, 35, 15)
mc.setBlock(169, y, 18, 35, 15)


mc.setBlocks(171, y, 19, 172, y, 19, 35, 15)

mc.setBlock(173, y, 20, 35, 15)

mc.setBlocks(174, y, 21, 174, y, 22, 35, 15)

mc.setBlock(173, y, 23, 35, 15)

mc.setBlocks(171, y, 24, 172, y, 24, 35, 15)

mc.setBlock(170, y, 23, 35, 15)

mc.setBlocks(169, y, 21, 169, y, 22, 35, 15)

mc.setBlock(170, y, 20, 35, 15)




# LEVOE UHO

mc.setBlocks(179, y, 2, 179, y, 4, 35, 15)
mc.setBlocks(178, y, 2, 178, y, 3, 35, 15)
mc.setBlock(177, y, 2, 35, 15)

# PRAVOE UHO

mc.setBlocks(179, y, 26, 179, y, 28, 35, 15)
mc.setBlocks(178, y, 27, 178, y, 28, 35, 15)
mc.setBlock(177, y, 28, 35, 15)


# NOS

mc.setBlock(167, y, 15, 35, 15)
mc.setBlocks(166, y, 14, 166, y, 16, 35, 15)
mc.setBlocks(165, y, 13, 165, y, 17, 35, 15)
mc.setBlocks(164, y, 12, 164, y, 18, 35, 15)

mc.setBlocks(163, y, 13, 163, y, 17, 35, 15)
mc.setBlocks(162, y, 14, 162, y, 16, 35, 15)

mc.setBlock(161, y, 15, 35, 15)