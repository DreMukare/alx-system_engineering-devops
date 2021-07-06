#!/usr/bin/env ruby
# Matches beginning and end of string with only one character in between

puts ARGV[0].scan(/^h.n$/).join
