import random

racers = (
    ("<:9r:892051492570300529>", "fast"),
    # ("<:8r:892051447120797737>", "fast"),
    # ("<:7r:892051446743318578>", "fast"),
    ("<:6r:892051334491172865>", "slow"),
    ("<:5r:892051304560594984>", "fast"),
    ("<:4r:892051089782898718>", "fast"),
    ("<:3r:892051026549542932>", "fast"),
    # ("<:34r:892055060962504816>", "fast"),
    # ("<:33r:892055007229255691>", "steady"),
    # ("<:32r:892054903017582613>", "steady"),
    # ("<:31r:892054733076987955>", "steady"),
    # ("<:30r:892054626537463850>", "steady"),
    ("<:2r:892050921436094524>", "steady"),
    ("<:29r:892054517259042848>", "abberant"),
    ("<:28r:892054275293855825>", "abberant"),
    ("<:27r:892054205030867034>", "abberant"),
    # ("<:26r:892054099850313800>", "abberant"),
    # ("<:25r:892053862268153940>", "abberant"),
    # ("<:24r:892053743707783168>", "abberant"),
    # ("<:24r:892053597154594896>", "abberant"),
    ("<:23r:892053470541135942>", "predator"),
    ("<:22r:892053070131900437>", "predator"),
    ("<:21r:892052968990470205>", "special"),
    ("<:20r:892052539590201415>", "special"),
    ("<:1r:892050863735070770>", "slow"),
    ("<:19r:892052466496049183>", "slow"),
    ("<:18r:892052184286519367>", "slow"),
    # ("<:17r:892052143807275068>", "slow"),
    # ("<:16r:892052062362292344>", "slow"),
    # ("<:15r:892051995995832340>", "slow"),
    # ("<:14r:892051950420504637>", "slow"),
    # ("<:14r:892051786364493854>", "slow"),
    # ("<:13r:892051709474529320>", "slow"),
    # ("<:11r:892051598707159040>", "slow"),
)


class Animal:
    def __init__(self, emoji, _type):
        self.emoji = emoji
        self._type = _type
        self.track = "•   " * 20
        self.position = 80
        self.turn = 0
        self.current = self.track + self.emoji

    def move(self):
        self._update_postion()
        self.turn += 1
        return self.current

    def _update_postion(self):
        distance = self._calculate_movement()
        self.current = "".join(
            (
                self.track[: max(0, self.position - distance)],
                self.emoji,
                self.track[max(0, self.position - distance) :],
            )
        )
        self.position = self._get_position()

    def _get_position(self):
        return self.current.find(self.emoji)

    def _calculate_movement(self):
        if self._type == "slow":
            return random.randint(1, 3) * 3
        elif self._type == "fast":
            return random.randint(0, 4) * 3

        elif self._type == "steady":
            return 2 * 3

        elif self._type == "abberant":
            if random.randint(1, 100) >= 90:
                return 5 * 3
            else:
                return random.randint(0, 2) * 3

        elif self._type == "predator":
            if self.turn % 2 == 0:
                return 0
            else:
                return random.randint(2, 5) * 3

        elif self._type == ":unicorn:":
            if self.turn % 3:
                return random.choice([len("blue"), len("red"), len("green")]) * 3
            else:
                return 0
        else:
            if self.turn == 1:
                return 14 * 3
            elif self.turn == 2:
                return 0
            else:
                return random.randint(0, 2) * 3
