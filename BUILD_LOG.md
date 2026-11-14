# BUILD_LOG — tiny-chess-01 v2

v1 (REJECTED): 4,063 B, 0x88 negamax depth 3 + quiescence, formula PST,
MVV-LVA, 50k nodes/move. Practice Elo 871 (floor 1154).

## v2 vs v1

- Iterative deepening 1-6, per-move node budget 100k (v1 reset per depth).
- TT (Zobrist), single killer/ply, null-move pruning, LMR, PVS,
  aspiration +-150, check extension (depth<=2), futility (depth<=2).
- Quiescence: captures only, all legal moves when in check.
- Eval: incremental tapered mg/eg formula PSTs + bishop pair + pawn
  structure (doubled/isolated/passed, rook on open file; king shield and
  QS delta pruning dropped to fit the cap). Structure is computed by a
  board scan inside the eval, not incremental masks.
- main.py is a compressed payload: golfed source (7,225 B) LZMA + base85,
  exec'd at import. Two-file snapshot rejected: kit rules forbid reading
  any file besides main.py to get round the size rule.

## Trials (kit scorer)

| variant | Elo | W/D/L | gauntlet |
|---|---|---|---|
| trial-0 (old eval, per-depth 100k) | 1087 | 1/2/5 | trial-0 |
| trial-0b (per-depth 130k) | 871 | 0/2/6 | trial-0 |
| trial-0c (+structure eval) | 1087 | 2/0/6 | trial-0 |
| trial-0d (per-move 100k + futility + ext) | 1173 | 2/1/5 | trial-0 |
| trial-1 (trial-0d, fresh gauntlet) | 1396 | 4/0/4 | trial-1 |
| trial-0s (PACKED, no structure eval) | 989 | 1/1/6 | trial-0 |
| trial-0t (PACKED, structure via scan) | 1464 | 4/1/3 | trial-0 |

Note: dropping structure cost ~184 Elo (1173 vs 989), so it was
restored in scan form.

## Final

- main.py 4,033 B (cap 4,096). Snapshot ~8,100 B (cap 8,192).
- perft ALL OK (6 positions). Determinism: two runs byte-identical.
- Dev source: `~/workspace/makefun/devtools-tiny-chess/engine_g.py`
  (7,225 B); readable `engine_v2.py`. Trials in
  `~/workspace/makefun/trials/tiny-chess-01-v2/`.
