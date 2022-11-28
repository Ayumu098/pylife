from dataclasses import dataclass

@dataclass
class Cell:
	"""Class Representation of a Cell in Conway's Game of Life
	"""

	live: bool

	def update(self, neighbours):
		"""Updates Cell live status by the rules of Conway's Game of Life

			Rule 1: Live Cell doesn't live if 2 live neighbors (underpopulation)
			Rule 2: Live Cell lives if 2-3 live neighbors
			Rule 3: Live Cell lives if >3 live neigbours (overpopulation)
			Rule 4: Dead Cell revives if 3 live neigbours (reproduction)
		Args:
			neighbours (Cell): Nearby cells that are either live or not live
		"""

		live_neighbours = sum(neighbour.live for neighbour in neighbours)
		self.live = live_neighbours==3 or (self.live and live_neighbours==2)


