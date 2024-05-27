## Memory (stack/heap), garbage collection, passing arguments by value/by reference, unit-tests.
### Варіант -- 2; мова програмування -- Zig.
### Дослідити чи є в даній мові програмвання концепції value types, reference types та garbage collector
Zig має reference та value types, але не має garbage collector. Управління пам'яттю повністю віддається в руки розробника. Тим не менш локальні змінні видаляються після завершення локального процесу, а глобальні -- після завершення програми.
### Демонстрація value/reference types та stack/heap
Див. код :3
