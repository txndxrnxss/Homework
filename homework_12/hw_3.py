class InvalidInt(Exception):
    ...
class InvalidFloat(Exception):
    ...
class InvalidStr(Exception):
    ...
    
class Queue():
    queue = []

    def add(self, *agrs):
        for i in agrs:
            try:
                if isinstance(i, int):
                    if i % 8 == 0 and len(str(i)) <= 4:
                        self.queue.append(i)
                    else:
                        raise InvalidInt
                elif isinstance(i, float):
                    if round(i, 2) == i:
                        self.queue.append(i)
                    else:
                        raise InvalidFloat
                elif isinstance(i, str):
                    a = 0
                    for c in i:
                        if i.count(c) > 1:
                            a = i.count(c) 
                    if len(i) <= 4 and a < 2:
                        self.queue.append(i)
                    else:
                        raise InvalidStr
            except InvalidInt:
                print(f'{i} - не делится на 8 или больше 4 символов')
            except InvalidFloat:
                print(f'{i} - больше 2 символов после запятой')
            except InvalidStr:
                print(f'{i} - содержит 2 повторяющихся знака или длиннее 4 знаков')
        print(f'{self.queue}')