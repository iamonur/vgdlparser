# vgdlparser

This is a parser for vgdl rule sets and finally it generates a state chart from them.
What to expect from these charts?

- They are based on user avatar stages
- Points are not important

# What I have done so far

Now I can parse vgdl strings, given a character type I can generate its states and state transitions of it.

# My initial design
- What it is
It was to generate statecharts for only the avatar, seeing any impossible transition would kill the validity of the game.
- Where it comes short
This is a mistake that cannot easily done. Most probably, this program would never find any mistakes on game designs.
So, I'm trying to improve it nowadays.

# New design(Due to change)
Parse all sprites' statecharts and the initial level. Impossible interactions, impossible to see sprites are all design flaws.
The promela program will be feeded by the statecharts found and the initial positioning, vgdlparser's job will be that only.
(Maybe) impossibilities due to positioning may be reported at the future.

# TODO:

More and more.

- Parse level map to see initial spriteset in play.
- Ability to generating promela files accordingly.
- Moving the ad-hoc generated scripts to an OO program.
- Automated tests to allow refactoring, also adding unit tests and get a good coverage.
