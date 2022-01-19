# Code style rules

## Getter/setter for position

```plain
p: \s*\.\s*position\s*=\s*(.*?);
r: ->setPosition(\1);

p: \s*\.\s*position
r: ->getPosition()
```

## children method

```plain
p: ->children\(\)
r: ->getChildren()
```

## for-cycle

Example:

```cpp
// from
for (SomeClass *cls in container->call(smth)) {

// to
CCObject * obj = nullptr;
_FOREACH_(container->call(smth), obj) {
SomeClass *cls = (SomeClass *)obj;
```

Rule:

```plain
:: for\s*\(
:: (\w+(?:\s*\*)+)\s*
:: (\w+)\s+in\s*
p: (.*?)\)(\s*{)

:: CCObject * obj = nullptr;\n
:: _FOREACH_(\3, obj)\4\n
r: \1 \2 = (\1)obj;\n
```
