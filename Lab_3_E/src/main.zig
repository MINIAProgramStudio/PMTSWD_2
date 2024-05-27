const std = @import("std");

const ExampleObject = struct {
    value: i32,
};

fn change_by_value_type(input_object: ExampleObject) ExampleObject {
    var temp_object = input_object;
    temp_object.value += 10;
    return temp_object;
}

fn change_by_reference_type(input_object: *ExampleObject) void {
    input_object.value += 10;
}

fn create_on_heap(allocator: *std.mem.Allocator) !*ExampleObject {
    const instance = try allocator.create(ExampleObject);
    instance.* = ExampleObject{ .value = 0 };
    return instance;
}

fn create_on_stack() ExampleObject {
    return ExampleObject{ .value = 0 };
}

test "test change_by_value_type" {
    const original_instance = ExampleObject{ .value = 0 };
    const changed_instance = change_by_value_type(original_instance);
    try std.testing.expectEqual(original_instance.value, 0); // оригінальне значення не має змінитись
    try std.testing.expectEqual(changed_instance.value, 10); // побічне значення має змінитись на 10
}

test "test change_by_reference_type" {
    var original_instance = ExampleObject{ .value = 0 };
    change_by_reference_type(&original_instance);
    try std.testing.expectEqual(original_instance.value, 10); // оригінальне значення має змінитись на 10
}

test "test create_on_heap" {
    var allocator = std.heap.page_allocator;
    const heap_instance = try create_on_heap(&allocator);
    defer allocator.destroy(heap_instance);
    try std.testing.expectEqual(heap_instance.value, 0); // об'єкт на хіпі має бути ініціалізований із значенням 0
}

test "test create_on_stack" {
    var stack_instance = create_on_stack();
    try std.testing.expectEqual(stack_instance.value, 0); // об'єкт на стеку має бути ініціалізований із значенням 0
    stack_instance = create_on_stack; // Тому що що? Правильно! Не можна створити змінну і її не змінити у явному для компілятора вигляді
}

pub fn main() !void {
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();
    var allocator = std.heap.page_allocator;

    // Створюємо ExampleObject на стеку
    var stack_instance = create_on_stack();

    // Створюємо ExampleObject на хіпі
    const heap_instance = try create_on_heap(&allocator);

    // Використовуємо ExampleObject на стеку для демонстрації value type

    var changed_value_type = change_by_value_type(stack_instance);
    try stdout.print("Stack instance value after value type change: {}\n", .{stack_instance.value}); // Чомусь воно не вміє в кирилицю :(
    try stdout.print("Changed value type: {}\n", .{changed_value_type.value});

    // Використовуємо об'єкт на стеку для демонстрації reference type

    // Використовуємо об'єкт на хіпі для демонстрації reference type
    change_by_reference_type(&stack_instance);
    change_by_reference_type(heap_instance);
    try stdout.print("Stack instance value after reference type change: {}\n", .{stack_instance.value});
    try stdout.print("Heap instance value after reference type change: {}\n", .{heap_instance.value});
    // Вивід результатів

    try bw.flush();

    // Зона Чистого четверга
    stack_instance = create_on_stack();
    changed_value_type = change_by_value_type(stack_instance);
    allocator.destroy(heap_instance);
}
