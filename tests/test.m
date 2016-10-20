#import "SomeHeaderFile.h"

CCObject * SomeClass::init()
{
    if ((this = __SUPER_CLASS__::init()))
    {
        some_operations();
    }
    return self;
}

@implementation MyClass

-(void) myMethod {

    NSLog(@"Start myMethod");
    
    for (int i=0; i<N; ++i) {
        objArray[i]= [[NSMutableArray array] retain];
    }

    NSString *file = [someObj getFileName];
    NSLog(@"Path to file: %@", file);

    NSString *text = [NSString stringWithContentsOfFile:file  usedEncoding: nil error: nil];

    NSArray *lines = [text componentsSeparatedByString:@"\n"];

    // and so on..
}

@end
