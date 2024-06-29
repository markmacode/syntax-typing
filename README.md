# Data for training your syntax typing

I have switched to using the [Glove 80](https://www.moergo.com/), and part of
that change required getting used to many things on the keyboard. This repo
holds data sets for [MonkeyType](https://monkeytype.com/) which will help you
gain muscle memory for typing various patterns while coding.

## Usage

I'll get back to this

## Why?

Going to a new keyboard design, keymap, or just getting started with taking your
typing speed and accuracy seriously; there will be a few issues to overcome. For
me in particular I created a symbol layer on my keyboard, which is a whole new
way of processing what keys to type. Beyond the use of the shift key for
capitalising letters and also getting alternative symbols, I want to exclusively
use a new Symbol layer key to access any symbol that isn't on the base layer of
the keyboard. So now I have to learn:

- Using the Shift key with the thumbs.
- Accessing many of the most common symbols in very different locations.
- Alternating between the Symbol layer and the 'Shifted' layer (especially when
  coding).

MonkeyType already has 'languages' for many programming languages, but the data
they provide does not actually help in typing patterns that include symbols.
Their data provides keywords and common 'vocabulary' when coding in a language,
but the don't provide many symbols. Test this out by typing *"we are very fast
at some things"* compared to *"ah eot gsvy rrea ei msen satwft"* -- you are
going to be much more accurate and possible much faster at typing the words you
are familiar with. I have never typed symbol patterns as fast as I type words
I'm used to, and my accuracy on symbols is poor, I want this to change.

So this repo will provide data sets that make sense for what you will actually
be typing in real code. In the JavaScript language on MonkeyType, it provides
something like `attributes i++ || the toLowerCase() and typeof` -- and that's me
cherry picking the parts that have symbols, symbols rarely show up in their
tests. The vocabulary of the common functions and keywords is good, but what
about the addition of some of the most common symbol patterns too:
`const helloWorld = () => {}` `for (item in arr) {}`
`const fooBar = myObject.someFunction();`
`if (thisThing === thatThing && something < another) {}`
