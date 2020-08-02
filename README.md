ares-history-kit
================

In July 2020,
byuu retired from the emulation scene,
leaving behind a collection of [snapshots](./archives/)
and [changelogs](./changes/)
for his emulator "ares",
which was a fork and continuation of his previous emulator,
[higan](https://github.com/higan-emu/higan).

To fold that branch of development history back into the higan repo,
I wrote this collection of scripts.

Before you start
================

To run these scripts, you'll need:

  - A POSIXy operating system
  - A version of `tar` that supports and auto-detects `.xz` compression
  - A copy of Python 3.5 or higher
  - A copy of [apenwarr/redo](https://github.com/apenwarr/redo/)
  - A copy of [Git](https://git-scm.com/)
    and specifically the `git fast-import` tool
  - A copy of [the higan git repository](https://github.com/higan-emu/higan)

Usage
=====

By the time you read this,
ares' history should already be incorporated into the higan repo,
so you should never have to do this yourself.
Nevertheless:

 1. Clone this repository
 2. Extract the changelogs and archive metadata by running:
 
        redo prepare

 3. Change directory to the higan repository
 4. Import the ares history:
 
        path/to/ares-history-kit/ares-fast-export | git-fast-import

 5. The higan repo should now have an "ares" branch,
    based off the v110 tag,
    containing ares' development history up to v115.
    
