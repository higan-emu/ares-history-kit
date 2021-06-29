ares-history-kit
================

In July 2020,
Near retired from the emulation scene,
leaving behind a collection of [snapshots](./archives/)
and [changelogs](./changes/)
for his emulator "ares",
which was a fork and continuation of his previous emulator,
[higan](https://github.com/higan-emu/higan).

I wrote this collection of scripts
to import those changes back into higan.

After his untimely death,
ares development had proceeded much further.
I added the later snapshots and changelogs I was able to find
in the hope that ares development could be continued in Near's memory.

Before you start
================

To run these scripts, you'll need:

  - A POSIXy operating system
  - A version of `tar` that supports and auto-detects `.xz` compression
  - A copy of the `unzip` command
  - A copy of the `awk` command
  - A copy of Python 3.5 or higher
  - A copy of [apenwarr/redo](https://github.com/apenwarr/redo/)
  - A copy of [Git](https://git-scm.com/)
    and specifically the `git fast-import` tool
  - A copy of [the higan git repository](https://github.com/higan-emu/higan)

Usage
=====

By the time you read this,
ares' history should already be recorded in an official repo.
Nevertheless:

 1. Clone this repository
 2. Extract the changelogs and archive metadata by running:
 
        redo prepare

 3. Clone the higan repository to make a new ares repository:

        git clone https://github.com/higan-emu/higan path/to/ares
        cd path/to/ares

 4. In the ares-repo-to-be, remove the tags pointing to
    history that will be replaced by new ares history:

        git tag -d v111
        git tag -d v112
        git tag -d v113
        git tag -d v114
        git tag -d v115

 5. Import the ares history:
 
        path/to/ares-history-kit/ares-fast-export | git fast-import

 6. The repo should now have an "ares" branch,
    based off the v110 tag,
    containing ares' development history.
    Replace higan's master branch with the new ares branch:

        git switch ares
        git branch -M master
