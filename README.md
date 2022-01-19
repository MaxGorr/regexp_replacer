# Idea

Sometimes it is necessary to process a set of text files with regular
expressions. Also it is convenient to keep them for repeating tasks. There are
a lot of old good tools like **awk** or **sed**. But this one:

- is very simple,
- uses Python's regular expressions.

## Usage

Apply rules for concrete file:

```bash
python -m regexp_replacer -r special.rules -f edited.file
```

Pipe usage:

```bash
cat some_file | python -m regexp_replacer -r some.rules -s | another_command
```

## Rules

Line for pattern regexp:

```plain
p: python_regex_pattern
```

Line for replacement regexp:

```plain
r: some_replacement
```

It is possible to split long regexps:

```plain
:: very very very
:: very very very
:: very very very
p: long regexp
```

To load another rules file from the current one:

```plain
>> another_file.rules
```

To interrupt current file loading use this command:

```plain
p: pattern
r: replacement

x:

p: ignored_pattern
r: ignored_replacement
```

Other lines are ignored, therefore it is possible to use them as documentation:

```plain
## ignored
// also ignored
This line will not be processed
/*!
 * Another way of documentation
 */
-- And so on...
```

One more tip: to perform rules as Markdown files is a good idea. It increases
their readability in the repository's web-interfaces.
