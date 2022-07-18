def readFile(root):
    with open('test.txt', "w") as t:
        _alphabet = {'0', '1', 'e', '0,1'}
        _states = []
        _states2 = []
        _state_final = []
        _state_start = 0
        _tran = dict()
        for automaton in root.findall('automaton'):  # Truy cập thuộc tính automaton
            for state in automaton.findall('state'):  # Truy cập thuộc tính state
                _name = state.get('name')  # Truy cập tên nút
                _states.append(_name)
                for child in state:
                    if child.tag.find('initial') == 0:  # tìm nút initial
                        _state_start = _name
                    if child.tag.find('final') == 0:  # tìm nút final
                        _state_final.append(_name)
            # dict tran{} biểu diễn transition table của Automaton
        for x in set(_states):
            _tran[x] = {}
            for letter in _alphabet:
                _tran[x][letter] = 'null'
        for automaton in root.findall('automaton'):
            for transition in automaton.findall('transition'):
                _from = transition.find('from').text
                _read = transition.find('read').text
                _to = transition.find('to').text
                if _read not in _alphabet:
                    _read = 'e'
                if _tran[_states[int(_from)]][_read] == 'null':
                    _tran[_states[int(_from)]][_read] = _states[int(_to)].split()
                else:
                    _tran[_states[int(_from)]][_read].extend(_states[int(_to)].split())
        return _tran, _state_start, _state_final
