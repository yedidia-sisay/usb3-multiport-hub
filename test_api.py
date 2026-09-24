import pcbnew
import sys

board = pcbnew.LoadBoard("usb_hub_2.kicad_pcb")
settings = board.GetDesignSettings()

print("TrackMinWidth:", settings.m_TrackMinWidth)
nc = settings.GetNetClasses().Find("Default")
print("Default NC:", nc)

# Test renaming
nets = board.GetNetsByName()
for name, net in nets.items():
    if "HDTX" in name:
        print("Found net:", name)
        break

print("Done")
