from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()

x, y, z = 162, 73, -1


mc.player.setPos(x, y, z)