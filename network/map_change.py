from utils.map import Map
import logging
from input.window import Window

# 1, -34
# DATA = 'GDM|1853|0706131721|4c2f4c4c7d204c71236065687966574a554e3d464841354820462930786b6f5f2f225f2f51632f7b78342f41206e7a2877377c61555a7378764d33553a622e5b57343a3d602422737c732447686a787538755d644660682d756864376e2a4b436c6b4f576c60263b703b2139766b44407326554c68327c5f39383031445d613d677369473b5877274262'

# 3, 2
DATA = 'GDM|10293|0706131721|29664658354738356926404631512e64464f7b473f7d5266452e503f4152464f4b7b35305e5f452532356a68726f4031712855213b27253242275724417665633e2e3e4d4322622c735c51755a6e60462430302e54654767517248623a2a38723b3a27536a2c3821654d3668253235776f65566c357d33395f2532424e2648217324452a452938606d727841486f53482c3625323536407152573e312f226a5a5357782f74413348605a79395034536b694a24642532427e566b55236d4d5245706d453c79677b5d'

# GDM
class MapChange:
    def __init__(self, raw):
        data = raw[4:].split('|')
        map_id = data[0]
        map_date = data[1]
        map_key = data[2]
        self.map = Map(map_id, map_date, map_key)


if __name__ == '__main__':
    m = MapChange(DATA)
    # m.map.debug()
    cell = m.map.cells[15]
    print(cell)
    s = m.map.sight.compute_sight(cell.posIJ, 3)
    m.map.sight.display(s)
    # m.map.graph.debug_edges()
    # w = Window.list_windows()[0]
    # w.focus()
    # logging.basicConfig(level=logging.DEBUG)
    # w.click_cell(24, debug=True)



