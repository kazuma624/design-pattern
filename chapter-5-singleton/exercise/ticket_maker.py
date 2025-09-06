class TicketMaker:
    _singleton = None
    _ticket: int = 1000

    def __new__(cls):
        """これがないと、カウンターの状態は保たれるがインスタンスはいくらでも作れてしまう
        作れてしまうと何がまずいのかはこの例だとよくわからん
        """
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        return cls._singleton

    @classmethod
    def get_next_ticket_number(cls) -> int:
        cls._ticket += 1
        return cls._ticket


if __name__ =="__main__":
    t1 = TicketMaker()
    n1 = t1.get_next_ticket_number()
    print(n1)

    t2 = TicketMaker()
    n2 = t2.get_next_ticket_number()
    print(n2)


