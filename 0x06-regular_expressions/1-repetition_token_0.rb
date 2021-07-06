#!/usr/bin/env ruby
# Matches a repeating token

puts ARGV[0].scan(/hbt{2,5}n/).join
