// tiny-chess-01 TypeScript entry point
// SPDX-License-Identifier: MIT

import { spawn } from "node:child_process";

const python = spawn("python3", ["main.py"], { stdio: "inherit" });
python.on("exit", (code) => process.exit(code ?? 1));