import cppyy

cppyy.include('./main.hpp')
cppyy.load_library('./libstockfish.so')

#Namespaces
StockfishNS = cppyy.gbl.Stockfish
UCI = StockfishNS.UCI
PSQT = StockfishNS.PSQT
Bitboards = StockfishNS.Bitboards
Bitbases = StockfishNS.Bitbases
Endgames = StockfishNS.Endgames
Search = StockfishNS.Search
Eval = StockfishNS.Eval
NNUE = Eval.NNUE

#Classes
Tune = StockfishNS.Tune
Position = StockfishNS.Position
MoveList_LEGAL = StockfishNS.MoveList_LEGAL

#Objects
Options = StockfishNS.Options
Threads = StockfishNS.Threads

class Moves(object):

    def __init__(self, movelist):
        self.movelist = movelist
        
    def __iter__(self):
        self.idx = -1
        self.end = self.movelist.size()
        return self
    
    def __next__(self):
        self.idx += 1
        if self.idx not in range(self.end):
            raise StopIteration

        return self.movelist.item(self.idx)

    def __del__(self):
        del self.movelist
        
class Stockfish(object):

    def __init__(self):
        UCI.init(Options)
        Tune.init()
        PSQT.init()
        Bitboards.init()
        Position.init()
        Bitbases.init()
        Endgames.init()
        Threads.set(int(Options['Threads'].__float__()))
        Search.clear()
        NNUE.init()

        self.pos = Position()
        for name,val in Options:
            print(name, val)
        
    def __del__(self):
        del self.pos
        Threads.set(0)

    def position(self, position_str):
        UCI.set_position(self.pos, position_str)

    def is_chess960(self):
        return self.pos.is_chess960()
    
    def legal_moves(self):
        return Moves(MoveList_LEGAL(self.pos))

    def legal_moves_str(self):
        is_chess960 = self.is_chess960()
        return [UCI.move(m.move, is_chess960) for m in self.legal_moves()]
