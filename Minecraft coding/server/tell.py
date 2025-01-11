from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat(pos.x)
mc.postToChat(pos.y)
mc.postToChat(pos.z)
