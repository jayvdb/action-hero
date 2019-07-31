[action_heroes_logo]: ./logo.svg
![Action Heroes Logo][action_heroes_logo]


![Build Status](https://camo.githubusercontent.com/550782da80dba216452e4f747237c0fee66e8510/68747470733a2f2f696d672e736869656c64732e696f2f636f766572616c6c732f636f766572616c6c732d636c69656e74732f636f766572616c6c732d707974686f6e2f6d61737465722e7376673f7374796c653d666c61742d737175617265)
![Python Version Support](https://camo.githubusercontent.com/718b0c250361d97af792b64d7499ea616a637acd/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f7079746573742d636f762e737667)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![LICENSE MIT](https://img.shields.io/github/license/kadimisetty/vuri)
![Build Status](https://camo.githubusercontent.com/2dcdb388c206e4e3776ba9c61bbb1086160c3413/68747470733a2f2f7472617669732d63692e6f72672f736561746765656b2f66757a7a7977757a7a792e7376673f6272616e63683d6d6173746572)


####

`action_heroes` is a python package that provides a bunch of   
__custom argparse _Actions_ to help you write command line interfaces.__


## Introduction
>  Jump to — __[Introduction](#introduction)__ · [Quick Usage](#quick-usage) · [Help & FAQ](#help-and-faq) · [FAQ](#faq) · [Catalog](#catalog) · [Development](#development)

##### 🤷‍♂️ Argparse, Parsers, Actions ? What now ??

<dl>

<dt>1. argparse</dt>
<dd><code>argparse</code> is a python module, in the python standard library, used to build command line interfaces that accept user arguments.
<a href="https://docs.python.org/3/library/argparse.html">⚓︎</a>
</dd>

<dt>2. ArgumentParser</dt>
<dd><code>argparse.ArgumentParser</code> parses user arguments by inspecting the command line, converting each argument to an appropriate type and finally invoking an appropriate <code>argparse.Action</code>
<a href="https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser">⚓︎</a>
</dd>


<dt>3. Action</dt>
<dd><code>argparse.Action</code> objects are used by <code>ArgumentParser</code> to represent information needed to parse arguments from the command line.
<a href="https://docs.python.org/3/library/argparse.html#action">⚓︎</a>
</dd>


<dt>4. action_heroes 💥</dt>
<dd><code>argparse.Action</code> objects are subclassable, to allow custom actions. This library, <code>action_heroes</code>, include many such custom actions that will prove their worth when dealing with accepting user arguments in your command line application.</dd>

<dd>For example, the <strong><code>FileIsWritableAction</code> automatically verifies that all file paths accepted as arguments are indeed writable.</strong> This saves you the trouble of coding that check yourself. Nice, no? <a href="#catalog">Browse the catalog</a> for more custom actions.</dd>

</dl>

> Hey! If you like action heroes could you give it a quick __star__ ⭐️   
> I put a lot of effort into this and each lil' star brightens my day


## Quick Usage
>  Jump to — [Introduction](#introduction) · __[Quick Usage](#quick-usage)__ · [Help & FAQ](#help-and-faq) · [FAQ](#faq) · [Catalog](#catalog) · [Development](#development)

- Use `pip` to install `action_heroes` 


```python
pip install action_heroes
```


## Help & FAQ
>  Jump to — [Introduction](#introduction) · [Quick Usage](#quick-usage) · __[Help & FAQ](#help-and-faq)__ · [FAQ](#faq) · [Catalog](#catalog) · [Development](#development)

### FAQ
<dl>
<dt>There was no mention of humans! Is this work for humans?</dt>
<dd>Yes, yes it does work for humans trademark.</dd>

<dt>What do I need to know to use `action_heroes` in my command line application?</dt>
<dd>Vanilla `argparse` knowledge is all you should need.</dd>

<dt>What form do user argument exceptions show themeselves as?</dt>
<dd>`argparse.ArgumentError{"helpful error message"}`</dd>

<dt>Is `action_heroes` tied to the `argparse` module?</dt>
<dd>Technically no. Any project that has a can use `argpoarse.Action` should be able to use it. Do watch for the exception type `argparse.ArgumentError`.</dd>

<dt>I don't want to learn another library. I already know `argparse.ArgumentParser`!</dt>
<dd>Great! You know all the concepts then. `action_heroes` can pretty much just be used like any other `argparse.Action`.</dd>

<dt>Who are you?</dt>
<dd>Hi! Nice to meet you, my name is Sri Kadimisetty.</dd>
</dl>


## Catalog
>  Jump to — [Introduction](#introduction) · [Quick Usage](#quick-usage) · [Help & FAQ](#help-and-faq) · [FAQ](#faq) · __[Catalog](#catalog)__ · [Development](#development)


## Development
>  Jump to — [Introduction](#introduction) · [Quick Usage](#quick-usage) · [Help & FAQ](#help-and-faq) · [FAQ](#faq) · [Catalog](#catalog) · __[Development](#development)__
