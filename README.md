# tiny-chess-01 entry

[![make.fun](https://img.shields.io/badge/make.fun-tiny--chess--01-blue)](https://make.fun/c/tiny-chess-01)
[![status](https://img.shields.io/badge/status-competing-orange)](https://make.fun/c/tiny-chess-01/leaderboard)

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