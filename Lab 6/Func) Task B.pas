program PowerFunction;

function Power(a: real; n: longint): real;
var
    result: real;
    i: longint;
begin
    result := 1.0;
    
    for i := 1 to n do
        result := result * a;
    
    Power := result;
end;

var
    a: real;
    n: longint;
begin
    readln(a, n);
    
    writeln(Power(a, n));
end.
