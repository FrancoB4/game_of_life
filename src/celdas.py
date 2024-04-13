class Cell:
    """A class that represent a live or dead cell, if the environment is propitious, the cell live or survive, if not
    the cell will die.

    Args:
        pos (tuple): The position of the cell in a plane.
        uid (str):  The parsed as string position of the cell.
        size (float | int):

    Attributes:
        pos (tuple): The position of the cell in a plane.
        uid (str):  The parsed as string position of the
    cell.
    """

    def __init__(self, pos: tuple[int, int], uid: str, size: float | int = 3) -> None:
        self.environment = None
        self.uid = uid
        self.pos = (pos[0], pos[1])
        self.size = size
        self.live = False
        self.last_state = False
        self.live_neighbour = 0

    def change_state(self):
        if self.live:
            self.live = False
        else:
            self.live = True

    def awake(self):
        self.live = True
        self.last_state = True  # This value changes one time per main iteration

    def actualize_last_state(self):
        """Actualizate the last_state to a new value.

        Last state is an attribute that save the state of a cell in the last main iteration, so if a cell changes
        its state, the environments that content it can access to the useful state and not the dynamic one.
        """
        self.last_state = self.live

    def set_environment(self, mesh):
        self.environment = []
        for i in range(-1, 2):
            for k in range(-1, 2):
                try:
                    if not (i == 0 and k == 0):
                        self.environment.append(
                            mesh[str((self.pos[0] + i, self.pos[1] + k))])
                except KeyError:
                    continue

        self.environment = tuple(set(self.environment))

    def check_environment(self):
        self.live_neighbour = 0
        for neighbour in self.environment:
            if neighbour.last_state:
                # We use last_state because live is changing during the iteration, last state changes for all the
                # Cells at the end of the iteration
                self.live_neighbour += 1

        if self.live:
            if self.live_neighbour > 3 or self.live_neighbour < 2:
                self.change_state()
        elif self.live_neighbour == 3:
            self.change_state()
