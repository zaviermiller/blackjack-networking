class Player:

    def __init__(self, name):
        self._name = name
        self._connection = None
        self._funds = 1000
        self._bet = 0
        self._cards = []

    def __repr__(self):
        return self._name

    def set_connection(self, connection):
        self._connection = connection

    def set_bet(self, bet):
        self._funds -= int(bet)
        self._bet = int(bet)

    def order_cards(self):
        values = {"King": 10, "Queen": 10, "Jack": 10, "Ace": 11}

        n = len(self._cards)

        for i in range(n):
            for j in range(0, n-i-1):
                try:
                    firstCard = values[self._cards[j].value]
                except:
                    firstCard = self._cards[j].value
                try:
                    secondCard = values[self._cards[j+1].value]
                except:
                    secondCard = self._cards[j+1].value

                if firstCard > secondCard:
                    self._cards[j], self._cards[j +
                                                1] = self._cards[j+1], self._cards[j]

    def show_cards(self):
        suits = {
            "Diamonds": "♦",
            "Hearts": "♥",
            "Clubs": "♣",
            "Spades": "♠"
        }

        lines = [[] for i in range(9)]

        for _, card in enumerate(self._cards):
            if card.value == 10:
                val = card.value
                space = ""
            else:
                try:
                    val = card.value[0]
                except:
                    val = card.value
                space = " "
            lines[0].append("┌─────────┐")
            lines[1].append(f"│{val}{space}       │")
            lines[2].append("│         │")
            lines[3].append("│         │")
            lines[4].append(f"│    {suits[card.suit]}    │")
            lines[5].append("│         │")
            lines[6].append("│         │")
            lines[7].append(f"│       {val}{space}│")
            lines[8].append("└─────────┘")

        lines[4].append(f" Value: {self.get_value()}, Bet: {self._bet}")
        lines[0].append(f" =-=-=-= {self._name} =-=-=-=")

        result = ["".join(line) for line in lines]

        return("\n".join(result) + "\n")

    def get_value(self):
        value = 0
        for card in self._cards:
            try:
                value += card.value
            except:
                if card.value in "QueenKingJack":
                    value += 10
                elif value > 10:
                    value += 1
                else:
                    value += 11
        return value
