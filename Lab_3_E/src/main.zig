const std = @import("std");

const ExampleObject = struct {
    value: i32,
};

fn change_by_value_type(input_object: ExampleObject) ExampleObject {
    var temp_object = input_object;
    temp_object.value = temp_object.value + 10;
    return temp_object;
}

fn change_by_reference_type(input_object: *ExampleObject) *ExampleObject {
    input_object.value += 10;
}

pub fn main() !void {
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // Демонстрація value type
    var original_instance = ExampleObject{ .value = 0 };
    var changed_value_type = change_by_value_type(original_instance);

    try stdout.print("{}\n", .{original_instance.value}); // хотів щоб виводило українською, але Zig іншої думки про це
    try stdout.print("{}\n", .{changed_value_type.value});
    try bw.flush(); // за собою необхідно змивати! (:

    // я не знаю чому, але це потрібно щоб воно компілювалось :/
    original_instance = ExampleObject{ .value = 0 };
    changed_value_type = ExampleObject{ .value = 0 };
}
