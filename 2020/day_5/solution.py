with open('input.txt', 'r') as f:
    raw_data = [line.strip() for line in f.readlines()]


class BoardingPass:
    def __init__(self, instructions):
        self.raw_instructions = instructions

        self.binary_instructions = self._decode_instruction()
        self.row = self._get_row()
        self.column = self._get_column()

    @property
    def board_number(self) -> int:
        return int(self.row*8 + self.column)

    def _get_column(self) -> int:
        return int(self.binary_instructions[7::], 2)

    def _get_row(self) -> int:
        return int(self.binary_instructions[0:7], 2)

    def _decode_instruction(self) -> str:
        d = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}

        instructions = self.raw_instructions
        for key, value in d.items():
            instructions = instructions.replace(key, value)

        return instructions


if __name__ == '__main__':
    board_cards = set()
    rows = set()
    columns = set()

    for data in raw_data:
        passenger = BoardingPass(instructions=data)
        row, column, board_id = passenger.row, passenger.column, passenger.board_number
        # print(passenger.instructions, row, column)
        rows.add(row)
        columns.add(column)
        board_cards.add(board_id)

    possible_ids = {
        int(row*8 + column) for row in range(min(rows)+1, max(rows)-1) for column in range(min(columns), max(columns))
    }

    print(f'\nMaximum value is {max(board_cards)}')
    print(f'The only remaining sits are {possible_ids - board_cards}')
