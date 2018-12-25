# Idea

Sometimes it is necessary to process a set of text files and sometimes it is convenient to use regular expressions for this purpose. And moreover it would be convenient to store regexp sets for repeating tasks. To solve these problems it is necessary to reinvent **awk** or **sed** (_use them instead of this tool_)!

# Usage

Apply rules for concrete file:
```
python -m regexp_replacer -r special.rules -f edited.file
```

Pipe usage:
```
cat some_file | python -m regexp_replacer -r some.rules -s | another_command
```

# Rules

Line for pattern regexp:
```
p: python_regex_pattern
```

Line for replacement regexp:
```
r: some_replacement
```

It is possible to split long regexps:
```
:: very very very
:: very very very
:: very very very
p: long regexp
```

To load another rules file from the current one:
```
>> another_file.rules
```

To interrupt current file loading use this command:
```
p: pattern
r: replacement

x:

p: ignored_pattern
r: ignored_replacement
```

Other lines are ignored, therefore it is possible to use them as documentation:
```
## ignored
// also ignored
This line will not be processed
/*!
 * Another way of documentation
 */
-- And so on...
```

It is not an obligatory but sometimes convenient to perform rules as Markdown files.
