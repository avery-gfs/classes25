// const board = [
//   [0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 3, 0, 8, 5],
//   [0, 0, 1, 0, 2, 0, 0, 0, 0],
//   [0, 0, 0, 5, 0, 7, 0, 0, 0],
//   [0, 0, 4, 0, 0, 0, 1, 0, 0],
//   [0, 9, 0, 0, 0, 0, 0, 0, 0],
//   [5, 0, 0, 0, 0, 0, 0, 7, 3],
//   [0, 0, 2, 0, 1, 0, 0, 0, 0],
//   [0, 0, 0, 0, 4, 0, 0, 0, 9],
// ];

// const board = [
//   [5, 3, 0, 0, 7, 0, 0, 0, 0],
//   [6, 0, 0, 1, 9, 5, 0, 0, 0],
//   [0, 9, 8, 0, 0, 0, 0, 6, 0],
//   [8, 0, 0, 0, 6, 0, 0, 0, 3],
//   [4, 0, 0, 8, 0, 3, 0, 0, 1],
//   [7, 0, 0, 0, 2, 0, 0, 0, 6],
//   [0, 6, 0, 0, 0, 0, 2, 8, 0],
//   [0, 0, 0, 4, 1, 9, 0, 0, 5],
//   [0, 0, 0, 0, 8, 0, 0, 7, 9],
// ];

const board = [
  [0, 4, 0, 0, 2, 0, 8, 6, 5],
  [7, 0, 0, 6, 0, 8, 0, 0, 0],
  [1, 0, 0, 0, 0, 4, 7, 0, 2],
  [0, 1, 8, 7, 4, 0, 0, 0, 0],
  [0, 0, 5, 2, 0, 9, 6, 0, 0],
  [0, 0, 0, 0, 8, 6, 1, 5, 0],
  [9, 0, 1, 5, 0, 0, 0, 0, 6],
  [0, 0, 0, 8, 0, 2, 0, 0, 7],
  [8, 7, 3, 0, 6, 0, 0, 2, 0],
];

const rows = [
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
];

const cols = [
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
  new Set(),
];

const blocks = [
  [new Set(), new Set(), new Set()],
  [new Set(), new Set(), new Set()],
  [new Set(), new Set(), new Set()],
];

for (let r = 0; r < 9; r++) {
  for (let c = 0; c < 9; c++) {
    const n = board[r][c];
    const br = Math.floor(r / 3);
    const bc = Math.floor(c / 3);

    if (n > 0) {
      rows[r].add(n);
      cols[c].add(n);
      blocks[br][bc].add(n);
    }
  }
}

function solve(r, c) {
  if (c == 9) {
    c = 0;
    r += 1;
  }

  if (r == 9) {
    return true;
  }

  if (board[r][c] > 0) {
    return solve(r, c + 1);
  }

  const br = Math.floor(r / 3);
  const bc = Math.floor(c / 3);

  for (let n = 1; n <= 9; n++) {
    if (!rows[r].has(n) && !cols[c].has(n) && !blocks[br][bc].has(n)) {
      board[r][c] = n;
      rows[r].add(n);
      cols[c].add(n);
      blocks[br][bc].add(n);

      show(board);
      if (solve(r, c + 1)) {
        return true;
      }

      board[r][c] = 0;
      rows[r].delete(n);
      cols[c].delete(n);
      blocks[br][bc].delete(n);
    }
  }

  return false;
}

function showRow(row) {
  const disp = row.map((x) => (x ? x : " "));
  return `${disp[0]} ${disp[1]} ${disp[2]} | ${disp[3]} ${disp[4]} ${disp[5]} | ${disp[6]} ${disp[7]} ${disp[8]}`;
}

function show(board) {
  console.clear();
  const display = board.map(showRow);

  console.log(
    [0, 3, 6]
      .map((i) => display.slice(i, i + 3).join("\n"))
      .join("\n------+-------+------\n"),
  );
}

solve(0, 0);
show(board);
