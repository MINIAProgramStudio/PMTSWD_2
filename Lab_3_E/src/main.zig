const std = @import("std");

const ExampleObject = struct {
    value: i32,
};

fn change_by_value_type(InputObject: ExampleObject) ExampleObject {
    InputObject.value = InputObject.value + 10;
    return InputObject;
}

fn change_by_reference_type(InputObject: *ExampleObject) *ExampleObject {
    InputObject.value = InputObject.value + 10;
    return InputObject;
}

pub fn main() !void {
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // Демонстрація value type
    var value_le_originale: i32 = 123;
    var value_type: i32 = value_le_originale;
    value_type = value_type - 10;
    try stdout.print("after value type: {}\n", .{value_le_originale}); // хотів щоб виводило українською, але Zig іншої думки про це
    var reference_type: *i32 = &value_le_originale;
    reference_type.* = reference_type.* + 10;
    try stdout.print("after reference type: {}\n", .{value_le_originale});
    reference_type = &value_type; // щоб не було константою
    value_le_originale = 0; // щоб не було константою
    try bw.flush(); // за собою необхідно змивати! (:
}
