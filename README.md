# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/KanekiCraynet/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/KanekiCraynet/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Alpha-beta search with iterative deepening, transposition table, MVV-LVA move ordering, killer moves, and piece-square tables. 3386 bytes.

## Engine

- Iterative deepening up to depth 20 (node budget 50k)
- Alpha-beta with null-move style pruning
- Transposition table + killer moves for ordering
- MVV-LVA capture ordering
- Evaluation: material + piece-square tables (pawns, knights, bishops)
- Time management via node counting

## Local test

```bash
makefun grade-local --kit . --bot . --driver docker
```

## License

MIT (SPDX-License-Identifier: MIT)