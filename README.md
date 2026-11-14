# tiny-chess-01 v2

Chess engine, Python 3.13 stdlib only, single file `main.py` (4,033 bytes,
cap 4,096). Deterministic: fixed 100,000-node budget per move, no clock,
no network, no model calls. No book, tablebase, or precomputed dictionary.

## Engine

- 0x88 board, negamax + alpha-beta, iterative deepening 1-6.
- TT (Zobrist), single killer/ply, null-move pruning, LMR, PVS,
  aspiration windows (+-150), check extension (depth<=2), futility (depth<=2).
- Quiescence: captures only (all legal moves when in check).
- Eval: incremental tapered mg/eg formula PSTs + bishop pair + pawn
  structure (doubled/isolated/passed, rook on open file). Structure is
  computed by a board scan inside the eval (no incremental masks), which
  keeps the code small enough to fit the cap.

## Files

- `main.py` — the entry: golfed engine source (7,225 B) LZMA-compressed
  (FORMAT_ALONE, lc=0/lp=0/pb=0) + base85, exec'd at import.
- `README.md`, `LICENSE` (MIT), `BUILD_LOG.md`, `.makefun/owner.json`.

## Validation

- perft OK on the 6 standard positions. Determinism: two runs byte-identical.
- Practice trial (kit scorer) — see BUILD_LOG.md.
