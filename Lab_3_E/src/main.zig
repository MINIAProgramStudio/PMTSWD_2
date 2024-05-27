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

pub fn main() !void {
    var allocator = std.heap.page_allocator;
    // Створюємо ExampleObject на стеку
    var stack_instance = create_on_stack();

    // Створюємо ExampleObject на хіпі
    const heap_instance = try create_on_heap(&allocator);

    // Використовуємо ExampleObject на стеку для демонстрації value type
    const changed_value_type = change_by_value_type(stack_instance);

    // Використовуємо об'єкт на стеку для демонстрації reference type
    change_by_reference_type(&stack_instance);

    // Використовуємо об'єкт на хіпі для демонстрації reference type
    change_by_reference_type(heap_instance);

    // Вивід результатів
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // Чомусь воно не вміє в кирилицю
    try stdout.print("Stack instance value after value type change: {}\n", .{stack_instance.value}); // Output: 10
    try stdout.print("Changed value type: {}\n", .{changed_value_type.value}); // Output: 10
    try stdout.print("Stack instance value after reference type change: {}\n", .{stack_instance.value}); // Output: 20
    try stdout.print("Heap instance value after reference type change: {}\n", .{heap_instance.value}); // Output: 10

    try bw.flush(); // Не забуваємо змивати за собою :3

    // Зона Чистого четверга
    allocator.destroy(heap_instance);
}
