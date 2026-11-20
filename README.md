# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/verren044/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/verren044/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Tiny chess engine in 4 KB of Python — PVS + tapered eval + persistent transposition table. v3: the TT and killers persist across moves (cleared only above 200,000 entries), 100,000 nodes/move, deterministic, no clock. Trial Elo 1545 / 1191 / 876 (mean 1204) vs v2 mean 1190, 0 time losses in 18 games.

## Run it

```sh
python3 main.py
```

The engine talks to the trial env at `MAKEFUN_ENV_URL` and exits when every game is over.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vvz66fvh&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
