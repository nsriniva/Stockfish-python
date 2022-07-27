import cppyy

cppyy.include('./stockfish.h')
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

#The default values for the various options are:
#Clear Hash 0
#Debug Log File 0
#EvalFile 0
#Hash 16
#Move Overhead 10
#MultiPV 1
#nodestime 0
#Ponder 0
#Skill Level 20
#Slow Mover 100
#Syzygy50MoveRule 1
#SyzygyPath 0
#SyzygyProbeDepth 1
#SyzygyProbeLimit 7
#Threads 1
#UCI_AnalyseMode 0
#UCI_Chess960 0
#UCI_Elo 1350
#UCI_LimitStrength 0
#UCI_ShowWDL 0
#Use NNUE 1
#LEGAL Iteration 0
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
        # The default value for the 'Threads' option is 1.
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
