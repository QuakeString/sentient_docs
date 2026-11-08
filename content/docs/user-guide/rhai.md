+++
title = "Script language (Rhai)"
description = "Write scripts in SENTIENT with Rhai: rule node scripts, calculated fields, alarm rule conditions and integration converters. Syntax, the values each script gets, built-in functions and common mistakes."
aliases = ["/docs/user-guide/rhai/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT runs scripts in two languages: **JavaScript** and **Rhai**. Rhai is a small scripting language that runs inside the SENTIENT server itself. It is fast, it cannot reach files or the network, and a script that runs too long is stopped instead of slowing the server down.

Where both are offered, a language switch above the script editor picks one.

| Where | Languages | What the script gets |
|---|---|---|
| Rule nodes: script filter, switch, transformation, log, generator, create and clear alarm details | JavaScript or Rhai | `msg`, `metadata`, `msgType` |
| [Calculated fields](/docs/user-guide/calculated-fields/) of type Script | Rhai | One variable per argument, plus `ctx` |
| [Alarm rules](/docs/user-guide/alarm-rules/), script conditions | Rhai | One variable per argument |
| Integration converters | JavaScript or Rhai | Uplink: `payload`, `metadata`. Downlink: `msg`, `metadata`, `msgType`, `integrationMetadata` |
| [Script reports](/docs/reports/) | Rhai | The report's arguments, plus `ctx` |

<div class="st-callout info">

Scripts written for Rhai, the expression language of other IoT platforms, work in **calculated fields** without changes: SENTIENT translates them to Rhai when they run. Rule node and converter scripts are **not** translated. An imported Rhai rule node opens with its script in the Rhai editor, and you rewrite it in Rhai syntax using the table in [Coming from Rhai or JavaScript](#coming-from-tbel-or-javascript).

</div>

## The language in five minutes

```rust
// Variables
let limit = 80;              // a value you change later
const FACTOR = 1.8;          // a value that never changes

// Numbers, text, true/false
let t = 21.5;
let name = "Pump 1";
let running = true;

// Maps (objects) and arrays
let reading = #{ temperature: 21.5, unit: "C" };
let values = [3, 1, 2];

// Read and change a map
reading.temperature = 22.0;
reading.status = "ok";       // adds a new key

// Conditions: `if` gives back a value
let level = if t > limit { "high" } else { "normal" };

// Loops
let sum = 0;
for v in values { sum += v; }

// Text with values in it
let label = `${name}: ${t} °C`;

// The last value is the result. `return` works too.
reading
```

The parts that differ from JavaScript:

- A map is written `#{ key: value }`, with a `#`. A plain `{ … }` is a block of code, not an object.
- A missing key gives `()`, Rhai's empty value. `msg.speed ?? 0` gives 0 when `speed` is missing.
- `5 / 2` is `2`: dividing two whole numbers gives a whole number. Write `5 / 2.0`, or `x.to_float() / 2`, to keep the decimals.
- Text is compared with text and numbers with numbers. `"21.5" > 20` is **false**, with no error. Turn text into a number first with `"21.5".parse_float()`.
- Every statement ends with `;`, except the last value of a block.

## Rule node scripts

The script gets the incoming message as three variables:

| Variable | Contains |
|---|---|
| `msg` | The message body as a map, for example `#{temperature: 21.5}` |
| `metadata` | The metadata as a map of text values, for example `metadata.deviceName` |
| `msgType` | The message type, for example `"POST_TELEMETRY_REQUEST"` |

What the script must give back depends on the node:

| Node | Give back | Example |
|---|---|---|
| Script filter | `true` or `false` | `(msg.temperature ?? 0) > 20` |
| Switch | An array of relation names | `if msg.temperature > 20 { ["High"] } else { ["Normal"] }` |
| Transformation | `#{msg: …, metadata: …, msgType: …}`, or just a new message map | see below |
| Log | Text to write to the log | `` `Temperature: ${msg.temperature}` `` |
| Generator | `#{msg: …, metadata: …, msgType: …}` | see below |
| Create alarm (details) | A map, stored as the alarm details | `#{reading: msg.temperature}` |

Transformation that adds a Fahrenheit value and a metadata key:

```rust
msg.temperatureF = msg.temperature * 1.8 + 32;
metadata.unit = "F";
#{ msg: msg, metadata: metadata, msgType: msgType }
```

Generator that sends a counter. The previous message is in `prevMsg` and `prevMetadata`, empty the first time:

```rust
let n = (prevMsg.count ?? 0) + 1;
#{ msg: #{ count: n }, metadata: #{}, msgType: "POST_TELEMETRY_REQUEST" }
```

Use **Test script function** in the node's editor to run the script on a message you type, before you save.

## Calculated field scripts

Each argument of the field is a variable with the argument's name. The script gives back a map: each key becomes an output key.

```rust
// Dew point from the arguments temperature and humidity
let a = 17.625;
let b = 243.04;
let alpha = (a * temperature) / (b + temperature) + ln(humidity / 100.0);
#{ dewPoint: round((b * alpha) / (a - alpha), 1) }
```

Also available:

| Name | Contains |
|---|---|
| `ctx.latestTs` | The newest timestamp among the arguments, in milliseconds |
| `ctx.args.<name>.ts`, `ctx.args.<name>.value` | Timestamp and value of a single-value argument |
| `previous.<name>` | The argument's value at the previous calculation, `()` the first time |
| `r_trig.<name>`, `f_trig.<name>` | `true` when a true/false argument has just switched on or off, like the PLC blocks R_TRIG and F_TRIG |
| `store` | A map the script can read and change. It is kept for each entity between calculations. SENTIENT keeps it only when the script uses `store` or `ctx.prevTs` |
| `ctx.ts`, `ctx.prevTs` | This calculation's timestamp and the previous one's, when the script keeps a `store` |

A **time series rolling** argument is a list of values over a time window:

| Use | Gives |
|---|---|
| `temperature.mean()`, `.avg()`, `.min()`, `.max()`, `.sum()`, `.count()`, `.std()`, `.median()`, `.first()`, `.last()` | One number. Values that are not numbers are skipped. With `false`, for example `temperature.mean(false)`, such a value makes the result NaN |
| `temperature.values` | An array of `#{ts, value}` |
| `temperature.timeWindow.startTs`, `.endTs` | The window, in milliseconds |
| `temperature.merge(pressure)`, `temperature.mergeAll([b, c])` | The arguments lined up by timestamp |

Running hours of a pump, counted in the `store`:

```rust
if running && ctx.prevTs != () {
    store.ms = (store.ms ?? 0) + (ctx.ts - ctx.prevTs);
}
#{ runningHours: round((store.ms ?? 0) / 3600000.0, 2) }
```

### Shifts and local time

Calculated field scripts know time zones and daylight-saving time. Timestamps are in milliseconds.

| Function | Gives |
|---|---|
| `local_time(ts, "Asia/Kolkata")` | `#{year, month, day, hour, minute, second, weekday, dayOfYear, minuteOfDay, date}`. `weekday` 1 is Monday |
| `shift_of(ts, tz, shifts)` | The shift running at `ts`: `#{name, index, start, end, date}`. `date` is the day the shift started, so a night shift keeps one date |
| `in_windows(ts, tz, windows)` | `true` when `ts` is in one of the windows, for example planned breaks. A window may cross midnight |
| `start_of_day(ts, tz)`, `start_of_hour(ts, tz)` | The start, in milliseconds |
| `format_time(ts, tz, "%Y-%m-%d %H:%M")` | Text |
| `parse_date("2027-03-31", tz)` | Midnight of that date, in milliseconds |

```rust
let shifts = [
    #{ name: "A", start: "06:00", durationMinutes: 480 },
    #{ name: "B", start: "14:00", durationMinutes: 480 },
    #{ name: "C", start: "22:00", durationMinutes: 480 },
];
let s = shift_of(ctx.latestTs, "Asia/Kolkata", shifts);
#{ shift: s.name, shiftDate: s.date }
```

Without `durationMinutes`, a shift lasts until the next one starts.

## Converter scripts

An uplink converter gets `payload` as an array of bytes (0 to 255) and `metadata` as a map, and gives back the device and its values:

```rust
let data = decodeToJson(payload);
#{
    deviceName: data.serial,
    deviceType: "sensor",
    telemetry: #{ temperature: data.t, humidity: data.h }
}
```

Helpers for bytes: `decodeToString`, `decodeToJson`, `bytesToString`, `stringToBytes`, `bytesToHex`, `hexToBytes`, `parseHexToInt`, `parseBytesToInt(bytes, offset, length, bigEndian)`, `base64ToBytes`, `bytesToBase64`, `btoa`, `atob`. They have the same names in JavaScript converters, so a decoder moves between the two languages with only syntax changes.

## Functions

Every script can use Rhai's own functions, for example:

| Kind | Functions |
|---|---|
| Text | `s.len()`, `s.contains("x")`, `s.to_upper()`, `s.to_lower()`, `s.split(",")`, `s.trim()`, `s.sub_string(0, 3)`, `s.parse_int()`, `s.parse_float()` |
| Numbers | `x.to_float()`, `x.to_int()`, `x.to_string()`, `x.to_hex()`, `x.round()`, `x.floor()`, `x.abs()` |
| Arrays | `a.len()`, `a.push(v)`, `a.sort()`, `a.filter(\|v\| v > 1)`, `a.map(\|v\| v * 2)`, `a.contains(v)` |
| Maps | `m.keys()`, `m.values()`, `"key" in m`, `m.remove("key")` |
| Other | `type_of(x)`, `timestamp()` |

SENTIENT adds:

| Where | Functions |
|---|---|
| All scripts | `pow`, `sqrt`, `abs`, `floor`, `ceil`, `round`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `log` (natural), `ln`, `log10`, `log2`, `exp`, `min`, `max`, `clamp`, `pi()`, `e()`, `toFixed(x, digits)`, `isNaN`, `isFinite`, `parse_json(text)` |
| Rule nodes | `stringify(value)`: any value as JSON text |
| Calculated fields | Also `cbrt`, `cot`, `sinh`, `cosh`, `tanh`, `expm1`, `log1p`, `lg`, `logab(base, x)`, `signum`, `trunc`, `round(x, digits)`, `to_number(text)`, `to_int(text)`, `to_string(x)`, `isInfinite`, the constants `PI`, `E`, `PHI`, and the time functions above |

`toFixed` gives text in rule nodes and a number in calculated fields.

## Limits

A script is stopped with an error when it runs more than 1,000,000 operations (2,000,000 in converters), or builds text longer than 5,000,000 characters or an array or map with more than 100,000 entries. Real scripts stay far below this; the limits stop endless loops. Administrators can change them with environment variables on the server:

| Scripts | Variables |
|---|---|
| Rule nodes | `RULE_ENGINE_RHAI_MAX_OPERATIONS`, `RULE_ENGINE_RHAI_MAX_STRING_SIZE`, `RULE_ENGINE_RHAI_MAX_ARRAY_SIZE`, `RULE_ENGINE_RHAI_MAX_MAP_SIZE` |
| Calculated fields | `CF_RHAI_MAX_OPERATIONS`, `CF_RHAI_MAX_STRING_SIZE`, `CF_RHAI_MAX_ARRAY_SIZE`, `CF_RHAI_MAX_MAP_SIZE` |

Each Rhai run counts toward the tenant's **Rhai executions** in [API usage](/docs/administration/api-usage/).

## Coming from Rhai or JavaScript

| Rhai or JavaScript | Rhai |
|---|---|
| `var x = 1;` | `let x = 1;` |
| `{"a": 1}` | `#{a: 1}` or `#{"a": 1}` |
| `foreach (v : list) { … }`, `for (var i = 0; i < n; i++)` | `for v in list { … }`, `for i in 0..n { … }` |
| `list.size()`, `list.length` | `list.len()` |
| `Math.sqrt(x)`, `Math.PI` | `sqrt(x)`, `pi()` |
| `x ^ 2` (Rhai power) | `x ** 2` or `pow(x, 2)` |
| `x === null`, `x == null` | `x == ()` |
| `x || 0` for a missing value | `x ?? 0` |
| `JSON.stringify(v)`, `JSON.parse(s)` | `stringify(v)` in rule nodes, `parse_json(s)` |
| `parseFloat(s)`, `parseInt(s)` | `s.parse_float()`, `s.parse_int()` |
| `'Value: ' + v` | `` `Value: ${v}` `` or `"Value: " + v` |
| `cond ? a : b` | `if cond { a } else { b }` |

## Common mistakes

| You see | Cause | Fix |
|---|---|---|
| The filter is always false | The value arrives as text, `"21.5"` | `msg.temperature.parse_float() > 20`, or send numbers from the device |
| A result has no decimals | Whole-number division: `7 / 2` is `3` | `7 / 2.0` or `x.to_float() / 2` |
| `Unknown property 'y' - a getter is not registered for type '()'` | `msg.x.y` when `x` is missing | `msg?.x?.y`, or check `"x" in msg` first |
| `Function not found` | The function exists only in another script type, for example `shift_of` in a rule node | See [Functions](#functions) |
| `Too many operations` | An endless loop, or a very large loop | Check the loop's end condition |

## Related

- [Calculated fields](/docs/user-guide/calculated-fields/)
- [Alarm rules](/docs/user-guide/alarm-rules/)
- [Rule engine](/docs/user-guide/rule-engine-2-0/re-getting-started/)
- [The Rhai book](https://rhai.rs/book/), the full language reference
