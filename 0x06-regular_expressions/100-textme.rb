#!/usr/bin/env ruby
# [from:] [to:] [flags:]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

puts ARGV[0].scan(/\[from:(\w+|+\d{11,11})\]\s\[to:(\w+|+\d{10,10})\]\s\[flags:-?\d:-?\d:-?\d:-?\d:-?\d\]/).join
