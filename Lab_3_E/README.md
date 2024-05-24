# Лабораторна робота 3-Є.
## Memory (stack/heap), garbage collection, passing arguments by value/by reference, unit-tests.
### Варіант -- 2; мова програмування -- Zig.
### Дослідити чи є в даній мові програмвання концепції value types, reference types та garbage collector
Zig має reference та value types, але не має garbage collector. Управління пам'яттю повністю віддається в руки розробника.
### Продемонструвати, що екземпляри reference type дійсно передаються за посиланням, а value types - за значеннями
#### Демонстрація передачі за значенням:
1. Створимо оригінальну змінну value_le_oridginale.
1. Передамо її значення як value type до змінної value_type
1. Змінимо value_type
1. Виведемо значення value_le_oridginale у консоль. Як бачимо вона не змінилась