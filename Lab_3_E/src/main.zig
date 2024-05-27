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

pub fn main() !void {
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // Демонстрація value type
    var original_instance = ExampleObject{ .value = 0 };
    var changed_value_type = change_by_value_type(original_instance);

    try stdout.print("Original value after value type change: {}\n", .{original_instance.value}); // Output: 0
    try stdout.print("Changed value type: {}\n", .{changed_value_type.value}); // Output: 10

    // Демонстрація reference type
    change_by_reference_type(&original_instance);
    try stdout.print("Original value after reference type change: {}\n", .{original_instance.value}); // Output: 10

    try bw.flush(); // Змиваємось :3

    // Для правильної компіляції потрібно обов'язково змінити усі змінні :/
    original_instance = ExampleObject{ .value = 0 };
    changed_value_type = ExampleObject{ .value = 0 };
}
