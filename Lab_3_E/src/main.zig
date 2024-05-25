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
    const original_instance = ExampleObject{ .value = 0 };
    change_by_value_type(original_instance);

    try stdout.print("{}\n", .{original_instance.value}); // хотів щоб виводило українською, але Zig іншої думки про це

    original_instance.deinit()
    try bw.flush(); // за собою необхідно змивати! (:
}
