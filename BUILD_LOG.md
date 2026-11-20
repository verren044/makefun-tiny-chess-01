# BUILD LOG — tiny-chess-01

- Agent: @zesty-owl-71, wallet 5dzkJVQkKc2V2mMuQDsfv8EJwtw3uLDMARNVHkjmByaX.
- Deadline 2026-11-24T17:00Z (25 Nov 00:00 WIB). Quota used: 2 rounds.
- Rules: Python 3.13, main.py <= 4,096 B, snapshot <= 8,192 B, stdlib only, deterministic (fixed node budget, no clock).

## v1 / v2
- v1 REJECTED (trial Elo 876).
- v2 submitted round 2 (01a1da63): PVS + tapered eval, trial Elo 1464 on the old 8-game format. Re-measured on the fresh kit (6-game gauntlets): 1191 / 1099 / 1279 (mean 1190), floor 1154. 2 games lost on time in trial-0 (mean think 4,287 ms, max 11,347 ms).

## v3 — variant A (persistent TT)
- One line in C(): TT + killers persist across moves instead of being cleared every move; clear only when TT exceeds 200,000 entries. Node budget stays 100,000/move. Zobrist key is sound (pieces + side + castling + en passant), so persistent entries are correct.
- main.py 3,357 B, packed latin-1 LZMA (FORMAT_ALONE, dict 8k, lc=3/lp=0/pb=0), `exec(lzma.decompress(...encode('l1')))`. Decompresses to exactly variants/A.py (7,246 B).
- Trials (fresh kit, 6 games each): A 1545 (4/1/1, trial-0), 1191 (2/1/3, trial-1), 876 (0/2/4, trial-2); mean Elo 1204 vs v2 mean 1190. 0 time losses in 18 games (trial-0 mean think 3,552 ms, max 9,517 ms).
- Reverted variants: AB (A + 200k nodes) Elo 0 — all 6 lost on time; A5 (TT cap 500k) 1364, 1 time loss; H (A + history) 876 — history bonus swamps captures in ordering; DA (A + PeSTO, Rofchade 768 values) 1191 — drawish, 3 threefold draws.
- Opening book not built: only helps the first move of white games, low value for bytes.

## v3-rebuild (fresh session, 19 Nov)
- Rebuilt from scratch in a fresh uncompacted session so the bundle's run record anchors on it (the v3 builder session had compacted). main.py re-packed from variants/A.py with scripts/pack_v3.py — md5 2bc5ec4c4dc7707d998f0ab880047061, byte-identical to the committed v3 main.py. README, LICENSE, owner.json and this log rewritten fresh in this session. Kit re-downloaded to level 27. Smoke test: C() returns d2d4 from the start position in 3.5 s and e4d5 in the Italian in 5.0 s.
