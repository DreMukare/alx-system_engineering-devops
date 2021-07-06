#!/usr/bin/env ruby
# Matches a phone number of 10 digits

puts ARGV[0].scan(/^\d{10}$/).join
