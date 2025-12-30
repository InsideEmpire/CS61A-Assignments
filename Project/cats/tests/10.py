test = {
  'name': 'Problem 10',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})
          [['What'], ['great', 'luck']]
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 3]
          >>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})  # with a tie, choose the first player
          [['What', 'luck'], ['great']]
          >>> p2 = [4, 3, 1]
          >>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1, p2]})
          [['What'], ['great'], ['luck']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p0 = [5, 1, 3]
          >>> p1 = [4, 1, 6]
          >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
          [['have', 'fun'], ['Just']]
          >>> p0  # input lists should not be mutated
          [5, 1, 3]
          >>> p1
          [4, 1, 6]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3], [5]]
          >>> fastest_words({'words': ['smopple'], 'times': p})
          [['smopple'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [2], [4]]
          >>> fastest_words({'words': ['seeingly'], 'times': p})
          [[], ['seeingly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 2, 3, 4], [1, 5, 3, 4, 1], [5, 1, 5, 2, 3]]
          >>> fastest_words({'words': ['reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary'], 'times': p})
          [['unweld', 'handgun'], ['reundergo', 'recessionary'], ['hydrometra']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2]]
          >>> fastest_words({'words': ['prebeleve', 'upanishadic', 'ftp'], 'times': p})
          [['prebeleve', 'upanishadic', 'ftp']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 5, 2, 4], [2, 4, 5, 1, 2], [1, 5, 2, 1, 3]]
          >>> fastest_words({'words': ['supplies', 'underivedly', 'henter', 'undeserving', 'uncope'], 'times': p})
          [['underivedly'], ['undeserving', 'uncope'], ['supplies', 'henter']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 5, 5, 5]]
          >>> fastest_words({'words': ['pentarch', 'nihilification', 'krieker', 'laureate', 'antechamber'], 'times': p})
          [['pentarch', 'nihilification', 'krieker', 'laureate', 'antechamber']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 4, 3, 4]]
          >>> fastest_words({'words': ['urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation'], 'times': p})
          [['urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 1, 1, 4, 1], [5, 3, 3, 4, 5, 3], [1, 2, 3, 1, 3, 5]]
          >>> fastest_words({'words': ['isoborneol', 'glabrate', 'excision', 'octobass', 'prevolitional', 'archtreasurership'], 'times': p})
          [['excision', 'octobass', 'archtreasurership'], [], ['isoborneol', 'glabrate', 'prevolitional']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 4, 3, 1], [3, 1, 2, 1, 3]]
          >>> fastest_words({'words': ['singletree', 'apocyneous', 'imminution', 'uncensuring', 'fungiform'], 'times': p})
          [['fungiform'], ['singletree', 'apocyneous', 'imminution', 'uncensuring']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2], [3, 2]]
          >>> fastest_words({'words': ['snideness', 'universalization'], 'times': p})
          [['snideness', 'universalization'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [3]]
          >>> fastest_words({'words': ['dependably'], 'times': p})
          [['dependably'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1]]
          >>> fastest_words({'words': ['spaceful', 'cautery', 'wiseness'], 'times': p})
          [['spaceful', 'cautery', 'wiseness']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 5, 3, 5, 1], [4, 4, 1, 2, 5, 3]]
          >>> fastest_words({'words': ['investigatable', 'quadrigenarious', 'protonemal', 'cardiodysneuria', 'provoker', 'associated'], 'times': p})
          [['investigatable', 'quadrigenarious', 'provoker', 'associated'], ['protonemal', 'cardiodysneuria']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1]]
          >>> fastest_words({'words': ['tubuliporoid', 'malleability'], 'times': p})
          [['tubuliporoid', 'malleability']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 2, 4, 4], [3, 4, 3, 3, 5], [1, 2, 5, 1, 2]]
          >>> fastest_words({'words': ['shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright'], 'times': p})
          [['shrubbiness', 'demoded'], [], ['shilling', 'commentary', 'housewright']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3, 3, 4, 1]]
          >>> fastest_words({'words': ['ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular'], 'times': p})
          [['ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 4, 3, 1], [5, 5, 1, 2, 3]]
          >>> fastest_words({'words': ['lithosis', 'bogland', 'interclash', 'widespread', 'thumbbird'], 'times': p})
          [['lithosis', 'bogland', 'thumbbird'], ['interclash', 'widespread']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2], [3, 3]]
          >>> fastest_words({'words': ['diplosphenal', 'cholecystogram'], 'times': p})
          [['diplosphenal', 'cholecystogram'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2]]
          >>> fastest_words({'words': ['eugenist', 'karyopyknosis'], 'times': p})
          [['eugenist', 'karyopyknosis']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 3]]
          >>> fastest_words({'words': ['cannily', 'lune', 'heathless'], 'times': p})
          [['cannily', 'lune', 'heathless']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 3, 3], [2, 1, 3, 4], [2, 2, 4, 4]]
          >>> fastest_words({'words': ['postprandially', 'helicogyrate', 'coccidology', 'circumradius'], 'times': p})
          [['coccidology', 'circumradius'], ['postprandially', 'helicogyrate'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3], [1, 3], [5, 1]]
          >>> fastest_words({'words': ['electrofused', 'incontinent'], 'times': p})
          [[], ['electrofused'], ['incontinent']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 2, 5, 3], [3, 3, 5, 5, 3]]
          >>> fastest_words({'words': ['trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'], 'times': p})
          [['trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 1, 1, 2], [1, 1, 5, 3, 4]]
          >>> fastest_words({'words': ['boucherism', 'rutabaga', 'fomentation', 'swampside', 'unpopularness'], 'times': p})
          [['rutabaga', 'fomentation', 'swampside', 'unpopularness'], ['boucherism']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [1, 2]]
          >>> fastest_words({'words': ['introspectionist', 'teeting'], 'times': p})
          [['teeting'], ['introspectionist']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 1, 2, 3, 3]]
          >>> fastest_words({'words': ['cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient'], 'times': p})
          [['cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 2, 2, 3], [1, 2, 5, 1, 3]]
          >>> fastest_words({'words': ['quodlibetic', 'previdence', 'nonviscous', 'reduplicatively', 'arterioverter'], 'times': p})
          [['nonviscous', 'arterioverter'], ['quodlibetic', 'previdence', 'reduplicatively']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 1, 2, 1], [4, 2, 1, 4, 5, 3]]
          >>> fastest_words({'words': ['cactoid', 'quadrialate', 'preflattery', 'emancipation', 'recedent', 'haustement'], 'times': p})
          [['cactoid', 'quadrialate', 'emancipation', 'recedent', 'haustement'], ['preflattery']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 5, 4, 4, 4], [5, 2, 1, 1, 2, 3], [4, 5, 4, 2, 3, 2]]
          >>> fastest_words({'words': ['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous', 'phycomycete'], 'times': p})
          [['puboprostatic', 'tumescent'], ['keraunograph', 'telecaster', 'selenigenous'], ['phycomycete']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 2, 4, 2], [1, 5, 1, 4, 5]]
          >>> fastest_words({'words': ['indisputableness', 'breastrope', 'hypocist', 'supersemination', 'ethnographically'], 'times': p})
          [['breastrope', 'supersemination', 'ethnographically'], ['indisputableness', 'hypocist']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 3, 3, 5, 4]]
          >>> fastest_words({'words': ['repetitiously', 'lecideiform', 'debtless', 'stream', 'loquent', 'leery'], 'times': p})
          [['repetitiously', 'lecideiform', 'debtless', 'stream', 'loquent', 'leery']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 3, 3, 3, 1, 4]]
          >>> fastest_words({'words': ['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations'], 'times': p})
          [['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 5, 4], [5, 4, 2, 2]]
          >>> fastest_words({'words': ['holland', 'nursedom', 'epidictical', 'defortify'], 'times': p})
          [['holland', 'nursedom'], ['epidictical', 'defortify']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 3]]
          >>> fastest_words({'words': ['sunbird', 'renewal', 'predivinable'], 'times': p})
          [['sunbird', 'renewal', 'predivinable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 4, 2], [5, 2, 2, 3]]
          >>> fastest_words({'words': ['tillot', 'douser', 'twankingly', 'eccentrate'], 'times': p})
          [['tillot', 'eccentrate'], ['douser', 'twankingly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 5, 3]]
          >>> fastest_words({'words': ['reest', 'predigest', 'adipocellulose', 'warriorwise'], 'times': p})
          [['reest', 'predigest', 'adipocellulose', 'warriorwise']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 5, 3, 5]]
          >>> fastest_words({'words': ['standing', 'cameroon', 'unpretendingly', 'puppydom', 'lardworm'], 'times': p})
          [['standing', 'cameroon', 'unpretendingly', 'puppydom', 'lardworm']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4], [5, 5]]
          >>> fastest_words({'words': ['cardioarterial', 'statolatry'], 'times': p})
          [['cardioarterial', 'statolatry'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4, 1]]
          >>> fastest_words({'words': ['whirley', 'coldly', 'compendiary', 'grovel'], 'times': p})
          [['whirley', 'coldly', 'compendiary', 'grovel']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [3, 3], [2, 4]]
          >>> fastest_words({'words': ['caducicorn', 'monociliated'], 'times': p})
          [['caducicorn', 'monociliated'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 4, 5, 3]]
          >>> fastest_words({'words': ['audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx'], 'times': p})
          [['audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [4], [4]]
          >>> fastest_words({'words': ['millage'], 'times': p})
          [[], ['millage'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1], [5, 4]]
          >>> fastest_words({'words': ['inyoite', 'complications'], 'times': p})
          [['inyoite', 'complications'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2], [2, 2], [4, 1]]
          >>> fastest_words({'words': ['sarcodous', 'microbiological'], 'times': p})
          [['sarcodous'], [], ['microbiological']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 1], [2, 2, 3]]
          >>> fastest_words({'words': ['chromophilic', 'brabant', 'detailed'], 'times': p})
          [['detailed'], ['chromophilic', 'brabant']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1, 1], [3, 1, 3, 3]]
          >>> fastest_words({'words': ['allochiral', 'hear', 'snur', 'myosarcomatous'], 'times': p})
          [['hear', 'snur', 'myosarcomatous'], ['allochiral']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [5]]
          >>> fastest_words({'words': ['studiedly'], 'times': p})
          [['studiedly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3, 3, 5, 2, 5]]
          >>> fastest_words({'words': ['katatonia', 'myoporaceous', 'tribunitive', 'mungofa', 'demodectic', 'kolobion'], 'times': p})
          [['katatonia', 'myoporaceous', 'tribunitive', 'mungofa', 'demodectic', 'kolobion']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2], [2, 2]]
          >>> fastest_words({'words': ['cheeser', 'cumulation'], 'times': p})
          [['cumulation'], ['cheeser']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2], [1, 3]]
          >>> fastest_words({'words': ['overemphatic', 'telpherway'], 'times': p})
          [['telpherway'], ['overemphatic']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4], [1, 2], [3, 5]]
          >>> fastest_words({'words': ['ultradolichocephalic', 'kinetophone'], 'times': p})
          [[], ['ultradolichocephalic', 'kinetophone'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 3]]
          >>> fastest_words({'words': ['protosaurian', 'plumbable', 'siroccoishly'], 'times': p})
          [['protosaurian', 'plumbable', 'siroccoishly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4, 5, 1, 1]]
          >>> fastest_words({'words': ['hydroidean', 'pesterer', 'seedcase', 'rudder', 'muttering', 'individualize'], 'times': p})
          [['hydroidean', 'pesterer', 'seedcase', 'rudder', 'muttering', 'individualize']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1, 2], [2, 3, 5, 3]]
          >>> fastest_words({'words': ['oleostearin', 'stitching', 'theanthropism', 'blate'], 'times': p})
          [['stitching', 'theanthropism', 'blate'], ['oleostearin']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 1], [2, 2]]
          >>> fastest_words({'words': ['oscillatory', 'geophyte'], 'times': p})
          [['oscillatory', 'geophyte'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [2]]
          >>> fastest_words({'words': ['withsave'], 'times': p})
          [['withsave'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1], [5, 3, 4]]
          >>> fastest_words({'words': ['battlewise', 'dare', 'halibiu'], 'times': p})
          [['battlewise', 'dare', 'halibiu'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 4, 2], [4, 3, 5, 5]]
          >>> fastest_words({'words': ['muscoid', 'reliquidation', 'broad', 'tugging'], 'times': p})
          [['muscoid', 'reliquidation', 'broad', 'tugging'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 5]]
          >>> fastest_words({'words': ['trophobiosis', 'parascenium', 'gibbet'], 'times': p})
          [['trophobiosis', 'parascenium', 'gibbet']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 1, 4]]
          >>> fastest_words({'words': ['nonsparking', 'calool', 'dorsopleural'], 'times': p})
          [['nonsparking', 'calool', 'dorsopleural']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4], [4, 4], [5, 3]]
          >>> fastest_words({'words': ['unexcusableness', 'bismuthyl'], 'times': p})
          [['unexcusableness'], [], ['bismuthyl']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 5, 5, 2], [1, 4, 1, 2, 4]]
          >>> fastest_words({'words': ['evolution', 'intransigency', 'improperly', 'angiophorous', 'urinogenital'], 'times': p})
          [['intransigency', 'urinogenital'], ['evolution', 'improperly', 'angiophorous']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 1]]
          >>> fastest_words({'words': ['penceless', 'bromothymol', 'reticuloramose'], 'times': p})
          [['penceless', 'bromothymol', 'reticuloramose']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 5, 2, 2, 3]]
          >>> fastest_words({'words': ['monument', 'appressor', 'tutu', 'gentilize', 'trihemimeral', 'bifid'], 'times': p})
          [['monument', 'appressor', 'tutu', 'gentilize', 'trihemimeral', 'bifid']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 3, 3, 5, 2]]
          >>> fastest_words({'words': ['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer'], 'times': p})
          [['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [4], [3]]
          >>> fastest_words({'words': ['inclementness'], 'times': p})
          [['inclementness'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words({'words': [], 'times': p})
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 3, 1, 2, 4]]
          >>> fastest_words({'words': ['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis'], 'times': p})
          [['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4], [5], [4]]
          >>> fastest_words({'words': ['transmundane'], 'times': p})
          [['transmundane'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3]]
          >>> fastest_words({'words': ['becense', 'hyperingenuity'], 'times': p})
          [['becense', 'hyperingenuity']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 4], [5, 5, 3], [3, 2, 3]]
          >>> fastest_words({'words': ['interventional', 'demiditone', 'chrysophilite'], 'times': p})
          [[], ['chrysophilite'], ['interventional', 'demiditone']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 3, 5, 1, 3], [1, 4, 3, 1, 3, 4], [1, 3, 1, 4, 4, 5]]
          >>> fastest_words({'words': ['pyritology', 'marbleize', 'blooddrop', 'prickingly', 'ecole', 'capitellar'], 'times': p})
          [['ecole', 'capitellar'], ['pyritology', 'prickingly'], ['marbleize', 'blooddrop']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 4, 5, 4, 3], [1, 3, 1, 1, 3, 5]]
          >>> fastest_words({'words': ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious', 'untakableness'], 'times': p})
          [['untakableness'], ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3], [4, 3], [5, 5]]
          >>> fastest_words({'words': ['tutoyer', 'fibrilliferous'], 'times': p})
          [['tutoyer', 'fibrilliferous'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 2, 1]]
          >>> fastest_words({'words': ['aneuploidy', 'unrubified', 'dynamic', 'twistable'], 'times': p})
          [['aneuploidy', 'unrubified', 'dynamic', 'twistable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 2, 3]]
          >>> fastest_words({'words': ['pholadoid', 'toxicodermatitis', 'gallification', 'survival'], 'times': p})
          [['pholadoid', 'toxicodermatitis', 'gallification', 'survival']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3, 1, 4, 5], [5, 2, 3, 2, 3]]
          >>> fastest_words({'words': ['principiate', 'archinfamy', 'cacomixle', 'endonuclear', 'writer'], 'times': p})
          [['principiate', 'cacomixle'], ['archinfamy', 'endonuclear', 'writer']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2, 4]]
          >>> fastest_words({'words': ['mechanicalist', 'losing', 'emancipation', 'counterquarterly'], 'times': p})
          [['mechanicalist', 'losing', 'emancipation', 'counterquarterly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1], [2, 1, 3]]
          >>> fastest_words({'words': ['subframe', 'infinitude', 'astrochemist'], 'times': p})
          [['astrochemist'], ['subframe', 'infinitude']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2]]
          >>> fastest_words({'words': ['isocheimal'], 'times': p})
          [['isocheimal']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 4, 5], [5, 4, 5, 2]]
          >>> fastest_words({'words': ['mistresshood', 'lazzarone', 'define', 'unmudded'], 'times': p})
          [['mistresshood', 'lazzarone', 'define'], ['unmudded']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 2, 2, 4], [3, 5, 4, 5, 1]]
          >>> fastest_words({'words': ['either', 'ungenuine', 'dealable', 'pejorism', 'cointersecting'], 'times': p})
          [['ungenuine', 'dealable', 'pejorism'], ['either', 'cointersecting']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1]]
          >>> fastest_words({'words': ['narcoanesthesia', 'tanbur'], 'times': p})
          [['narcoanesthesia', 'tanbur']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words({'words': [], 'times': p})
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4]]
          >>> fastest_words({'words': ['overappraise', 'disdiapason'], 'times': p})
          [['overappraise', 'disdiapason']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
