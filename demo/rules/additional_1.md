# Rules for cocos2d to cocos2d-x partial conversion

## Alloc to constructor

Еxample:
```
// from
CCObject * SomeClass::alloc()
void SomeClass::dealloc()

// to
SomeClass::SomeClass()
SomeClass::~SomeClass()
```

Rules:
```
p: (?:cocos2d::)?CCObject\s*\*\s*(\w+)::alloc\(\)
r: \1::\1()

p: void\s*(\w+)::dealloc\(\)
r: \1::~\1()

p: (__SUPER_CLASS__::(de)?alloc\(\))
r: //\1
```

## init-method fix

Example:
```
// from
CCObject * SomeClass::init()
{
    if ((this = __SUPER_CLASS__::init()))
    {
        some_operations();
    }
    return this;
}

// to
bool SomeClass::init()
{
   if (__SUPER_CLASS__::init())
   {
       some_operations();
       return true;
   }
   return false;
}
```

Rule:
```
:: (?:cocos2d::)?CCObject\s*\*\s*
:: ([a-zA-Z_]\w*)::init\(\)
:: (\s*\{\s*)
:: if\s*\(+this\s*=\s*__SUPER_CLASS__::init\(\)\)+
:: (\s*\{\s*(?:\n|.)*?)
p: \}\s*return this;(\s*\})
r: bool \1::init()\2if (__SUPER_CLASS__::init())\3return true;}\nreturn false;\4
```


## alloc + init method fix

Example:
```
// from
SomeClass *object = SomeClass::alloc()->init()

// to
SomeClass *object = SomeClass::create()
```

Rule:
```
:: (\w*)(\s*\*)+\s*(\w*)
p: \s*=\s*\1::alloc\(\)->init\(\)
r: \1 2\3 = \1::create()
```

## autorelease/retain fix

Example:
```
// from
SomeClass *object = SomeClass::createWithArgs(a, b)->autorelease()

// to
SomeClass *object = SomeClass::createWithArgs(a, b);
object->autorelease()
```

Rule:
```
:: (\w*)(\s*\*)+\s*(\w*)
p: \s*=\s*(.*?)(->(?:autorelease|retian)\(\))
r: \1 \2\3 = \4;\n\3\5
```