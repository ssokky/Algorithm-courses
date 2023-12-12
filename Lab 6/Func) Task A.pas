program MinFunction;

function Min(a, b, c, d: integer): integer;
var
    min_value: integer;
begin
    min_value := a;
    
    if b < min_value then
        min_value := b;
    
    if c < min_value then
        min_value := c;
    
    if d < min_value then
        min_value := d;
    
    Min := min_value;
end;

var
    a, b, c, d: integer;
begin
    readln(a, b, c, d);
    
    writeln(Min(a, b, c, d));
end.
