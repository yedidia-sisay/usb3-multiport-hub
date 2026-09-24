import pcbnew
board = pcbnew.LoadBoard("usb_hub_2.kicad_pcb")
pcbnew.ImportSpecctraSES(board, "usb_hub_2.ses")
pcbnew.SaveBoard("usb_hub_2.kicad_pcb", board)
print("Imported SES and saved board!")
