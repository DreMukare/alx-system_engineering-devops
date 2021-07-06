#!/usr/bin/env ruby
# Matches a repeating token

puts ARGV[0].scan(/^\d{10,10}$/).join
