# Sample file with rules

## Method fix

Example:

```cpp
// from
-(void) method

// to
void __CLASS__::method()
```

Rule:

```plain
p: -\((.*?)\)\s+(\w*)
r: \1 __CLASS__::\2()
```

## String rules

Example:

```cpp
// from
@"Format string example: %@"

// to
"Format string example: %s"
```

Rules:

```plain
p: %@
r: %s

p: @"
r: "
```

## Simple rules

```plain
p: @(implementation|end)
r: //@\1

p: NASMutableArray
r: CCArray

p: self
r: this

p: NS
r: CC

p: #import
r: #include
```

## init-method patch

Load rules from other files:

```plain
>> additional_1.md
>> additional_2.md
```

## Forced exit and unused rules

Exit here:

```plain
x:
```

Remained rules are ignored:

```plain
p: for
r: FOREACH

p: //
r: /*

>> non_existent_file.rules
```
