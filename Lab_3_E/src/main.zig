const std = @import("std");

pub fn main() !void {
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // Демонстрація value type
    var value_le_oridginale: i32 = 123;
    var value_type: i32 = value_le_oridginale;
    value_type = value_type - 10;
    try stdout.print("after value type: {}\n", .{value_le_oridginale}); // хотів щоб виводило українською, але Zig іншої думки про це
    value_le_oridginale = 0; // щоб не було константою
    try bw.flush(); // за собою необхідно змивати! (:
}
