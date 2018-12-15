# Code style rules

## Getter/setter for position
```
p: \s*\.\s*position\s*=\s*(.*?);
r: ->setPosition(\1);

p: \s*\.\s*position
r: ->getPosition()
```

## children method
```
p: ->children\(\)
r: ->getChildren()
```

## for-cycle

Example:
```
// from
for (SomeClass *cls in cnt->call(smth)) {

// to
CCObject * obj = nullptr;
_FOREACH_(cnt->call(smth), obj) {
SomeClass *cls = (SomeClass *)obj;
```

Rule:
```
:: for\s*\(
:: (\w+(?:\s*\*)+)\s*
:: (\w+)\s+in\s*
p: (.*?)\)(\s*{)

:: CCObject * obj = nullptr;\n
:: _FOREACH_(\3, obj)\4\n
r: \1 \2 = (\1)obj;\n
```
